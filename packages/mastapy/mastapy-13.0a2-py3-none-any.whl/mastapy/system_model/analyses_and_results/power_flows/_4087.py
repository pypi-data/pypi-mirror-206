"""_4087.py

MountableComponentPowerFlow
"""
from mastapy.system_model.part_model import _2444
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4034
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'MountableComponentPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentPowerFlow',)


class MountableComponentPowerFlow(_4034.ComponentPowerFlow):
    """MountableComponentPowerFlow

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_POWER_FLOW

    class _Cast_MountableComponentPowerFlow:
        """Special nested class for casting MountableComponentPowerFlow to subclasses."""

        def __init__(self, parent: 'MountableComponentPowerFlow'):
            self._parent = parent

        @property
        def component_power_flow(self):
            return self._parent._cast(_4034.ComponentPowerFlow)

        @property
        def part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4089
            
            return self._parent._cast(_4089.PartPowerFlow)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
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
        def agma_gleason_conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4014
            
            return self._parent._cast(_4014.AGMAGleasonConicalGearPowerFlow)

        @property
        def bearing_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4017
            
            return self._parent._cast(_4017.BearingPowerFlow)

        @property
        def bevel_differential_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4021
            
            return self._parent._cast(_4021.BevelDifferentialGearPowerFlow)

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
        def clutch_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4031
            
            return self._parent._cast(_4031.ClutchHalfPowerFlow)

        @property
        def concept_coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4036
            
            return self._parent._cast(_4036.ConceptCouplingHalfPowerFlow)

        @property
        def concept_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4039
            
            return self._parent._cast(_4039.ConceptGearPowerFlow)

        @property
        def conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4042
            
            return self._parent._cast(_4042.ConicalGearPowerFlow)

        @property
        def connector_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4045
            
            return self._parent._cast(_4045.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4047
            
            return self._parent._cast(_4047.CouplingHalfPowerFlow)

        @property
        def cvt_pulley_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4051
            
            return self._parent._cast(_4051.CVTPulleyPowerFlow)

        @property
        def cylindrical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4058
            
            return self._parent._cast(_4058.CylindricalGearPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4060
            
            return self._parent._cast(_4060.CylindricalPlanetGearPowerFlow)

        @property
        def face_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4064
            
            return self._parent._cast(_4064.FaceGearPowerFlow)

        @property
        def gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4069
            
            return self._parent._cast(_4069.GearPowerFlow)

        @property
        def hypoid_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4073
            
            return self._parent._cast(_4073.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4077
            
            return self._parent._cast(_4077.KlingelnbergCycloPalloidConicalGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4080
            
            return self._parent._cast(_4080.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4083
            
            return self._parent._cast(_4083.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow)

        @property
        def mass_disc_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4085
            
            return self._parent._cast(_4085.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4086
            
            return self._parent._cast(_4086.MeasurementComponentPowerFlow)

        @property
        def oil_seal_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4088
            
            return self._parent._cast(_4088.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4091
            
            return self._parent._cast(_4091.PartToPartShearCouplingHalfPowerFlow)

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
        def rolling_ring_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4105
            
            return self._parent._cast(_4105.RollingRingPowerFlow)

        @property
        def shaft_hub_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4107
            
            return self._parent._cast(_4107.ShaftHubConnectionPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4112
            
            return self._parent._cast(_4112.SpiralBevelGearPowerFlow)

        @property
        def spring_damper_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4115
            
            return self._parent._cast(_4115.SpringDamperHalfPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4118
            
            return self._parent._cast(_4118.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4121
            
            return self._parent._cast(_4121.StraightBevelGearPowerFlow)

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
        def synchroniser_sleeve_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4128
            
            return self._parent._cast(_4128.SynchroniserSleevePowerFlow)

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
        def zerol_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4140
            
            return self._parent._cast(_4140.ZerolBevelGearPowerFlow)

        @property
        def mountable_component_power_flow(self) -> 'MountableComponentPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2444.MountableComponent':
        """MountableComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MountableComponentPowerFlow._Cast_MountableComponentPowerFlow':
        return self._Cast_MountableComponentPowerFlow(self)
