"""_263.py

LubricationDetail
"""
from mastapy.materials import (
    _235, _258, _248, _253,
    _256, _257, _259, _261,
    _262, _240, _260, _272,
    _273
)
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.math_utility import _1523
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility.databases import _1816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LUBRICATION_DETAIL = python_net_import('SMT.MastaAPI.Materials', 'LubricationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('LubricationDetail',)


class LubricationDetail(_1816.NamedDatabaseItem):
    """LubricationDetail

    This is a mastapy class.
    """

    TYPE = _LUBRICATION_DETAIL

    class _Cast_LubricationDetail:
        """Special nested class for casting LubricationDetail to subclasses."""

        def __init__(self, parent: 'LubricationDetail'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def lubrication_detail(self) -> 'LubricationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LubricationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def agma925a03_lubricant_type(self) -> '_235.AGMALubricantType':
        """AGMALubricantType: 'AGMA925A03LubricantType' is the original name of this property."""

        temp = self.wrapped.AGMA925A03LubricantType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _235.AGMALubricantType)
        return constructor.new_from_mastapy_type(_235.AGMALubricantType)(value) if value is not None else None

    @agma925a03_lubricant_type.setter
    def agma925a03_lubricant_type(self, value: '_235.AGMALubricantType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _235.AGMALubricantType.type_())
        self.wrapped.AGMA925A03LubricantType = value

    @property
    def air_flow_velocity(self) -> 'float':
        """float: 'AirFlowVelocity' is the original name of this property."""

        temp = self.wrapped.AirFlowVelocity

        if temp is None:
            return 0.0

        return temp

    @air_flow_velocity.setter
    def air_flow_velocity(self, value: 'float'):
        self.wrapped.AirFlowVelocity = float(value) if value else 0.0

    @property
    def delivery(self) -> '_258.LubricantDelivery':
        """LubricantDelivery: 'Delivery' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Delivery

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _258.LubricantDelivery)
        return constructor.new_from_mastapy_type(_258.LubricantDelivery)(value) if value is not None else None

    @property
    def density(self) -> 'float':
        """float: 'Density' is the original name of this property."""

        temp = self.wrapped.Density

        if temp is None:
            return 0.0

        return temp

    @density.setter
    def density(self, value: 'float'):
        self.wrapped.Density = float(value) if value else 0.0

    @property
    def density_specification_method(self) -> '_248.DensitySpecificationMethod':
        """DensitySpecificationMethod: 'DensitySpecificationMethod' is the original name of this property."""

        temp = self.wrapped.DensitySpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _248.DensitySpecificationMethod)
        return constructor.new_from_mastapy_type(_248.DensitySpecificationMethod)(value) if value is not None else None

    @density_specification_method.setter
    def density_specification_method(self, value: '_248.DensitySpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _248.DensitySpecificationMethod.type_())
        self.wrapped.DensitySpecificationMethod = value

    @property
    def density_vs_temperature(self) -> '_1523.Vector2DListAccessor':
        """Vector2DListAccessor: 'DensityVsTemperature' is the original name of this property."""

        temp = self.wrapped.DensityVsTemperature

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @density_vs_temperature.setter
    def density_vs_temperature(self, value: '_1523.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.DensityVsTemperature = value

    @property
    def dynamic_viscosity_at_38c(self) -> 'float':
        """float: 'DynamicViscosityAt38C' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicViscosityAt38C

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_viscosity_of_the_lubricant_at_100_degrees_c(self) -> 'float':
        """float: 'DynamicViscosityOfTheLubricantAt100DegreesC' is the original name of this property."""

        temp = self.wrapped.DynamicViscosityOfTheLubricantAt100DegreesC

        if temp is None:
            return 0.0

        return temp

    @dynamic_viscosity_of_the_lubricant_at_100_degrees_c.setter
    def dynamic_viscosity_of_the_lubricant_at_100_degrees_c(self, value: 'float'):
        self.wrapped.DynamicViscosityOfTheLubricantAt100DegreesC = float(value) if value else 0.0

    @property
    def dynamic_viscosity_of_the_lubricant_at_40_degrees_c(self) -> 'float':
        """float: 'DynamicViscosityOfTheLubricantAt40DegreesC' is the original name of this property."""

        temp = self.wrapped.DynamicViscosityOfTheLubricantAt40DegreesC

        if temp is None:
            return 0.0

        return temp

    @dynamic_viscosity_of_the_lubricant_at_40_degrees_c.setter
    def dynamic_viscosity_of_the_lubricant_at_40_degrees_c(self, value: 'float'):
        self.wrapped.DynamicViscosityOfTheLubricantAt40DegreesC = float(value) if value else 0.0

    @property
    def ep_additives_proven_with_severe_contamination(self) -> 'bool':
        """bool: 'EPAdditivesProvenWithSevereContamination' is the original name of this property."""

        temp = self.wrapped.EPAdditivesProvenWithSevereContamination

        if temp is None:
            return False

        return temp

    @ep_additives_proven_with_severe_contamination.setter
    def ep_additives_proven_with_severe_contamination(self, value: 'bool'):
        self.wrapped.EPAdditivesProvenWithSevereContamination = bool(value) if value else False

    @property
    def ep_and_aw_additives_present(self) -> 'bool':
        """bool: 'EPAndAWAdditivesPresent' is the original name of this property."""

        temp = self.wrapped.EPAndAWAdditivesPresent

        if temp is None:
            return False

        return temp

    @ep_and_aw_additives_present.setter
    def ep_and_aw_additives_present(self, value: 'bool'):
        self.wrapped.EPAndAWAdditivesPresent = bool(value) if value else False

    @property
    def factor_for_newly_greased_bearings(self) -> 'float':
        """float: 'FactorForNewlyGreasedBearings' is the original name of this property."""

        temp = self.wrapped.FactorForNewlyGreasedBearings

        if temp is None:
            return 0.0

        return temp

    @factor_for_newly_greased_bearings.setter
    def factor_for_newly_greased_bearings(self, value: 'float'):
        self.wrapped.FactorForNewlyGreasedBearings = float(value) if value else 0.0

    @property
    def feed_flow_rate(self) -> 'float':
        """float: 'FeedFlowRate' is the original name of this property."""

        temp = self.wrapped.FeedFlowRate

        if temp is None:
            return 0.0

        return temp

    @feed_flow_rate.setter
    def feed_flow_rate(self, value: 'float'):
        self.wrapped.FeedFlowRate = float(value) if value else 0.0

    @property
    def feed_pressure(self) -> 'float':
        """float: 'FeedPressure' is the original name of this property."""

        temp = self.wrapped.FeedPressure

        if temp is None:
            return 0.0

        return temp

    @feed_pressure.setter
    def feed_pressure(self, value: 'float'):
        self.wrapped.FeedPressure = float(value) if value else 0.0

    @property
    def grease_contamination_level(self) -> '_253.GreaseContaminationOptions':
        """GreaseContaminationOptions: 'GreaseContaminationLevel' is the original name of this property."""

        temp = self.wrapped.GreaseContaminationLevel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _253.GreaseContaminationOptions)
        return constructor.new_from_mastapy_type(_253.GreaseContaminationOptions)(value) if value is not None else None

    @grease_contamination_level.setter
    def grease_contamination_level(self, value: '_253.GreaseContaminationOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _253.GreaseContaminationOptions.type_())
        self.wrapped.GreaseContaminationLevel = value

    @property
    def heat_transfer_coefficient(self) -> 'float':
        """float: 'HeatTransferCoefficient' is the original name of this property."""

        temp = self.wrapped.HeatTransferCoefficient

        if temp is None:
            return 0.0

        return temp

    @heat_transfer_coefficient.setter
    def heat_transfer_coefficient(self, value: 'float'):
        self.wrapped.HeatTransferCoefficient = float(value) if value else 0.0

    @property
    def iso_lubricant_type(self) -> '_256.ISOLubricantType':
        """ISOLubricantType: 'ISOLubricantType' is the original name of this property."""

        temp = self.wrapped.ISOLubricantType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _256.ISOLubricantType)
        return constructor.new_from_mastapy_type(_256.ISOLubricantType)(value) if value is not None else None

    @iso_lubricant_type.setter
    def iso_lubricant_type(self, value: '_256.ISOLubricantType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _256.ISOLubricantType.type_())
        self.wrapped.ISOLubricantType = value

    @property
    def kinematic_viscosity_at_38c(self) -> 'float':
        """float: 'KinematicViscosityAt38C' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KinematicViscosityAt38C

        if temp is None:
            return 0.0

        return temp

    @property
    def kinematic_viscosity_of_the_lubricant_at_100_degrees_c(self) -> 'float':
        """float: 'KinematicViscosityOfTheLubricantAt100DegreesC' is the original name of this property."""

        temp = self.wrapped.KinematicViscosityOfTheLubricantAt100DegreesC

        if temp is None:
            return 0.0

        return temp

    @kinematic_viscosity_of_the_lubricant_at_100_degrees_c.setter
    def kinematic_viscosity_of_the_lubricant_at_100_degrees_c(self, value: 'float'):
        self.wrapped.KinematicViscosityOfTheLubricantAt100DegreesC = float(value) if value else 0.0

    @property
    def kinematic_viscosity_of_the_lubricant_at_40_degrees_c(self) -> 'float':
        """float: 'KinematicViscosityOfTheLubricantAt40DegreesC' is the original name of this property."""

        temp = self.wrapped.KinematicViscosityOfTheLubricantAt40DegreesC

        if temp is None:
            return 0.0

        return temp

    @kinematic_viscosity_of_the_lubricant_at_40_degrees_c.setter
    def kinematic_viscosity_of_the_lubricant_at_40_degrees_c(self, value: 'float'):
        self.wrapped.KinematicViscosityOfTheLubricantAt40DegreesC = float(value) if value else 0.0

    @property
    def lubricant_definition(self) -> 'enum_with_selected_value.EnumWithSelectedValue_LubricantDefinition':
        """enum_with_selected_value.EnumWithSelectedValue_LubricantDefinition: 'LubricantDefinition' is the original name of this property."""

        temp = self.wrapped.LubricantDefinition

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_LubricantDefinition.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @lubricant_definition.setter
    def lubricant_definition(self, value: 'enum_with_selected_value.EnumWithSelectedValue_LubricantDefinition.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_LubricantDefinition.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LubricantDefinition = value

    @property
    def lubricant_grade_agma(self) -> '_259.LubricantViscosityClassAGMA':
        """LubricantViscosityClassAGMA: 'LubricantGradeAGMA' is the original name of this property."""

        temp = self.wrapped.LubricantGradeAGMA

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _259.LubricantViscosityClassAGMA)
        return constructor.new_from_mastapy_type(_259.LubricantViscosityClassAGMA)(value) if value is not None else None

    @lubricant_grade_agma.setter
    def lubricant_grade_agma(self, value: '_259.LubricantViscosityClassAGMA'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _259.LubricantViscosityClassAGMA.type_())
        self.wrapped.LubricantGradeAGMA = value

    @property
    def lubricant_grade_iso(self) -> 'enum_with_selected_value.EnumWithSelectedValue_LubricantViscosityClassISO':
        """enum_with_selected_value.EnumWithSelectedValue_LubricantViscosityClassISO: 'LubricantGradeISO' is the original name of this property."""

        temp = self.wrapped.LubricantGradeISO

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_LubricantViscosityClassISO.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @lubricant_grade_iso.setter
    def lubricant_grade_iso(self, value: 'enum_with_selected_value.EnumWithSelectedValue_LubricantViscosityClassISO.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_LubricantViscosityClassISO.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LubricantGradeISO = value

    @property
    def lubricant_grade_sae(self) -> '_262.LubricantViscosityClassSAE':
        """LubricantViscosityClassSAE: 'LubricantGradeSAE' is the original name of this property."""

        temp = self.wrapped.LubricantGradeSAE

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _262.LubricantViscosityClassSAE)
        return constructor.new_from_mastapy_type(_262.LubricantViscosityClassSAE)(value) if value is not None else None

    @lubricant_grade_sae.setter
    def lubricant_grade_sae(self, value: '_262.LubricantViscosityClassSAE'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _262.LubricantViscosityClassSAE.type_())
        self.wrapped.LubricantGradeSAE = value

    @property
    def lubricant_shear_modulus(self) -> 'float':
        """float: 'LubricantShearModulus' is the original name of this property."""

        temp = self.wrapped.LubricantShearModulus

        if temp is None:
            return 0.0

        return temp

    @lubricant_shear_modulus.setter
    def lubricant_shear_modulus(self, value: 'float'):
        self.wrapped.LubricantShearModulus = float(value) if value else 0.0

    @property
    def lubricant_type_ampersand_supply(self) -> '_240.BearingLubricationCondition':
        """BearingLubricationCondition: 'LubricantTypeAmpersandSupply' is the original name of this property."""

        temp = self.wrapped.LubricantTypeAmpersandSupply

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _240.BearingLubricationCondition)
        return constructor.new_from_mastapy_type(_240.BearingLubricationCondition)(value) if value is not None else None

    @lubricant_type_ampersand_supply.setter
    def lubricant_type_ampersand_supply(self, value: '_240.BearingLubricationCondition'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _240.BearingLubricationCondition.type_())
        self.wrapped.LubricantTypeAmpersandSupply = value

    @property
    def lubricant_viscosity_classification(self) -> '_260.LubricantViscosityClassification':
        """LubricantViscosityClassification: 'LubricantViscosityClassification' is the original name of this property."""

        temp = self.wrapped.LubricantViscosityClassification

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _260.LubricantViscosityClassification)
        return constructor.new_from_mastapy_type(_260.LubricantViscosityClassification)(value) if value is not None else None

    @lubricant_viscosity_classification.setter
    def lubricant_viscosity_classification(self, value: '_260.LubricantViscosityClassification'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _260.LubricantViscosityClassification.type_())
        self.wrapped.LubricantViscosityClassification = value

    @property
    def mass(self) -> 'float':
        """float: 'Mass' is the original name of this property."""

        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return temp

    @mass.setter
    def mass(self, value: 'float'):
        self.wrapped.Mass = float(value) if value else 0.0

    @property
    def micropitting_failure_load_stage(self) -> 'int':
        """int: 'MicropittingFailureLoadStage' is the original name of this property."""

        temp = self.wrapped.MicropittingFailureLoadStage

        if temp is None:
            return 0

        return temp

    @micropitting_failure_load_stage.setter
    def micropitting_failure_load_stage(self, value: 'int'):
        self.wrapped.MicropittingFailureLoadStage = int(value) if value else 0

    @property
    def micropitting_failure_load_stage_test_temperature(self) -> 'float':
        """float: 'MicropittingFailureLoadStageTestTemperature' is the original name of this property."""

        temp = self.wrapped.MicropittingFailureLoadStageTestTemperature

        if temp is None:
            return 0.0

        return temp

    @micropitting_failure_load_stage_test_temperature.setter
    def micropitting_failure_load_stage_test_temperature(self, value: 'float'):
        self.wrapped.MicropittingFailureLoadStageTestTemperature = float(value) if value else 0.0

    @property
    def oil_filtration_and_contamination(self) -> '_272.OilFiltrationOptions':
        """OilFiltrationOptions: 'OilFiltrationAndContamination' is the original name of this property."""

        temp = self.wrapped.OilFiltrationAndContamination

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _272.OilFiltrationOptions)
        return constructor.new_from_mastapy_type(_272.OilFiltrationOptions)(value) if value is not None else None

    @oil_filtration_and_contamination.setter
    def oil_filtration_and_contamination(self, value: '_272.OilFiltrationOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _272.OilFiltrationOptions.type_())
        self.wrapped.OilFiltrationAndContamination = value

    @property
    def oil_to_air_heat_transfer_area(self) -> 'float':
        """float: 'OilToAirHeatTransferArea' is the original name of this property."""

        temp = self.wrapped.OilToAirHeatTransferArea

        if temp is None:
            return 0.0

        return temp

    @oil_to_air_heat_transfer_area.setter
    def oil_to_air_heat_transfer_area(self, value: 'float'):
        self.wrapped.OilToAirHeatTransferArea = float(value) if value else 0.0

    @property
    def pressure_viscosity_coefficient(self) -> 'float':
        """float: 'PressureViscosityCoefficient' is the original name of this property."""

        temp = self.wrapped.PressureViscosityCoefficient

        if temp is None:
            return 0.0

        return temp

    @pressure_viscosity_coefficient.setter
    def pressure_viscosity_coefficient(self, value: 'float'):
        self.wrapped.PressureViscosityCoefficient = float(value) if value else 0.0

    @property
    def pressure_viscosity_coefficient_method(self) -> '_273.PressureViscosityCoefficientMethod':
        """PressureViscosityCoefficientMethod: 'PressureViscosityCoefficientMethod' is the original name of this property."""

        temp = self.wrapped.PressureViscosityCoefficientMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _273.PressureViscosityCoefficientMethod)
        return constructor.new_from_mastapy_type(_273.PressureViscosityCoefficientMethod)(value) if value is not None else None

    @pressure_viscosity_coefficient_method.setter
    def pressure_viscosity_coefficient_method(self, value: '_273.PressureViscosityCoefficientMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _273.PressureViscosityCoefficientMethod.type_())
        self.wrapped.PressureViscosityCoefficientMethod = value

    @property
    def scuffing_failure_load_stage(self) -> 'int':
        """int: 'ScuffingFailureLoadStage' is the original name of this property."""

        temp = self.wrapped.ScuffingFailureLoadStage

        if temp is None:
            return 0

        return temp

    @scuffing_failure_load_stage.setter
    def scuffing_failure_load_stage(self, value: 'int'):
        self.wrapped.ScuffingFailureLoadStage = int(value) if value else 0

    @property
    def specific_heat_capacity(self) -> 'float':
        """float: 'SpecificHeatCapacity' is the original name of this property."""

        temp = self.wrapped.SpecificHeatCapacity

        if temp is None:
            return 0.0

        return temp

    @specific_heat_capacity.setter
    def specific_heat_capacity(self, value: 'float'):
        self.wrapped.SpecificHeatCapacity = float(value) if value else 0.0

    @property
    def specified_parameter_k(self) -> 'float':
        """float: 'SpecifiedParameterK' is the original name of this property."""

        temp = self.wrapped.SpecifiedParameterK

        if temp is None:
            return 0.0

        return temp

    @specified_parameter_k.setter
    def specified_parameter_k(self, value: 'float'):
        self.wrapped.SpecifiedParameterK = float(value) if value else 0.0

    @property
    def specified_parameter_s(self) -> 'float':
        """float: 'SpecifiedParameterS' is the original name of this property."""

        temp = self.wrapped.SpecifiedParameterS

        if temp is None:
            return 0.0

        return temp

    @specified_parameter_s.setter
    def specified_parameter_s(self, value: 'float'):
        self.wrapped.SpecifiedParameterS = float(value) if value else 0.0

    @property
    def specify_heat_transfer_coefficient(self) -> 'bool':
        """bool: 'SpecifyHeatTransferCoefficient' is the original name of this property."""

        temp = self.wrapped.SpecifyHeatTransferCoefficient

        if temp is None:
            return False

        return temp

    @specify_heat_transfer_coefficient.setter
    def specify_heat_transfer_coefficient(self, value: 'bool'):
        self.wrapped.SpecifyHeatTransferCoefficient = bool(value) if value else False

    @property
    def system_includes_oil_pump(self) -> 'bool':
        """bool: 'SystemIncludesOilPump' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemIncludesOilPump

        if temp is None:
            return False

        return temp

    @property
    def temperature_at_which_density_is_specified(self) -> 'float':
        """float: 'TemperatureAtWhichDensityIsSpecified' is the original name of this property."""

        temp = self.wrapped.TemperatureAtWhichDensityIsSpecified

        if temp is None:
            return 0.0

        return temp

    @temperature_at_which_density_is_specified.setter
    def temperature_at_which_density_is_specified(self, value: 'float'):
        self.wrapped.TemperatureAtWhichDensityIsSpecified = float(value) if value else 0.0

    @property
    def temperature_at_which_pressure_viscosity_coefficient_is_specified(self) -> 'float':
        """float: 'TemperatureAtWhichPressureViscosityCoefficientIsSpecified' is the original name of this property."""

        temp = self.wrapped.TemperatureAtWhichPressureViscosityCoefficientIsSpecified

        if temp is None:
            return 0.0

        return temp

    @temperature_at_which_pressure_viscosity_coefficient_is_specified.setter
    def temperature_at_which_pressure_viscosity_coefficient_is_specified(self, value: 'float'):
        self.wrapped.TemperatureAtWhichPressureViscosityCoefficientIsSpecified = float(value) if value else 0.0

    @property
    def thermal_conductivity(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ThermalConductivity' is the original name of this property."""

        temp = self.wrapped.ThermalConductivity

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @thermal_conductivity.setter
    def thermal_conductivity(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ThermalConductivity = value

    @property
    def use_user_specified_contamination_factor(self) -> 'bool':
        """bool: 'UseUserSpecifiedContaminationFactor' is the original name of this property."""

        temp = self.wrapped.UseUserSpecifiedContaminationFactor

        if temp is None:
            return False

        return temp

    @use_user_specified_contamination_factor.setter
    def use_user_specified_contamination_factor(self, value: 'bool'):
        self.wrapped.UseUserSpecifiedContaminationFactor = bool(value) if value else False

    @property
    def user_specified_contamination_factor(self) -> 'float':
        """float: 'UserSpecifiedContaminationFactor' is the original name of this property."""

        temp = self.wrapped.UserSpecifiedContaminationFactor

        if temp is None:
            return 0.0

        return temp

    @user_specified_contamination_factor.setter
    def user_specified_contamination_factor(self, value: 'float'):
        self.wrapped.UserSpecifiedContaminationFactor = float(value) if value else 0.0

    @property
    def volume(self) -> 'float':
        """float: 'Volume' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Volume

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LubricationDetail._Cast_LubricationDetail':
        return self._Cast_LubricationDetail(self)
