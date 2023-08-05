"""_449.py

CylindricalGearDesignAndRatingSettingsDatabase
"""
from mastapy.utility.databases import _1815
from mastapy.gears.rating.cylindrical import _450
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearDesignAndRatingSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearDesignAndRatingSettingsDatabase',)


class CylindricalGearDesignAndRatingSettingsDatabase(_1815.NamedDatabase['_450.CylindricalGearDesignAndRatingSettingsItem']):
    """CylindricalGearDesignAndRatingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS_DATABASE

    class _Cast_CylindricalGearDesignAndRatingSettingsDatabase:
        """Special nested class for casting CylindricalGearDesignAndRatingSettingsDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalGearDesignAndRatingSettingsDatabase'):
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
        def cylindrical_gear_design_and_rating_settings_database(self) -> 'CylindricalGearDesignAndRatingSettingsDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearDesignAndRatingSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearDesignAndRatingSettingsDatabase._Cast_CylindricalGearDesignAndRatingSettingsDatabase':
        return self._Cast_CylindricalGearDesignAndRatingSettingsDatabase(self)
