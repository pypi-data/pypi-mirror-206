"""_1292.py

StatorRotorMaterialDatabase
"""
from mastapy.materials import _266
from mastapy.electric_machines import _1291
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR_ROTOR_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.ElectricMachines', 'StatorRotorMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('StatorRotorMaterialDatabase',)


class StatorRotorMaterialDatabase(_266.MaterialDatabase['_1291.StatorRotorMaterial']):
    """StatorRotorMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _STATOR_ROTOR_MATERIAL_DATABASE

    class _Cast_StatorRotorMaterialDatabase:
        """Special nested class for casting StatorRotorMaterialDatabase to subclasses."""

        def __init__(self, parent: 'StatorRotorMaterialDatabase'):
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
        def stator_rotor_material_database(self) -> 'StatorRotorMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StatorRotorMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase':
        return self._Cast_StatorRotorMaterialDatabase(self)
