"""_590.py

GearMaterialDatabase
"""
from typing import TypeVar

from mastapy.utility.databases import _1815
from mastapy.gears.materials import _589
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'GearMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMaterialDatabase',)


T = TypeVar('T', bound='_589.GearMaterial')


class GearMaterialDatabase(_1815.NamedDatabase[T]):
    """GearMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _GEAR_MATERIAL_DATABASE

    class _Cast_GearMaterialDatabase:
        """Special nested class for casting GearMaterialDatabase to subclasses."""

        def __init__(self, parent: 'GearMaterialDatabase'):
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
        def bevel_gear_material_database(self):
            from mastapy.gears.materials import _583
            
            return self._parent._cast(_583.BevelGearMaterialDatabase)

        @property
        def klingelnberg_conical_gear_material_database(self):
            from mastapy.gears.materials import _595
            
            return self._parent._cast(_595.KlingelnbergConicalGearMaterialDatabase)

        @property
        def gear_material_database(self) -> 'GearMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearMaterialDatabase._Cast_GearMaterialDatabase':
        return self._Cast_GearMaterialDatabase(self)
