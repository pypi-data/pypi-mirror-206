# This file is part of django-ca (https://github.com/mathiasertl/django-ca).
#
# django-ca is free software: you can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# django-ca is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along with django-ca. If not, see
# <http://www.gnu.org/licenses/>.

"""Management command to create a certificate authority.

.. seealso:: https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
"""

import argparse
import os
import pathlib
import warnings
from datetime import datetime, timedelta
from datetime import timezone as tz
from typing import Any, Iterable, List, Optional

from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509.oid import ExtensionOID, NameOID

from django.core.management.base import CommandError, CommandParser
from django.utils import timezone

from django_ca import ca_settings, constants
from django_ca.deprecation import RemovedInDjangoCA126Warning
from django_ca.management.actions import (
    ExpiresAction,
    IntegerRangeAction,
    MultipleURLAction,
    NameAction,
    PasswordAction,
)
from django_ca.management.base import BaseSignCommand
from django_ca.management.mixins import CertificateAuthorityDetailMixin
from django_ca.models import CertificateAuthority
from django_ca.tasks import cache_crl, generate_ocsp_key, run_task
from django_ca.typehints import AllowedHashTypes, ParsableKeyType
from django_ca.utils import parse_general_name, sort_name, validate_private_key_parameters


class Command(CertificateAuthorityDetailMixin, BaseSignCommand):
    """Implement :command:`manage.py init_ca`."""

    help = "Create a certificate authority."

    def add_inhibit_any_policy_group(self, parser: CommandParser) -> None:
        """Add argument group for the Inhibit anyPolicy extension."""
        ext_name = constants.EXTENSION_NAMES[ExtensionOID.INHIBIT_ANY_POLICY]
        cert_policies_name = constants.EXTENSION_NAMES[ExtensionOID.CERTIFICATE_POLICIES]
        group = parser.add_argument_group(
            ext_name,
            f"The {ext_name} extension indicates that the special anyPolicy is not considered a match when "
            f"it appears in the {cert_policies_name} extension after the given number of certificates in the "
            "validation path.",
        )
        group.add_argument(
            "--inhibit-any-policy",
            action=IntegerRangeAction,
            min=0,
            help="Number of certificates in the validation path where the anyPolicy is still permitted. "
            "Must be an integer >= 0.",
        )

    def add_name_constraints_group(self, parser: CommandParser) -> argparse._ArgumentGroup:
        """Add an argument group for the NameConstraints extension."""
        group = parser.add_argument_group(
            "Name Constraints", "Add name constraints to the CA, limiting what certificates this CA can sign."
        )
        group.add_argument(
            "--permit-name",
            metavar="NAME",
            action="append",
            type=parse_general_name,
            help="Add NAME to the permitted-subtree.",
        )
        group.add_argument(
            "--exclude-name",
            metavar="NAME",
            action="append",
            type=parse_general_name,
            help="Add NAME to the excluded-subtree.",
        )
        return group

    def add_policy_constraints_group(self, parser: CommandParser) -> None:
        """Add argument group for the Policy Constraints extension."""
        ext_name = constants.EXTENSION_NAMES[ExtensionOID.POLICY_CONSTRAINTS]
        group = parser.add_argument_group(
            constants.EXTENSION_NAMES[ExtensionOID.POLICY_CONSTRAINTS],
            f"The {ext_name} extension can be used to require an explicit policy and/or prohibit policy "
            "mapping.",
        )
        group.add_argument(
            "--inhibit-policy-mapping",
            action=IntegerRangeAction,
            min=0,
            help="Number of certificates in the validation path until policy mapping is no longer permitted.",
        )
        group.add_argument(
            "--require-explicit-policy",
            action=IntegerRangeAction,
            min=0,
            help="Number of certificates in the validation path until an explicit policy for the entire path "
            "is required.",
        )

    def add_arguments(self, parser: CommandParser) -> None:
        default = constants.HASH_ALGORITHM_NAMES[type(ca_settings.CA_DEFAULT_SIGNATURE_HASH_ALGORITHM)]
        dsa_default = constants.HASH_ALGORITHM_NAMES[
            type(ca_settings.CA_DEFAULT_DSA_SIGNATURE_HASH_ALGORITHM)
        ]

        general_group = self.add_general_args(parser)
        general_group.add_argument(
            "--expires",
            metavar="DAYS",
            action=ExpiresAction,
            default=timedelta(365 * 10),
            help="CA certificate expires in DAYS days (default: %(default)s).",
        )
        self.add_algorithm(
            general_group, default_text=f"{default} for RSA/EC keys, {dsa_default} for DSA keys"
        )
        general_group.add_argument(
            "--path",
            type=pathlib.PurePath,
            help="Path where to store Certificate Authorities (relative to CA_DIR).",
        )

        private_key_group = parser.add_argument_group("Private key parameters")
        self.add_key_type(private_key_group)
        self.add_key_size(private_key_group)
        self.add_elliptic_curve(private_key_group)
        self.add_password(
            private_key_group,
            help_text="Encrypt the private key with PASSWORD. If PASSWORD is not passed, you will be "
            "prompted. By default, the private key is not encrypted.",
        )

        intermediate_group = parser.add_argument_group(
            "Intermediate certificate authority", "Options to create an intermediate certificate authority."
        )
        self.add_ca(
            intermediate_group,
            "--parent",
            no_default=True,
            help_text="Make the CA an intermediate CA of the named CA. By default, this is a new root CA.",
        )
        intermediate_group.add_argument(
            "--parent-password",
            nargs="?",
            action=PasswordAction,
            metavar="PASSWORD",
            prompt="Password for parent CA: ",
            help="Password for the private key of any parent CA.",
        )

        parser.add_argument("name", help="Human-readable name of the CA")
        parser.add_argument(
            "subject",
            action=NameAction,
            help='The subject of the CA in the format "/key1=value1/key2=value2/...", requires at least a'
            "CommonName to be present (/CN=...).",
        )

        group = parser.add_argument_group(
            "Default hostname",
            f"""The default hostname is used to compute default URLs for services like OCSP. The hostname is
            usually configured in your settings (current setting: {ca_settings.CA_DEFAULT_HOSTNAME}), but you
            can override that value here. The value must be just the hostname and optionally a port, *without*
            a protocol, e.g.  "ca.example.com" or "ca.example.com:8000".""",
        )
        group = group.add_mutually_exclusive_group()
        group.add_argument(
            "--default-hostname",
            metavar="HOSTNAME",
            help="Override the the default hostname configured in your settings.",
        )
        group.add_argument(
            "--no-default-hostname",
            dest="default_hostname",
            action="store_false",
            help="Disable any default hostname configured in your settings.",
        )

        self.add_acme_group(parser)

        group = parser.add_argument_group(
            "path length attribute",
            """Maximum number of CAs that can appear below this one. A path length of zero (the default) means
            it can only be used to sign end user certificates and not further CAs.""",
        )
        group = group.add_mutually_exclusive_group()
        group.add_argument(
            "--path-length",
            "--pathlen",  # remove in django-ca==1.26.0
            default=0,
            type=int,
            help="Maximum number of intermediate CAs (default: %(default)s).",
        )
        group.add_argument(
            "--no-path-length",
            "--no-pathlen",  # remove in django-ca==1.26.0
            action="store_const",
            const=None,
            dest="path_length",
            help="Do not add a path length attribute.",
        )

        group = parser.add_argument_group(
            "X509 v3 certificate extensions for CA",
            """Extensions for the certificate authority. These options cannot be changed without
            creating a new authority.

            By default, URLs based on the default hostname (see above) will be used. The default URLs work
            out of the box as long as a webserver is correctly configured.
            """,
        )
        group.add_argument(
            "--ca-crl-url",
            action=MultipleURLAction,
            help="URL to a certificate revocation list. Can be given multiple times.",
        )

        aia_group = parser.add_argument_group(
            "Authority Information Access",
            """Information about the issuer of the CA. These options only work for intermediate CAs. Default
            values are based on the default hostname (see above) and work out of the box if a webserver is
            configured. Options can be given multiple times to add multiple values.""",
        )
        aia_group.add_argument(
            "--ca-ocsp-url", metavar="URL", action=MultipleURLAction, help="URL of an OCSP responder."
        )
        aia_group.add_argument(
            "--ca-issuer-url",
            metavar="URL",
            action=MultipleURLAction,
            help="URL to the certificate of your CA (in DER format).",
        )

        self.add_inhibit_any_policy_group(parser)
        self.add_key_usage_group(parser, default=CertificateAuthority.DEFAULT_KEY_USAGE)
        self.add_name_constraints_group(parser)
        self.add_policy_constraints_group(parser)
        self.add_tls_feature_group(parser)

        self.add_ca_args(parser)

    def handle(  # pylint: disable=too-many-arguments,too-many-locals,too-many-branches
        self,
        name: str,
        subject: x509.Name,
        parent: Optional[CertificateAuthority],
        expires: timedelta,
        key_size: Optional[int],
        key_type: ParsableKeyType,
        elliptic_curve: Optional[ec.EllipticCurve],
        algorithm: Optional[AllowedHashTypes],
        path_length: Optional[int],
        password: Optional[bytes],
        parent_password: Optional[bytes],
        crl_url: List[str],
        ocsp_url: Optional[str],
        issuer_url: Optional[str],
        ca_crl_url: List[str],
        ca_ocsp_url: List[str],
        ca_issuer_url: List[str],
        # Inhibit anyPolicy extension:
        inhibit_any_policy: Optional[int],
        # Key Usage extension:
        key_usage: x509.KeyUsage,
        key_usage_critical: bool,
        # NameConstraints extension:
        permit_name: Optional[Iterable[x509.GeneralName]],
        exclude_name: Optional[Iterable[x509.GeneralName]],
        # PolicyConstraints extension:
        require_explicit_policy: Optional[int],
        inhibit_policy_mapping: Optional[int],
        caa: str,
        website: str,
        tos: str,
        **options: Any,
    ) -> None:
        if not os.path.exists(ca_settings.CA_DIR):  # pragma: no cover
            # TODO: set permissions
            os.makedirs(ca_settings.CA_DIR)

        # NOTE: When removing this in 1.26.0, don't forget to remove choices in the --key-type action.
        if key_type == "ECC":  # type: ignore[comparison-overlap]  # that's a deprecated value
            warnings.warn(
                "--key-type=ECC is deprecated, use --key-type=EC instead.", RemovedInDjangoCA126Warning
            )
            key_type = "EC"
        if key_type == "EdDSA":  # type: ignore[comparison-overlap]  # that's a deprecated value
            warnings.warn(
                "--key-type=EdDSA is deprecated, use --key-type=Ed25519 instead.", RemovedInDjangoCA126Warning
            )
            key_type = "Ed25519"

        # Validate private key parameters early so that we can return better feedback to the user.
        try:
            key_size, elliptic_curve = validate_private_key_parameters(key_type, key_size, elliptic_curve)
        except ValueError as ex:
            raise CommandError(*ex.args) from ex

        # Get/validate signature hash algorithm
        algorithm = self.get_hash_algorithm(key_type, algorithm)

        # In case of CAs, we silently set the expiry date to that of the parent CA if the user specified a
        # number of days that would make the CA expire after the parent CA.
        #
        # The reasoning is simple: When issuing the child CA, the default is automatically after that of the
        # parent if it wasn't issued on the same day.
        if parent and timezone.now() + expires > parent.expires:
            expires_datetime = parent.expires

            # Make sure expires_datetime is tz-aware, even if USE_TZ=False.
            if timezone.is_naive(expires_datetime):
                expires_datetime = timezone.make_aware(expires_datetime)
        else:
            expires_datetime = datetime.now(tz=tz.utc) + expires

        if parent and not parent.allows_intermediate_ca:
            raise CommandError("Parent CA cannot create intermediate CA due to path length restrictions.")
        if not parent and ca_crl_url:
            raise CommandError("CRLs cannot be used to revoke root CAs.")
        if not parent and ca_ocsp_url:
            raise CommandError("OCSP cannot be used to revoke root CAs.")

        # We require a valid common name
        common_name = next((attr.value for attr in subject if attr.oid == NameOID.COMMON_NAME), False)
        if not common_name:
            raise CommandError("Subject must contain a common name (/CN=...).")

        # See if we can work with the private key
        if parent:
            self.test_private_key(parent, parent_password)

        subject = sort_name(subject)
        extensions: List[x509.Extension[x509.ExtensionType]] = [
            x509.Extension(oid=ExtensionOID.KEY_USAGE, critical=key_usage_critical, value=key_usage)
        ]
        if inhibit_any_policy is not None:
            extensions.append(
                x509.Extension(
                    oid=ExtensionOID.INHIBIT_ANY_POLICY,
                    critical=constants.EXTENSION_DEFAULT_CRITICAL[ExtensionOID.INHIBIT_ANY_POLICY],
                    value=x509.InhibitAnyPolicy(skip_certs=inhibit_any_policy),
                )
            )
        if require_explicit_policy is not None or inhibit_policy_mapping is not None:
            extensions.append(
                x509.Extension(
                    oid=ExtensionOID.POLICY_CONSTRAINTS,
                    critical=constants.EXTENSION_DEFAULT_CRITICAL[ExtensionOID.POLICY_CONSTRAINTS],
                    value=x509.PolicyConstraints(
                        require_explicit_policy=require_explicit_policy,
                        inhibit_policy_mapping=inhibit_policy_mapping,
                    ),
                )
            )

        issuer_alternative_name = options[constants.EXTENSION_KEYS[x509.IssuerAlternativeName.oid]]

        kwargs = {}
        for opt in ["path", "default_hostname"]:
            if options[opt] is not None:
                kwargs[opt] = options[opt]

        if ca_settings.CA_ENABLE_ACME:  # pragma: no branch; never False because parser throws error already
            # These settings are only there if ACME is enabled
            for opt in ["acme_enabled", "acme_requires_contact"]:
                if options[opt] is not None:
                    kwargs[opt] = options[opt]

            if acme_profile := options["acme_profile"]:
                if acme_profile not in ca_settings.CA_PROFILES:
                    raise CommandError(f"{acme_profile}: Profile is not defined.")
                kwargs["acme_profile"] = acme_profile

        try:
            ca = CertificateAuthority.objects.init(
                name=name,
                subject=subject,
                expires=expires_datetime,
                algorithm=algorithm,
                parent=parent,
                path_length=path_length,
                issuer_url=issuer_url,
                issuer_alt_name=issuer_alternative_name,
                crl_url=crl_url,
                ocsp_url=ocsp_url,
                ca_issuer_url=ca_issuer_url,
                ca_crl_url=ca_crl_url,
                ca_ocsp_url=ca_ocsp_url,
                permitted_subtrees=permit_name,
                excluded_subtrees=exclude_name,
                password=password,
                parent_password=parent_password,
                elliptic_curve=elliptic_curve,
                key_type=key_type,
                key_size=key_size,
                caa=caa,
                website=website,
                terms_of_service=tos,
                extensions=extensions,
                **kwargs,
            )
        except Exception as ex:  # pragma: no cover
            raise CommandError(ex) from ex

        # Generate OCSP keys and cache CRLs
        run_task(generate_ocsp_key, serial=ca.serial, password=password)
        run_task(cache_crl, serial=ca.serial, password=password)
