"""_2.py

LegacyV2RuntimeActivationPolicyAttributeSetter
"""
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEGACY_V2_RUNTIME_ACTIVATION_POLICY_ATTRIBUTE_SETTER = python_net_import('SMT.MastaAPI', 'LegacyV2RuntimeActivationPolicyAttributeSetter')


__docformat__ = 'restructuredtext en'
__all__ = ('LegacyV2RuntimeActivationPolicyAttributeSetter',)


class LegacyV2RuntimeActivationPolicyAttributeSetter:
    """LegacyV2RuntimeActivationPolicyAttributeSetter

    This is a mastapy class.
    """

    TYPE = _LEGACY_V2_RUNTIME_ACTIVATION_POLICY_ATTRIBUTE_SETTER

    class _Cast_LegacyV2RuntimeActivationPolicyAttributeSetter:
        """Special nested class for casting LegacyV2RuntimeActivationPolicyAttributeSetter to subclasses."""

        def __init__(self, parent: 'LegacyV2RuntimeActivationPolicyAttributeSetter'):
            self._parent = parent

        @property
        def legacy_v2_runtime_activation_policy_attribute_setter(self) -> 'LegacyV2RuntimeActivationPolicyAttributeSetter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LegacyV2RuntimeActivationPolicyAttributeSetter.TYPE'):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, 'reference_count'):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @staticmethod
    def ensure_config_file_for_current_app_domain_permits_dot_net_2():
        """ 'EnsureConfigFileForCurrentAppDomainPermitsDotNet2' is the original name of this method."""

        LegacyV2RuntimeActivationPolicyAttributeSetter.TYPE.EnsureConfigFileForCurrentAppDomainPermitsDotNet2()

    @staticmethod
    def get_config_file_path_for_setup_assembly() -> 'str':
        """ 'GetConfigFilePathForSetupAssembly' is the original name of this method.

        Returns:
            str
        """

        method_result = LegacyV2RuntimeActivationPolicyAttributeSetter.TYPE.GetConfigFilePathForSetupAssembly()
        return method_result

    @property
    def cast_to(self) -> 'LegacyV2RuntimeActivationPolicyAttributeSetter._Cast_LegacyV2RuntimeActivationPolicyAttributeSetter':
        return self._Cast_LegacyV2RuntimeActivationPolicyAttributeSetter(self)
