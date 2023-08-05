"""_7517.py

EnvironmentVariableUtility
"""
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENVIRONMENT_VARIABLE_UTILITY = python_net_import('SMT.MastaAPIUtility', 'EnvironmentVariableUtility')


__docformat__ = 'restructuredtext en'
__all__ = ('EnvironmentVariableUtility',)


class EnvironmentVariableUtility:
    """EnvironmentVariableUtility

    This is a mastapy class.
    """

    TYPE = _ENVIRONMENT_VARIABLE_UTILITY

    class _Cast_EnvironmentVariableUtility:
        """Special nested class for casting EnvironmentVariableUtility to subclasses."""

        def __init__(self, parent: 'EnvironmentVariableUtility'):
            self._parent = parent

        @property
        def environment_variable_utility(self) -> 'EnvironmentVariableUtility':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EnvironmentVariableUtility.TYPE'):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, 'reference_count'):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @staticmethod
    def add_to_path_if_necessary(directory: 'str'):
        """ 'AddToPathIfNecessary' is the original name of this method.

        Args:
            directory (str)
        """

        directory = str(directory)
        EnvironmentVariableUtility.TYPE.AddToPathIfNecessary(directory if directory else '')

    @property
    def cast_to(self) -> 'EnvironmentVariableUtility._Cast_EnvironmentVariableUtility':
        return self._Cast_EnvironmentVariableUtility(self)
