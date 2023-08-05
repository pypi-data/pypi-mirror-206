"""_1049.py

ISO6336GeometryBase
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_GEOMETRY_BASE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'ISO6336GeometryBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO6336GeometryBase',)


class ISO6336GeometryBase(_0.APIBase):
    """ISO6336GeometryBase

    This is a mastapy class.
    """

    TYPE = _ISO6336_GEOMETRY_BASE

    class _Cast_ISO6336GeometryBase:
        """Special nested class for casting ISO6336GeometryBase to subclasses."""

        def __init__(self, parent: 'ISO6336GeometryBase'):
            self._parent = parent

        @property
        def iso6336_geometry(self):
            from mastapy.gears.gear_designs.cylindrical import _1048
            
            return self._parent._cast(_1048.ISO6336Geometry)

        @property
        def iso6336_geometry_for_shaped_gears(self):
            from mastapy.gears.gear_designs.cylindrical import _1050
            
            return self._parent._cast(_1050.ISO6336GeometryForShapedGears)

        @property
        def iso6336_geometry_manufactured(self):
            from mastapy.gears.gear_designs.cylindrical import _1051
            
            return self._parent._cast(_1051.ISO6336GeometryManufactured)

        @property
        def iso6336_geometry_base(self) -> 'ISO6336GeometryBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO6336GeometryBase.TYPE'):
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
    def virtual_number_of_teeth(self) -> 'float':
        """float: 'VirtualNumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualNumberOfTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ISO6336GeometryBase._Cast_ISO6336GeometryBase':
        return self._Cast_ISO6336GeometryBase(self)
