"""_4089.py

PartPowerFlow
"""
from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2448
from mastapy.system_model.analyses_and_results.power_flows import _4097
from mastapy.system_model.drawing import _2235
from mastapy.system_model.analyses_and_results.analysis_cases import _7510
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'PartPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('PartPowerFlow',)


class PartPowerFlow(_7510.PartStaticLoadAnalysisCase):
    """PartPowerFlow

    This is a mastapy class.
    """

    TYPE = _PART_POWER_FLOW

    class _Cast_PartPowerFlow:
        """Special nested class for casting PartPowerFlow to subclasses."""

        def __init__(self, parent: 'PartPowerFlow'):
            self._parent = parent

        @property
        def part_static_load_analysis_case(self):
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def abstract_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4009
            
            return self._parent._cast(_4009.AbstractAssemblyPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4010
            
            return self._parent._cast(_4010.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4011
            
            return self._parent._cast(_4011.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4014
            
            return self._parent._cast(_4014.AGMAGleasonConicalGearPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4015
            
            return self._parent._cast(_4015.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4016
            
            return self._parent._cast(_4016.AssemblyPowerFlow)

        @property
        def bearing_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4017
            
            return self._parent._cast(_4017.BearingPowerFlow)

        @property
        def belt_drive_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4019
            
            return self._parent._cast(_4019.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4021
            
            return self._parent._cast(_4021.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4022
            
            return self._parent._cast(_4022.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4023
            
            return self._parent._cast(_4023.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4024
            
            return self._parent._cast(_4024.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4026
            
            return self._parent._cast(_4026.BevelGearPowerFlow)

        @property
        def bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4027
            
            return self._parent._cast(_4027.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4028
            
            return self._parent._cast(_4028.BoltedJointPowerFlow)

        @property
        def bolt_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4029
            
            return self._parent._cast(_4029.BoltPowerFlow)

        @property
        def clutch_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4031
            
            return self._parent._cast(_4031.ClutchHalfPowerFlow)

        @property
        def clutch_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4032
            
            return self._parent._cast(_4032.ClutchPowerFlow)

        @property
        def component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4034
            
            return self._parent._cast(_4034.ComponentPowerFlow)

        @property
        def concept_coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4036
            
            return self._parent._cast(_4036.ConceptCouplingHalfPowerFlow)

        @property
        def concept_coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4037
            
            return self._parent._cast(_4037.ConceptCouplingPowerFlow)

        @property
        def concept_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4039
            
            return self._parent._cast(_4039.ConceptGearPowerFlow)

        @property
        def concept_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4040
            
            return self._parent._cast(_4040.ConceptGearSetPowerFlow)

        @property
        def conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4042
            
            return self._parent._cast(_4042.ConicalGearPowerFlow)

        @property
        def conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4043
            
            return self._parent._cast(_4043.ConicalGearSetPowerFlow)

        @property
        def connector_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4045
            
            return self._parent._cast(_4045.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4047
            
            return self._parent._cast(_4047.CouplingHalfPowerFlow)

        @property
        def coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4048
            
            return self._parent._cast(_4048.CouplingPowerFlow)

        @property
        def cvt_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4050
            
            return self._parent._cast(_4050.CVTPowerFlow)

        @property
        def cvt_pulley_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4051
            
            return self._parent._cast(_4051.CVTPulleyPowerFlow)

        @property
        def cycloidal_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4052
            
            return self._parent._cast(_4052.CycloidalAssemblyPowerFlow)

        @property
        def cycloidal_disc_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4055
            
            return self._parent._cast(_4055.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4058
            
            return self._parent._cast(_4058.CylindricalGearPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4059
            
            return self._parent._cast(_4059.CylindricalGearSetPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4060
            
            return self._parent._cast(_4060.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4061
            
            return self._parent._cast(_4061.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4062
            
            return self._parent._cast(_4062.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4064
            
            return self._parent._cast(_4064.FaceGearPowerFlow)

        @property
        def face_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4065
            
            return self._parent._cast(_4065.FaceGearSetPowerFlow)

        @property
        def fe_part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4066
            
            return self._parent._cast(_4066.FEPartPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4067
            
            return self._parent._cast(_4067.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4069
            
            return self._parent._cast(_4069.GearPowerFlow)

        @property
        def gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4070
            
            return self._parent._cast(_4070.GearSetPowerFlow)

        @property
        def guide_dxf_model_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4071
            
            return self._parent._cast(_4071.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4073
            
            return self._parent._cast(_4073.HypoidGearPowerFlow)

        @property
        def hypoid_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4074
            
            return self._parent._cast(_4074.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4077
            
            return self._parent._cast(_4077.KlingelnbergCycloPalloidConicalGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4078
            
            return self._parent._cast(_4078.KlingelnbergCycloPalloidConicalGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4080
            
            return self._parent._cast(_4080.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4081
            
            return self._parent._cast(_4081.KlingelnbergCycloPalloidHypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4083
            
            return self._parent._cast(_4083.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4084
            
            return self._parent._cast(_4084.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow)

        @property
        def mass_disc_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4085
            
            return self._parent._cast(_4085.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4086
            
            return self._parent._cast(_4086.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4087
            
            return self._parent._cast(_4087.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4088
            
            return self._parent._cast(_4088.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4091
            
            return self._parent._cast(_4091.PartToPartShearCouplingHalfPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4092
            
            return self._parent._cast(_4092.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4094
            
            return self._parent._cast(_4094.PlanetaryGearSetPowerFlow)

        @property
        def planet_carrier_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4095
            
            return self._parent._cast(_4095.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4096
            
            return self._parent._cast(_4096.PointLoadPowerFlow)

        @property
        def power_load_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4099
            
            return self._parent._cast(_4099.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4100
            
            return self._parent._cast(_4100.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4101
            
            return self._parent._cast(_4101.RingPinsPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4103
            
            return self._parent._cast(_4103.RollingRingAssemblyPowerFlow)

        @property
        def rolling_ring_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4105
            
            return self._parent._cast(_4105.RollingRingPowerFlow)

        @property
        def root_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4106
            
            return self._parent._cast(_4106.RootAssemblyPowerFlow)

        @property
        def shaft_hub_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4107
            
            return self._parent._cast(_4107.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4108
            
            return self._parent._cast(_4108.ShaftPowerFlow)

        @property
        def specialised_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4110
            
            return self._parent._cast(_4110.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4112
            
            return self._parent._cast(_4112.SpiralBevelGearPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4113
            
            return self._parent._cast(_4113.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4115
            
            return self._parent._cast(_4115.SpringDamperHalfPowerFlow)

        @property
        def spring_damper_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4116
            
            return self._parent._cast(_4116.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4118
            
            return self._parent._cast(_4118.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4119
            
            return self._parent._cast(_4119.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4121
            
            return self._parent._cast(_4121.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4122
            
            return self._parent._cast(_4122.StraightBevelGearSetPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4123
            
            return self._parent._cast(_4123.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4124
            
            return self._parent._cast(_4124.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4125
            
            return self._parent._cast(_4125.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4126
            
            return self._parent._cast(_4126.SynchroniserPartPowerFlow)

        @property
        def synchroniser_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4127
            
            return self._parent._cast(_4127.SynchroniserPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4128
            
            return self._parent._cast(_4128.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4131
            
            return self._parent._cast(_4131.TorqueConverterPowerFlow)

        @property
        def torque_converter_pump_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4132
            
            return self._parent._cast(_4132.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4133
            
            return self._parent._cast(_4133.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4134
            
            return self._parent._cast(_4134.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4135
            
            return self._parent._cast(_4135.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4137
            
            return self._parent._cast(_4137.WormGearPowerFlow)

        @property
        def worm_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4138
            
            return self._parent._cast(_4138.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4140
            
            return self._parent._cast(_4140.ZerolBevelGearPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4141
            
            return self._parent._cast(_4141.ZerolBevelGearSetPowerFlow)

        @property
        def part_power_flow(self) -> 'PartPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_power_flow(self) -> 'Image':
        """Image: 'TwoDDrawingShowingPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TwoDDrawingShowingPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def component_design(self) -> '_2448.Part':
        """Part: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow(self) -> '_4097.PowerFlow':
        """PowerFlow: 'PowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def create_viewable(self) -> '_2235.PowerFlowViewable':
        """ 'CreateViewable' is the original name of this method.

        Returns:
            mastapy.system_model.drawing.PowerFlowViewable
        """

        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'PartPowerFlow._Cast_PartPowerFlow':
        return self._Cast_PartPowerFlow(self)
