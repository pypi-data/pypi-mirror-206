"""_242.py

BearingMaterialDatabase
"""
from mastapy.utility.databases import _1815
from mastapy.materials import _241
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Materials', 'BearingMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingMaterialDatabase',)


class BearingMaterialDatabase(_1815.NamedDatabase['_241.BearingMaterial']):
    """BearingMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BEARING_MATERIAL_DATABASE

    class _Cast_BearingMaterialDatabase:
        """Special nested class for casting BearingMaterialDatabase to subclasses."""

        def __init__(self, parent: 'BearingMaterialDatabase'):
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
        def bearing_material_database(self) -> 'BearingMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BearingMaterialDatabase._Cast_BearingMaterialDatabase':
        return self._Cast_BearingMaterialDatabase(self)
