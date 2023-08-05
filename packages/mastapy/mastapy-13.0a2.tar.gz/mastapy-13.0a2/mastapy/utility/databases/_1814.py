"""_1814.py

DatabaseSettings
"""
from mastapy.utility.databases import _1812
from mastapy._internal import constructor
from mastapy.utility import _1583
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATABASE_SETTINGS = python_net_import('SMT.MastaAPI.Utility.Databases', 'DatabaseSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('DatabaseSettings',)


class DatabaseSettings(_1583.PerMachineSettings):
    """DatabaseSettings

    This is a mastapy class.
    """

    TYPE = _DATABASE_SETTINGS

    class _Cast_DatabaseSettings:
        """Special nested class for casting DatabaseSettings to subclasses."""

        def __init__(self, parent: 'DatabaseSettings'):
            self._parent = parent

        @property
        def per_machine_settings(self):
            return self._parent._cast(_1583.PerMachineSettings)

        @property
        def persistent_singleton(self):
            from mastapy.utility import _1584
            
            return self._parent._cast(_1584.PersistentSingleton)

        @property
        def database_settings(self) -> 'DatabaseSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DatabaseSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_settings(self) -> '_1812.DatabaseConnectionSettings':
        """DatabaseConnectionSettings: 'ConnectionSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'DatabaseSettings._Cast_DatabaseSettings':
        return self._Cast_DatabaseSettings(self)
