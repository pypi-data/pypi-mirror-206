"""_2147.py

RollerBearing
"""
from typing import List

from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings import _1876
from mastapy.bearings.roller_bearing_profiles import _1913, _1923
from mastapy.bearings.bearing_designs.rolling import _2150
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'RollerBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('RollerBearing',)


class RollerBearing(_2150.RollingBearing):
    """RollerBearing

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING

    class _Cast_RollerBearing:
        """Special nested class for casting RollerBearing to subclasses."""

        def __init__(self, parent: 'RollerBearing'):
            self._parent = parent

        @property
        def rolling_bearing(self):
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
        def asymmetric_spherical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2122
            
            return self._parent._cast(_2122.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2123
            
            return self._parent._cast(_2123.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2124
            
            return self._parent._cast(_2124.AxialThrustNeedleRollerBearing)

        @property
        def barrel_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2127
            
            return self._parent._cast(_2127.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2133
            
            return self._parent._cast(_2133.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2134
            
            return self._parent._cast(_2134.CylindricalRollerBearing)

        @property
        def needle_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2145
            
            return self._parent._cast(_2145.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2146
            
            return self._parent._cast(_2146.NonBarrelRollerBearing)

        @property
        def spherical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2154
            
            return self._parent._cast(_2154.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2155
            
            return self._parent._cast(_2155.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2156
            
            return self._parent._cast(_2156.TaperRollerBearing)

        @property
        def toroidal_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2159
            
            return self._parent._cast(_2159.ToroidalRollerBearing)

        @property
        def roller_bearing(self) -> 'RollerBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def corner_radii(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CornerRadii' is the original name of this property."""

        temp = self.wrapped.CornerRadii

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @corner_radii.setter
    def corner_radii(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CornerRadii = value

    @property
    def effective_roller_length(self) -> 'float':
        """float: 'EffectiveRollerLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveRollerLength

        if temp is None:
            return 0.0

        return temp

    @property
    def element_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ElementDiameter' is the original name of this property."""

        temp = self.wrapped.ElementDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @element_diameter.setter
    def element_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ElementDiameter = value

    @property
    def kl(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'KL' is the original name of this property."""

        temp = self.wrapped.KL

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @kl.setter
    def kl(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.KL = value

    @property
    def roller_length(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RollerLength' is the original name of this property."""

        temp = self.wrapped.RollerLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @roller_length.setter
    def roller_length(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RollerLength = value

    @property
    def roller_profile(self) -> 'enum_with_selected_value.EnumWithSelectedValue_RollerBearingProfileTypes':
        """enum_with_selected_value.EnumWithSelectedValue_RollerBearingProfileTypes: 'RollerProfile' is the original name of this property."""

        temp = self.wrapped.RollerProfile

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_RollerBearingProfileTypes.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @roller_profile.setter
    def roller_profile(self, value: 'enum_with_selected_value.EnumWithSelectedValue_RollerBearingProfileTypes.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_RollerBearingProfileTypes.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.RollerProfile = value

    @property
    def inner_race_profile_set(self) -> '_1913.ProfileSet':
        """ProfileSet: 'InnerRaceProfileSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRaceProfileSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_race_profile_set(self) -> '_1913.ProfileSet':
        """ProfileSet: 'OuterRaceProfileSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRaceProfileSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def roller_profile_set(self) -> '_1913.ProfileSet':
        """ProfileSet: 'RollerProfileSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollerProfileSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_race_and_roller_profiles(self) -> 'List[_1923.RollerRaceProfilePoint]':
        """List[RollerRaceProfilePoint]: 'InnerRaceAndRollerProfiles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRaceAndRollerProfiles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def inner_race_and_roller_profiles_for_first_row(self) -> 'List[_1923.RollerRaceProfilePoint]':
        """List[RollerRaceProfilePoint]: 'InnerRaceAndRollerProfilesForFirstRow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRaceAndRollerProfilesForFirstRow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def inner_race_and_roller_profiles_for_second_row(self) -> 'List[_1923.RollerRaceProfilePoint]':
        """List[RollerRaceProfilePoint]: 'InnerRaceAndRollerProfilesForSecondRow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRaceAndRollerProfilesForSecondRow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def outer_race_and_roller_profiles(self) -> 'List[_1923.RollerRaceProfilePoint]':
        """List[RollerRaceProfilePoint]: 'OuterRaceAndRollerProfiles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRaceAndRollerProfiles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def outer_race_and_roller_profiles_for_first_row(self) -> 'List[_1923.RollerRaceProfilePoint]':
        """List[RollerRaceProfilePoint]: 'OuterRaceAndRollerProfilesForFirstRow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRaceAndRollerProfilesForFirstRow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def outer_race_and_roller_profiles_for_second_row(self) -> 'List[_1923.RollerRaceProfilePoint]':
        """List[RollerRaceProfilePoint]: 'OuterRaceAndRollerProfilesForSecondRow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRaceAndRollerProfilesForSecondRow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RollerBearing._Cast_RollerBearing':
        return self._Cast_RollerBearing(self)
