"""_587.py

CylindricalGearMaterialDatabase
"""
from typing import TypeVar

from mastapy.materials import _266
from mastapy.gears.materials import _586
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'CylindricalGearMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMaterialDatabase',)


T = TypeVar('T', bound='_586.CylindricalGearMaterial')


class CylindricalGearMaterialDatabase(_266.MaterialDatabase[T]):
    """CylindricalGearMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _CYLINDRICAL_GEAR_MATERIAL_DATABASE

    class _Cast_CylindricalGearMaterialDatabase:
        """Special nested class for casting CylindricalGearMaterialDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalGearMaterialDatabase'):
            self._parent = parent

        @property
        def material_database(self):
            return self._parent._cast(_266.MaterialDatabase)

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
        def cylindrical_gear_agma_material_database(self):
            from mastapy.gears.materials import _584
            
            return self._parent._cast(_584.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(self):
            from mastapy.gears.materials import _585
            
            return self._parent._cast(_585.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(self):
            from mastapy.gears.materials import _588
            
            return self._parent._cast(_588.CylindricalGearPlasticMaterialDatabase)

        @property
        def cylindrical_gear_material_database(self) -> 'CylindricalGearMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase':
        return self._Cast_CylindricalGearMaterialDatabase(self)
