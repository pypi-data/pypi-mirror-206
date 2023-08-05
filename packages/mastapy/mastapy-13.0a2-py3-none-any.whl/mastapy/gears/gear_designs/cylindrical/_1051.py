"""_1051.py

ISO6336GeometryManufactured
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1049
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_GEOMETRY_MANUFACTURED = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'ISO6336GeometryManufactured')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO6336GeometryManufactured',)


class ISO6336GeometryManufactured(_1049.ISO6336GeometryBase):
    """ISO6336GeometryManufactured

    This is a mastapy class.
    """

    TYPE = _ISO6336_GEOMETRY_MANUFACTURED

    class _Cast_ISO6336GeometryManufactured:
        """Special nested class for casting ISO6336GeometryManufactured to subclasses."""

        def __init__(self, parent: 'ISO6336GeometryManufactured'):
            self._parent = parent

        @property
        def iso6336_geometry_base(self):
            return self._parent._cast(_1049.ISO6336GeometryBase)

        @property
        def iso6336_geometry_manufactured(self) -> 'ISO6336GeometryManufactured':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO6336GeometryManufactured.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def iso6336_root_fillet_radius(self) -> 'float':
        """float: 'ISO6336RootFilletRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO6336RootFilletRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def iso6336_tooth_root_chord(self) -> 'float':
        """float: 'ISO6336ToothRootChord' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO6336ToothRootChord

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ISO6336GeometryManufactured._Cast_ISO6336GeometryManufactured':
        return self._Cast_ISO6336GeometryManufactured(self)
