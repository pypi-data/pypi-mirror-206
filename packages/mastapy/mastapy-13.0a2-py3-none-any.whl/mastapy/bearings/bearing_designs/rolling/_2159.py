"""_2159.py

ToroidalRollerBearing
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.rolling import _2127
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOROIDAL_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'ToroidalRollerBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('ToroidalRollerBearing',)


class ToroidalRollerBearing(_2127.BarrelRollerBearing):
    """ToroidalRollerBearing

    This is a mastapy class.
    """

    TYPE = _TOROIDAL_ROLLER_BEARING

    class _Cast_ToroidalRollerBearing:
        """Special nested class for casting ToroidalRollerBearing to subclasses."""

        def __init__(self, parent: 'ToroidalRollerBearing'):
            self._parent = parent

        @property
        def barrel_roller_bearing(self):
            return self._parent._cast(_2127.BarrelRollerBearing)

        @property
        def roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2147
            
            return self._parent._cast(_2147.RollerBearing)

        @property
        def rolling_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2150
            
            return self._parent._cast(_2150.RollingBearing)

        @property
        def detailed_bearing(self):
            from mastapy.bearings.bearing_designs import _2116
            
            return self._parent._cast(_2116.DetailedBearing)

        @property
        def non_linear_bearing(self):
            from mastapy.bearings.bearing_designs import _2119
            
            return self._parent._cast(_2119.NonLinearBearing)

        @property
        def bearing_design(self):
            from mastapy.bearings.bearing_designs import _2115
            
            return self._parent._cast(_2115.BearingDesign)

        @property
        def toroidal_roller_bearing(self) -> 'ToroidalRollerBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ToroidalRollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_displacement_capability(self) -> 'float':
        """float: 'AxialDisplacementCapability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialDisplacementCapability

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_displacement_capability_towards_snap_ring(self) -> 'float':
        """float: 'AxialDisplacementCapabilityTowardsSnapRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialDisplacementCapabilityTowardsSnapRing

        if temp is None:
            return 0.0

        return temp

    @property
    def snap_ring_offset_from_element(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SnapRingOffsetFromElement' is the original name of this property."""

        temp = self.wrapped.SnapRingOffsetFromElement

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @snap_ring_offset_from_element.setter
    def snap_ring_offset_from_element(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SnapRingOffsetFromElement = value

    @property
    def snap_ring_width(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SnapRingWidth' is the original name of this property."""

        temp = self.wrapped.SnapRingWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @snap_ring_width.setter
    def snap_ring_width(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SnapRingWidth = value

    @property
    def cast_to(self) -> 'ToroidalRollerBearing._Cast_ToroidalRollerBearing':
        return self._Cast_ToroidalRollerBearing(self)
