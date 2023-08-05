"""_68.py

FEUserSettings
"""
from mastapy.utility import _1583
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_USER_SETTINGS = python_net_import('SMT.MastaAPI.NodalAnalysis', 'FEUserSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('FEUserSettings',)


class FEUserSettings(_1583.PerMachineSettings):
    """FEUserSettings

    This is a mastapy class.
    """

    TYPE = _FE_USER_SETTINGS

    class _Cast_FEUserSettings:
        """Special nested class for casting FEUserSettings to subclasses."""

        def __init__(self, parent: 'FEUserSettings'):
            self._parent = parent

        @property
        def per_machine_settings(self):
            return self._parent._cast(_1583.PerMachineSettings)

        @property
        def persistent_singleton(self):
            from mastapy.utility import _1584
            
            return self._parent._cast(_1584.PersistentSingleton)

        @property
        def fe_user_settings(self) -> 'FEUserSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEUserSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FEUserSettings._Cast_FEUserSettings':
        return self._Cast_FEUserSettings(self)
