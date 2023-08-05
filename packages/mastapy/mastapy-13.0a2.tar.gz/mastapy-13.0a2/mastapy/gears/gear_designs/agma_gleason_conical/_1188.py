"""_1188.py

AGMAGleasonConicalGearMeshDesign
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.rating.iso_10300 import (
    _417, _430, _432, _433
)
from mastapy.gears.gear_designs.conical import _1163, _1149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.AGMAGleasonConical', 'AGMAGleasonConicalGearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearMeshDesign',)


class AGMAGleasonConicalGearMeshDesign(_1149.ConicalGearMeshDesign):
    """AGMAGleasonConicalGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_DESIGN

    class _Cast_AGMAGleasonConicalGearMeshDesign:
        """Special nested class for casting AGMAGleasonConicalGearMeshDesign to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearMeshDesign'):
            self._parent = parent

        @property
        def conical_gear_mesh_design(self):
            return self._parent._cast(_1149.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(self):
            from mastapy.gears.gear_designs import _944
            
            return self._parent._cast(_944.GearMeshDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def zerol_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.zerol_bevel import _948
            
            return self._parent._cast(_948.ZerolBevelGearMeshDesign)

        @property
        def straight_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.straight_bevel import _957
            
            return self._parent._cast(_957.StraightBevelGearMeshDesign)

        @property
        def straight_bevel_diff_gear_mesh_design(self):
            from mastapy.gears.gear_designs.straight_bevel_diff import _961
            
            return self._parent._cast(_961.StraightBevelDiffGearMeshDesign)

        @property
        def spiral_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.spiral_bevel import _965
            
            return self._parent._cast(_965.SpiralBevelGearMeshDesign)

        @property
        def hypoid_gear_mesh_design(self):
            from mastapy.gears.gear_designs.hypoid import _981
            
            return self._parent._cast(_981.HypoidGearMeshDesign)

        @property
        def bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.bevel import _1175
            
            return self._parent._cast(_1175.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(self) -> 'AGMAGleasonConicalGearMeshDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowned(self) -> 'bool':
        """bool: 'Crowned' is the original name of this property."""

        temp = self.wrapped.Crowned

        if temp is None:
            return False

        return temp

    @crowned.setter
    def crowned(self, value: 'bool'):
        self.wrapped.Crowned = bool(value) if value else False

    @property
    def crowning_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CrowningFactor' is the original name of this property."""

        temp = self.wrapped.CrowningFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @crowning_factor.setter
    def crowning_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CrowningFactor = value

    @property
    def dynamic_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DynamicFactor' is the original name of this property."""

        temp = self.wrapped.DynamicFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @dynamic_factor.setter
    def dynamic_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DynamicFactor = value

    @property
    def hardness_ratio_factor(self) -> 'float':
        """float: 'HardnessRatioFactor' is the original name of this property."""

        temp = self.wrapped.HardnessRatioFactor

        if temp is None:
            return 0.0

        return temp

    @hardness_ratio_factor.setter
    def hardness_ratio_factor(self, value: 'float'):
        self.wrapped.HardnessRatioFactor = float(value) if value else 0.0

    @property
    def iso10300_gear_set_finishing_methods(self) -> '_417.Iso10300FinishingMethods':
        """Iso10300FinishingMethods: 'ISO10300GearSetFinishingMethods' is the original name of this property."""

        temp = self.wrapped.ISO10300GearSetFinishingMethods

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _417.Iso10300FinishingMethods)
        return constructor.new_from_mastapy_type(_417.Iso10300FinishingMethods)(value) if value is not None else None

    @iso10300_gear_set_finishing_methods.setter
    def iso10300_gear_set_finishing_methods(self, value: '_417.Iso10300FinishingMethods'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _417.Iso10300FinishingMethods.type_())
        self.wrapped.ISO10300GearSetFinishingMethods = value

    @property
    def load_distribution_factor(self) -> 'float':
        """float: 'LoadDistributionFactor' is the original name of this property."""

        temp = self.wrapped.LoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @load_distribution_factor.setter
    def load_distribution_factor(self, value: 'float'):
        self.wrapped.LoadDistributionFactor = float(value) if value else 0.0

    @property
    def load_distribution_factor_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_LoadDistributionFactorMethods':
        """enum_with_selected_value.EnumWithSelectedValue_LoadDistributionFactorMethods: 'LoadDistributionFactorMethod' is the original name of this property."""

        temp = self.wrapped.LoadDistributionFactorMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_LoadDistributionFactorMethods.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @load_distribution_factor_method.setter
    def load_distribution_factor_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_LoadDistributionFactorMethods.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_LoadDistributionFactorMethods.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LoadDistributionFactorMethod = value

    @property
    def mounting_conditions_of_pinion_and_wheel(self) -> '_430.MountingConditionsOfPinionAndWheel':
        """MountingConditionsOfPinionAndWheel: 'MountingConditionsOfPinionAndWheel' is the original name of this property."""

        temp = self.wrapped.MountingConditionsOfPinionAndWheel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _430.MountingConditionsOfPinionAndWheel)
        return constructor.new_from_mastapy_type(_430.MountingConditionsOfPinionAndWheel)(value) if value is not None else None

    @mounting_conditions_of_pinion_and_wheel.setter
    def mounting_conditions_of_pinion_and_wheel(self, value: '_430.MountingConditionsOfPinionAndWheel'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _430.MountingConditionsOfPinionAndWheel.type_())
        self.wrapped.MountingConditionsOfPinionAndWheel = value

    @property
    def net_face_width(self) -> 'float':
        """float: 'NetFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NetFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_face_width_offset(self) -> 'float':
        """float: 'PinionFaceWidthOffset' is the original name of this property."""

        temp = self.wrapped.PinionFaceWidthOffset

        if temp is None:
            return 0.0

        return temp

    @pinion_face_width_offset.setter
    def pinion_face_width_offset(self, value: 'float'):
        self.wrapped.PinionFaceWidthOffset = float(value) if value else 0.0

    @property
    def profile_crowning_setting(self) -> '_432.ProfileCrowningSetting':
        """ProfileCrowningSetting: 'ProfileCrowningSetting' is the original name of this property."""

        temp = self.wrapped.ProfileCrowningSetting

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _432.ProfileCrowningSetting)
        return constructor.new_from_mastapy_type(_432.ProfileCrowningSetting)(value) if value is not None else None

    @profile_crowning_setting.setter
    def profile_crowning_setting(self, value: '_432.ProfileCrowningSetting'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _432.ProfileCrowningSetting.type_())
        self.wrapped.ProfileCrowningSetting = value

    @property
    def size_factor_bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SizeFactorBending' is the original name of this property."""

        temp = self.wrapped.SizeFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @size_factor_bending.setter
    def size_factor_bending(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SizeFactorBending = value

    @property
    def size_factor_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SizeFactorContact' is the original name of this property."""

        temp = self.wrapped.SizeFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @size_factor_contact.setter
    def size_factor_contact(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SizeFactorContact = value

    @property
    def surface_condition_factor(self) -> 'float':
        """float: 'SurfaceConditionFactor' is the original name of this property."""

        temp = self.wrapped.SurfaceConditionFactor

        if temp is None:
            return 0.0

        return temp

    @surface_condition_factor.setter
    def surface_condition_factor(self, value: 'float'):
        self.wrapped.SurfaceConditionFactor = float(value) if value else 0.0

    @property
    def temperature_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TemperatureFactor' is the original name of this property."""

        temp = self.wrapped.TemperatureFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @temperature_factor.setter
    def temperature_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.TemperatureFactor = value

    @property
    def tooth_lengthwise_curvature_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ToothLengthwiseCurvatureFactor' is the original name of this property."""

        temp = self.wrapped.ToothLengthwiseCurvatureFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @tooth_lengthwise_curvature_factor.setter
    def tooth_lengthwise_curvature_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ToothLengthwiseCurvatureFactor = value

    @property
    def verification_of_contact_pattern(self) -> '_433.VerificationOfContactPattern':
        """VerificationOfContactPattern: 'VerificationOfContactPattern' is the original name of this property."""

        temp = self.wrapped.VerificationOfContactPattern

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _433.VerificationOfContactPattern)
        return constructor.new_from_mastapy_type(_433.VerificationOfContactPattern)(value) if value is not None else None

    @verification_of_contact_pattern.setter
    def verification_of_contact_pattern(self, value: '_433.VerificationOfContactPattern'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _433.VerificationOfContactPattern.type_())
        self.wrapped.VerificationOfContactPattern = value

    @property
    def wheel_effective_face_width_factor(self) -> 'float':
        """float: 'WheelEffectiveFaceWidthFactor' is the original name of this property."""

        temp = self.wrapped.WheelEffectiveFaceWidthFactor

        if temp is None:
            return 0.0

        return temp

    @wheel_effective_face_width_factor.setter
    def wheel_effective_face_width_factor(self, value: 'float'):
        self.wrapped.WheelEffectiveFaceWidthFactor = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign':
        return self._Cast_AGMAGleasonConicalGearMeshDesign(self)
