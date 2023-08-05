"""_2127.py

BarrelRollerBearing
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.bearings.bearing_designs.rolling import _2147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BARREL_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'BarrelRollerBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('BarrelRollerBearing',)


class BarrelRollerBearing(_2147.RollerBearing):
    """BarrelRollerBearing

    This is a mastapy class.
    """

    TYPE = _BARREL_ROLLER_BEARING

    class _Cast_BarrelRollerBearing:
        """Special nested class for casting BarrelRollerBearing to subclasses."""

        def __init__(self, parent: 'BarrelRollerBearing'):
            self._parent = parent

        @property
        def roller_bearing(self):
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
        def spherical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2154
            
            return self._parent._cast(_2154.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2155
            
            return self._parent._cast(_2155.SphericalRollerThrustBearing)

        @property
        def toroidal_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2159
            
            return self._parent._cast(_2159.ToroidalRollerBearing)

        @property
        def barrel_roller_bearing(self) -> 'BarrelRollerBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BarrelRollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_profile_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ElementProfileRadius' is the original name of this property."""

        temp = self.wrapped.ElementProfileRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @element_profile_radius.setter
    def element_profile_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ElementProfileRadius = value

    @property
    def groove_radius_inner(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'GrooveRadiusInner' is the original name of this property."""

        temp = self.wrapped.GrooveRadiusInner

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @groove_radius_inner.setter
    def groove_radius_inner(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.GrooveRadiusInner = value

    @property
    def groove_radius_outer(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'GrooveRadiusOuter' is the original name of this property."""

        temp = self.wrapped.GrooveRadiusOuter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @groove_radius_outer.setter
    def groove_radius_outer(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.GrooveRadiusOuter = value

    @property
    def roller_race_radius_ratio(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RollerRaceRadiusRatio' is the original name of this property."""

        temp = self.wrapped.RollerRaceRadiusRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @roller_race_radius_ratio.setter
    def roller_race_radius_ratio(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RollerRaceRadiusRatio = value

    @property
    def cast_to(self) -> 'BarrelRollerBearing._Cast_BarrelRollerBearing':
        return self._Cast_BarrelRollerBearing(self)
