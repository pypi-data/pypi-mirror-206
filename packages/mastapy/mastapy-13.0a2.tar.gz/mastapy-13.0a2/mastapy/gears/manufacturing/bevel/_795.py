"""_795.py

ManufacturingMachineDatabase
"""
from mastapy.utility.databases import _1815
from mastapy.gears.manufacturing.bevel import _794
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MANUFACTURING_MACHINE_DATABASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ManufacturingMachineDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ManufacturingMachineDatabase',)


class ManufacturingMachineDatabase(_1815.NamedDatabase['_794.ManufacturingMachine']):
    """ManufacturingMachineDatabase

    This is a mastapy class.
    """

    TYPE = _MANUFACTURING_MACHINE_DATABASE

    class _Cast_ManufacturingMachineDatabase:
        """Special nested class for casting ManufacturingMachineDatabase to subclasses."""

        def __init__(self, parent: 'ManufacturingMachineDatabase'):
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
        def manufacturing_machine_database(self) -> 'ManufacturingMachineDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ManufacturingMachineDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ManufacturingMachineDatabase._Cast_ManufacturingMachineDatabase':
        return self._Cast_ManufacturingMachineDatabase(self)
