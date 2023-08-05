"""_1451.py

RingPinsMaterial
"""
from mastapy.materials import _265
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_MATERIAL = python_net_import('SMT.MastaAPI.Cycloidal', 'RingPinsMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsMaterial',)


class RingPinsMaterial(_265.Material):
    """RingPinsMaterial

    This is a mastapy class.
    """

    TYPE = _RING_PINS_MATERIAL

    class _Cast_RingPinsMaterial:
        """Special nested class for casting RingPinsMaterial to subclasses."""

        def __init__(self, parent: 'RingPinsMaterial'):
            self._parent = parent

        @property
        def material(self):
            return self._parent._cast(_265.Material)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def ring_pins_material(self) -> 'RingPinsMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingPinsMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RingPinsMaterial._Cast_RingPinsMaterial':
        return self._Cast_RingPinsMaterial(self)
