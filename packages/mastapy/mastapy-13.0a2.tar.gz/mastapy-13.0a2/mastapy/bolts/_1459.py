"""_1459.py

BoltMaterialDatabase
"""
from mastapy.bolts import _1455, _1458
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Bolts', 'BoltMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltMaterialDatabase',)


class BoltMaterialDatabase(_1455.BoltedJointMaterialDatabase['_1458.BoltMaterial']):
    """BoltMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BOLT_MATERIAL_DATABASE

    class _Cast_BoltMaterialDatabase:
        """Special nested class for casting BoltMaterialDatabase to subclasses."""

        def __init__(self, parent: 'BoltMaterialDatabase'):
            self._parent = parent

        @property
        def bolted_joint_material_database(self):
            return self._parent._cast(_1455.BoltedJointMaterialDatabase)

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
        def bolt_material_database(self) -> 'BoltMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoltMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BoltMaterialDatabase._Cast_BoltMaterialDatabase':
        return self._Cast_BoltMaterialDatabase(self)
