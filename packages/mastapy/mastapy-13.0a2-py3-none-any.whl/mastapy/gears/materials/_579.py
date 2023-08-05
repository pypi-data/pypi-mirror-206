"""_579.py

BevelGearAbstractMaterialDatabase
"""
from typing import TypeVar

from mastapy.materials import _266
from mastapy.gears.materials import _582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_ABSTRACT_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'BevelGearAbstractMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearAbstractMaterialDatabase',)


T = TypeVar('T', bound='_582.BevelGearMaterial')


class BevelGearAbstractMaterialDatabase(_266.MaterialDatabase[T]):
    """BevelGearAbstractMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _BEVEL_GEAR_ABSTRACT_MATERIAL_DATABASE

    class _Cast_BevelGearAbstractMaterialDatabase:
        """Special nested class for casting BevelGearAbstractMaterialDatabase to subclasses."""

        def __init__(self, parent: 'BevelGearAbstractMaterialDatabase'):
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
        def bevel_gear_iso_material_database(self):
            from mastapy.gears.materials import _581
            
            return self._parent._cast(_581.BevelGearIsoMaterialDatabase)

        @property
        def bevel_gear_abstract_material_database(self) -> 'BevelGearAbstractMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearAbstractMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase':
        return self._Cast_BevelGearAbstractMaterialDatabase(self)
