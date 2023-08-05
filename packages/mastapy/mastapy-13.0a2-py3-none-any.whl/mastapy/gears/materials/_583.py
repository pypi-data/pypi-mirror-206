"""_583.py

BevelGearMaterialDatabase
"""
from mastapy.gears.materials import _590, _582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'BevelGearMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearMaterialDatabase',)


class BevelGearMaterialDatabase(_590.GearMaterialDatabase['_582.BevelGearMaterial']):
    """BevelGearMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MATERIAL_DATABASE

    class _Cast_BevelGearMaterialDatabase:
        """Special nested class for casting BevelGearMaterialDatabase to subclasses."""

        def __init__(self, parent: 'BevelGearMaterialDatabase'):
            self._parent = parent

        @property
        def gear_material_database(self):
            return self._parent._cast(_590.GearMaterialDatabase)

        @property
        def named_database(self):
            from mastapy.utility.databases import _1815
            
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
        def bevel_gear_material_database(self) -> 'BevelGearMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase':
        return self._Cast_BevelGearMaterialDatabase(self)
