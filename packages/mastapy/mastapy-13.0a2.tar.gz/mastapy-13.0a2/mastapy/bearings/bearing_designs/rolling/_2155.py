"""_2155.py

SphericalRollerThrustBearing
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.rolling import _2127
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPHERICAL_ROLLER_THRUST_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'SphericalRollerThrustBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('SphericalRollerThrustBearing',)


class SphericalRollerThrustBearing(_2127.BarrelRollerBearing):
    """SphericalRollerThrustBearing

    This is a mastapy class.
    """

    TYPE = _SPHERICAL_ROLLER_THRUST_BEARING

    class _Cast_SphericalRollerThrustBearing:
        """Special nested class for casting SphericalRollerThrustBearing to subclasses."""

        def __init__(self, parent: 'SphericalRollerThrustBearing'):
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
        def spherical_roller_thrust_bearing(self) -> 'SphericalRollerThrustBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SphericalRollerThrustBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_roller_end_and_bearing_axis(self) -> 'float':
        """float: 'AngleBetweenRollerEndAndBearingAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngleBetweenRollerEndAndBearingAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_to_pressure_point_from_left_face(self) -> 'float':
        """float: 'DistanceToPressurePointFromLeftFace' is the original name of this property."""

        temp = self.wrapped.DistanceToPressurePointFromLeftFace

        if temp is None:
            return 0.0

        return temp

    @distance_to_pressure_point_from_left_face.setter
    def distance_to_pressure_point_from_left_face(self, value: 'float'):
        self.wrapped.DistanceToPressurePointFromLeftFace = float(value) if value else 0.0

    @property
    def effective_taper_angle(self) -> 'float':
        """float: 'EffectiveTaperAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveTaperAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def element_centre_point_diameter(self) -> 'float':
        """float: 'ElementCentrePointDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementCentrePointDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def major_diameter_offset_from_roller_centre(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MajorDiameterOffsetFromRollerCentre' is the original name of this property."""

        temp = self.wrapped.MajorDiameterOffsetFromRollerCentre

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @major_diameter_offset_from_roller_centre.setter
    def major_diameter_offset_from_roller_centre(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MajorDiameterOffsetFromRollerCentre = value

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'SphericalRollerThrustBearing._Cast_SphericalRollerThrustBearing':
        return self._Cast_SphericalRollerThrustBearing(self)
