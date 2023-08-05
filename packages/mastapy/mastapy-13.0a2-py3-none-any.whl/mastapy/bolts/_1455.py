"""_1455.py

BoltedJointMaterialDatabase
"""
from typing import TypeVar

from mastapy.utility.databases import _1815
from mastapy.bolts import _1454
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Bolts', 'BoltedJointMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointMaterialDatabase',)


T = TypeVar('T', bound='_1454.BoltedJointMaterial')


class BoltedJointMaterialDatabase(_1815.NamedDatabase[T]):
    """BoltedJointMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _BOLTED_JOINT_MATERIAL_DATABASE

    class _Cast_BoltedJointMaterialDatabase:
        """Special nested class for casting BoltedJointMaterialDatabase to subclasses."""

        def __init__(self, parent: 'BoltedJointMaterialDatabase'):
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
        def bolt_material_database(self):
            from mastapy.bolts import _1459
            
            return self._parent._cast(_1459.BoltMaterialDatabase)

        @property
        def clamped_section_material_database(self):
            from mastapy.bolts import _1464
            
            return self._parent._cast(_1464.ClampedSectionMaterialDatabase)

        @property
        def bolted_joint_material_database(self) -> 'BoltedJointMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoltedJointMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BoltedJointMaterialDatabase._Cast_BoltedJointMaterialDatabase':
        return self._Cast_BoltedJointMaterialDatabase(self)
