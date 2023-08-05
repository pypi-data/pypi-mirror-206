"""_1403.py

SplineJointDesign
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.detailed_rigid_connectors.splines import (
    _1382, _1394, _1393, _1401,
    _1405, _1397, _1402
)
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.detailed_rigid_connectors import _1375
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPLINE_JOINT_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'SplineJointDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('SplineJointDesign',)


class SplineJointDesign(_1375.DetailedRigidConnectorDesign):
    """SplineJointDesign

    This is a mastapy class.
    """

    TYPE = _SPLINE_JOINT_DESIGN

    class _Cast_SplineJointDesign:
        """Special nested class for casting SplineJointDesign to subclasses."""

        def __init__(self, parent: 'SplineJointDesign'):
            self._parent = parent

        @property
        def detailed_rigid_connector_design(self):
            return self._parent._cast(_1375.DetailedRigidConnectorDesign)

        @property
        def custom_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1378
            
            return self._parent._cast(_1378.CustomSplineJointDesign)

        @property
        def din5480_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1381
            
            return self._parent._cast(_1381.DIN5480SplineJointDesign)

        @property
        def gbt3478_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1385
            
            return self._parent._cast(_1385.GBT3478SplineJointDesign)

        @property
        def iso4156_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1388
            
            return self._parent._cast(_1388.ISO4156SplineJointDesign)

        @property
        def jisb1603_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1389
            
            return self._parent._cast(_1389.JISB1603SplineJointDesign)

        @property
        def sae_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1396
            
            return self._parent._cast(_1396.SAESplineJointDesign)

        @property
        def standard_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1408
            
            return self._parent._cast(_1408.StandardSplineJointDesign)

        @property
        def spline_joint_design(self) -> 'SplineJointDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SplineJointDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_diameter(self) -> 'float':
        """float: 'BaseDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def base_pitch(self) -> 'float':
        """float: 'BasePitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def base_radius(self) -> 'float':
        """float: 'BaseRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_space_width(self) -> 'float':
        """float: 'BasicSpaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_tooth_thickness(self) -> 'float':
        """float: 'BasicToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicToothThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def before_running_in(self) -> 'bool':
        """bool: 'BeforeRunningIn' is the original name of this property."""

        temp = self.wrapped.BeforeRunningIn

        if temp is None:
            return False

        return temp

    @before_running_in.setter
    def before_running_in(self, value: 'bool'):
        self.wrapped.BeforeRunningIn = bool(value) if value else False

    @property
    def circular_pitch(self) -> 'float':
        """float: 'CircularPitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CircularPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def designation(self) -> 'str':
        """str: 'Designation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Designation

        if temp is None:
            return ''

        return temp

    @property
    def diametral_pitch(self) -> 'float':
        """float: 'DiametralPitch' is the original name of this property."""

        temp = self.wrapped.DiametralPitch

        if temp is None:
            return 0.0

        return temp

    @diametral_pitch.setter
    def diametral_pitch(self, value: 'float'):
        self.wrapped.DiametralPitch = float(value) if value else 0.0

    @property
    def dudley_maximum_effective_length(self) -> 'float':
        """float: 'DudleyMaximumEffectiveLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DudleyMaximumEffectiveLength

        if temp is None:
            return 0.0

        return temp

    @property
    def dudley_maximum_effective_length_option(self) -> 'enum_with_selected_value.EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption':
        """enum_with_selected_value.EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption: 'DudleyMaximumEffectiveLengthOption' is the original name of this property."""

        temp = self.wrapped.DudleyMaximumEffectiveLengthOption

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @dudley_maximum_effective_length_option.setter
    def dudley_maximum_effective_length_option(self, value: 'enum_with_selected_value.EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DudleyMaximumEffectiveLengthOption = value

    @property
    def fatigue_life_factor_type(self) -> '_1394.SAEFatigueLifeFactorTypes':
        """SAEFatigueLifeFactorTypes: 'FatigueLifeFactorType' is the original name of this property."""

        temp = self.wrapped.FatigueLifeFactorType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1394.SAEFatigueLifeFactorTypes)
        return constructor.new_from_mastapy_type(_1394.SAEFatigueLifeFactorTypes)(value) if value is not None else None

    @fatigue_life_factor_type.setter
    def fatigue_life_factor_type(self, value: '_1394.SAEFatigueLifeFactorTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1394.SAEFatigueLifeFactorTypes.type_())
        self.wrapped.FatigueLifeFactorType = value

    @property
    def minimum_effective_clearance(self) -> 'float':
        """float: 'MinimumEffectiveClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumEffectiveClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def module(self) -> 'float':
        """float: 'Module' is the original name of this property."""

        temp = self.wrapped.Module

        if temp is None:
            return 0.0

        return temp

    @module.setter
    def module(self, value: 'float'):
        self.wrapped.Module = float(value) if value else 0.0

    @property
    def number_of_teeth(self) -> 'int':
        """int: 'NumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @number_of_teeth.setter
    def number_of_teeth(self, value: 'int'):
        self.wrapped.NumberOfTeeth = int(value) if value else 0

    @property
    def number_of_teeth_in_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NumberOfTeethInContact' is the original name of this property."""

        temp = self.wrapped.NumberOfTeethInContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @number_of_teeth_in_contact.setter
    def number_of_teeth_in_contact(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NumberOfTeethInContact = value

    @property
    def pitch_diameter(self) -> 'float':
        """float: 'PitchDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def pressure_angle(self) -> 'float':
        """float: 'PressureAngle' is the original name of this property."""

        temp = self.wrapped.PressureAngle

        if temp is None:
            return 0.0

        return temp

    @pressure_angle.setter
    def pressure_angle(self, value: 'float'):
        self.wrapped.PressureAngle = float(value) if value else 0.0

    @property
    def root_type(self) -> '_1393.RootTypes':
        """RootTypes: 'RootType' is the original name of this property."""

        temp = self.wrapped.RootType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1393.RootTypes)
        return constructor.new_from_mastapy_type(_1393.RootTypes)(value) if value is not None else None

    @root_type.setter
    def root_type(self, value: '_1393.RootTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1393.RootTypes.type_())
        self.wrapped.RootType = value

    @property
    def spline_fixture_type(self) -> '_1401.SplineFixtureTypes':
        """SplineFixtureTypes: 'SplineFixtureType' is the original name of this property."""

        temp = self.wrapped.SplineFixtureType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1401.SplineFixtureTypes)
        return constructor.new_from_mastapy_type(_1401.SplineFixtureTypes)(value) if value is not None else None

    @spline_fixture_type.setter
    def spline_fixture_type(self, value: '_1401.SplineFixtureTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1401.SplineFixtureTypes.type_())
        self.wrapped.SplineFixtureType = value

    @property
    def spline_rating_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_SplineRatingTypes':
        """enum_with_selected_value.EnumWithSelectedValue_SplineRatingTypes: 'SplineRatingType' is the original name of this property."""

        temp = self.wrapped.SplineRatingType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_SplineRatingTypes.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @spline_rating_type.setter
    def spline_rating_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_SplineRatingTypes.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_SplineRatingTypes.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SplineRatingType = value

    @property
    def torque_cycles(self) -> '_1397.SAETorqueCycles':
        """SAETorqueCycles: 'TorqueCycles' is the original name of this property."""

        temp = self.wrapped.TorqueCycles

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1397.SAETorqueCycles)
        return constructor.new_from_mastapy_type(_1397.SAETorqueCycles)(value) if value is not None else None

    @torque_cycles.setter
    def torque_cycles(self, value: '_1397.SAETorqueCycles'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1397.SAETorqueCycles.type_())
        self.wrapped.TorqueCycles = value

    @property
    def total_crowning(self) -> 'float':
        """float: 'TotalCrowning' is the original name of this property."""

        temp = self.wrapped.TotalCrowning

        if temp is None:
            return 0.0

        return temp

    @total_crowning.setter
    def total_crowning(self, value: 'float'):
        self.wrapped.TotalCrowning = float(value) if value else 0.0

    @property
    def use_sae_stress_concentration_factor(self) -> 'bool':
        """bool: 'UseSAEStressConcentrationFactor' is the original name of this property."""

        temp = self.wrapped.UseSAEStressConcentrationFactor

        if temp is None:
            return False

        return temp

    @use_sae_stress_concentration_factor.setter
    def use_sae_stress_concentration_factor(self, value: 'bool'):
        self.wrapped.UseSAEStressConcentrationFactor = bool(value) if value else False

    @property
    def use_user_input_allowable_stresses(self) -> 'bool':
        """bool: 'UseUserInputAllowableStresses' is the original name of this property."""

        temp = self.wrapped.UseUserInputAllowableStresses

        if temp is None:
            return False

        return temp

    @use_user_input_allowable_stresses.setter
    def use_user_input_allowable_stresses(self, value: 'bool'):
        self.wrapped.UseUserInputAllowableStresses = bool(value) if value else False

    @property
    def user_specified_external_teeth_stress_concentration_factor(self) -> 'float':
        """float: 'UserSpecifiedExternalTeethStressConcentrationFactor' is the original name of this property."""

        temp = self.wrapped.UserSpecifiedExternalTeethStressConcentrationFactor

        if temp is None:
            return 0.0

        return temp

    @user_specified_external_teeth_stress_concentration_factor.setter
    def user_specified_external_teeth_stress_concentration_factor(self, value: 'float'):
        self.wrapped.UserSpecifiedExternalTeethStressConcentrationFactor = float(value) if value else 0.0

    @property
    def user_specified_internal_teeth_stress_concentration_factor(self) -> 'float':
        """float: 'UserSpecifiedInternalTeethStressConcentrationFactor' is the original name of this property."""

        temp = self.wrapped.UserSpecifiedInternalTeethStressConcentrationFactor

        if temp is None:
            return 0.0

        return temp

    @user_specified_internal_teeth_stress_concentration_factor.setter
    def user_specified_internal_teeth_stress_concentration_factor(self, value: 'float'):
        self.wrapped.UserSpecifiedInternalTeethStressConcentrationFactor = float(value) if value else 0.0

    @property
    def wall_thickness(self) -> 'float':
        """float: 'WallThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WallThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def with_crown(self) -> 'bool':
        """bool: 'WithCrown' is the original name of this property."""

        temp = self.wrapped.WithCrown

        if temp is None:
            return False

        return temp

    @with_crown.setter
    def with_crown(self, value: 'bool'):
        self.wrapped.WithCrown = bool(value) if value else False

    @property
    def external_half(self) -> '_1402.SplineHalfDesign':
        """SplineHalfDesign: 'ExternalHalf' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExternalHalf

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def internal_half(self) -> '_1402.SplineHalfDesign':
        """SplineHalfDesign: 'InternalHalf' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InternalHalf

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SplineJointDesign._Cast_SplineJointDesign':
        return self._Cast_SplineJointDesign(self)
