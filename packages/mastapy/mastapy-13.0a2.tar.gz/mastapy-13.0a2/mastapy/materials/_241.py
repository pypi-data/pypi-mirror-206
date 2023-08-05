"""_241.py

BearingMaterial
"""
from mastapy.materials import _265
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_MATERIAL = python_net_import('SMT.MastaAPI.Materials', 'BearingMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingMaterial',)


class BearingMaterial(_265.Material):
    """BearingMaterial

    This is a mastapy class.
    """

    TYPE = _BEARING_MATERIAL

    class _Cast_BearingMaterial:
        """Special nested class for casting BearingMaterial to subclasses."""

        def __init__(self, parent: 'BearingMaterial'):
            self._parent = parent

        @property
        def material(self):
            return self._parent._cast(_265.Material)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def bearing_material(self) -> 'BearingMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BearingMaterial._Cast_BearingMaterial':
        return self._Cast_BearingMaterial(self)
