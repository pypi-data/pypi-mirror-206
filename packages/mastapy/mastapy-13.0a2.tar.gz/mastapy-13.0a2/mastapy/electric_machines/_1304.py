"""_1304.py

WindingMaterialDatabase
"""
from mastapy.materials import _266
from mastapy.electric_machines import _1303
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WINDING_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.ElectricMachines', 'WindingMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('WindingMaterialDatabase',)


class WindingMaterialDatabase(_266.MaterialDatabase['_1303.WindingMaterial']):
    """WindingMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _WINDING_MATERIAL_DATABASE

    class _Cast_WindingMaterialDatabase:
        """Special nested class for casting WindingMaterialDatabase to subclasses."""

        def __init__(self, parent: 'WindingMaterialDatabase'):
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
        def winding_material_database(self) -> 'WindingMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WindingMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'WindingMaterialDatabase._Cast_WindingMaterialDatabase':
        return self._Cast_WindingMaterialDatabase(self)
