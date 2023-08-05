"""_937.py

BevelHypoidGearRatingSettingsDatabase
"""
from mastapy.utility.databases import _1815
from mastapy.gears.gear_designs import _938
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_RATING_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'BevelHypoidGearRatingSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelHypoidGearRatingSettingsDatabase',)


class BevelHypoidGearRatingSettingsDatabase(_1815.NamedDatabase['_938.BevelHypoidGearRatingSettingsItem']):
    """BevelHypoidGearRatingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_RATING_SETTINGS_DATABASE

    class _Cast_BevelHypoidGearRatingSettingsDatabase:
        """Special nested class for casting BevelHypoidGearRatingSettingsDatabase to subclasses."""

        def __init__(self, parent: 'BevelHypoidGearRatingSettingsDatabase'):
            self._parent = parent

        @property
        def named_database(self):
            return self._parent._cast(_1815.NamedDatabase)

        @property
        def sql_database(self):
            from mastapy.utility.databases import _1818, _1817
            
            return self._parent._cast(_1818.SQLDatabase)

        @property
        def database(self):
            from mastapy.utility.databases import _1811, _1817
            
            return self._parent._cast(_1811.Database)

        @property
        def bevel_hypoid_gear_rating_settings_database(self) -> 'BevelHypoidGearRatingSettingsDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelHypoidGearRatingSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelHypoidGearRatingSettingsDatabase._Cast_BevelHypoidGearRatingSettingsDatabase':
        return self._Cast_BevelHypoidGearRatingSettingsDatabase(self)
