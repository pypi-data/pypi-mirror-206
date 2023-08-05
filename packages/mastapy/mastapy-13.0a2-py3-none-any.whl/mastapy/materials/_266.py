"""_266.py

MaterialDatabase
"""
from typing import TypeVar

from mastapy.utility.databases import _1815
from mastapy.materials import _265
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Materials', 'MaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('MaterialDatabase',)


T = TypeVar('T', bound='_265.Material')


class MaterialDatabase(_1815.NamedDatabase[T]):
    """MaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _MATERIAL_DATABASE

    class _Cast_MaterialDatabase:
        """Special nested class for casting MaterialDatabase to subclasses."""

        def __init__(self, parent: 'MaterialDatabase'):
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
        def shaft_material_database(self):
            from mastapy.shafts import _25
            
            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def bevel_gear_abstract_material_database(self):
            from mastapy.gears.materials import _579
            
            return self._parent._cast(_579.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(self):
            from mastapy.gears.materials import _581
            
            return self._parent._cast(_581.BevelGearIsoMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(self):
            from mastapy.gears.materials import _584
            
            return self._parent._cast(_584.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(self):
            from mastapy.gears.materials import _585
            
            return self._parent._cast(_585.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(self):
            from mastapy.gears.materials import _587
            
            return self._parent._cast(_587.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(self):
            from mastapy.gears.materials import _588
            
            return self._parent._cast(_588.CylindricalGearPlasticMaterialDatabase)

        @property
        def magnet_material_database(self):
            from mastapy.electric_machines import _1274
            
            return self._parent._cast(_1274.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(self):
            from mastapy.electric_machines import _1292
            
            return self._parent._cast(_1292.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(self):
            from mastapy.electric_machines import _1304
            
            return self._parent._cast(_1304.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(self):
            from mastapy.cycloidal import _1445
            
            return self._parent._cast(_1445.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(self):
            from mastapy.cycloidal import _1452
            
            return self._parent._cast(_1452.RingPinsMaterialDatabase)

        @property
        def material_database(self) -> 'MaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MaterialDatabase._Cast_MaterialDatabase':
        return self._Cast_MaterialDatabase(self)
