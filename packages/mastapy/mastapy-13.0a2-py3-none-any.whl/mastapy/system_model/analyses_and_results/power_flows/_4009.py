"""_4009.py

AbstractAssemblyPowerFlow
"""
from mastapy.system_model.part_model import _2414
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4089
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'AbstractAssemblyPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyPowerFlow',)


class AbstractAssemblyPowerFlow(_4089.PartPowerFlow):
    """AbstractAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_POWER_FLOW

    class _Cast_AbstractAssemblyPowerFlow:
        """Special nested class for casting AbstractAssemblyPowerFlow to subclasses."""

        def __init__(self, parent: 'AbstractAssemblyPowerFlow'):
            self._parent = parent

        @property
        def part_power_flow(self):
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
        def agma_gleason_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4015
            
            return self._parent._cast(_4015.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4016
            
            return self._parent._cast(_4016.AssemblyPowerFlow)

        @property
        def belt_drive_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4019
            
            return self._parent._cast(_4019.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4022
            
            return self._parent._cast(_4022.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4027
            
            return self._parent._cast(_4027.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4028
            
            return self._parent._cast(_4028.BoltedJointPowerFlow)

        @property
        def clutch_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4032
            
            return self._parent._cast(_4032.ClutchPowerFlow)

        @property
        def concept_coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4037
            
            return self._parent._cast(_4037.ConceptCouplingPowerFlow)

        @property
        def concept_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4040
            
            return self._parent._cast(_4040.ConceptGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4043
            
            return self._parent._cast(_4043.ConicalGearSetPowerFlow)

        @property
        def coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4048
            
            return self._parent._cast(_4048.CouplingPowerFlow)

        @property
        def cvt_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4050
            
            return self._parent._cast(_4050.CVTPowerFlow)

        @property
        def cycloidal_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4052
            
            return self._parent._cast(_4052.CycloidalAssemblyPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4059
            
            return self._parent._cast(_4059.CylindricalGearSetPowerFlow)

        @property
        def face_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4065
            
            return self._parent._cast(_4065.FaceGearSetPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4067
            
            return self._parent._cast(_4067.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4070
            
            return self._parent._cast(_4070.GearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4074
            
            return self._parent._cast(_4074.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4078
            
            return self._parent._cast(_4078.KlingelnbergCycloPalloidConicalGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4081
            
            return self._parent._cast(_4081.KlingelnbergCycloPalloidHypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4084
            
            return self._parent._cast(_4084.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4092
            
            return self._parent._cast(_4092.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4094
            
            return self._parent._cast(_4094.PlanetaryGearSetPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4103
            
            return self._parent._cast(_4103.RollingRingAssemblyPowerFlow)

        @property
        def root_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4106
            
            return self._parent._cast(_4106.RootAssemblyPowerFlow)

        @property
        def specialised_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4110
            
            return self._parent._cast(_4110.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4113
            
            return self._parent._cast(_4113.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4116
            
            return self._parent._cast(_4116.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4119
            
            return self._parent._cast(_4119.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4122
            
            return self._parent._cast(_4122.StraightBevelGearSetPowerFlow)

        @property
        def synchroniser_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4127
            
            return self._parent._cast(_4127.SynchroniserPowerFlow)

        @property
        def torque_converter_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4131
            
            return self._parent._cast(_4131.TorqueConverterPowerFlow)

        @property
        def worm_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4138
            
            return self._parent._cast(_4138.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4141
            
            return self._parent._cast(_4141.ZerolBevelGearSetPowerFlow)

        @property
        def abstract_assembly_power_flow(self) -> 'AbstractAssemblyPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2414.AbstractAssembly':
        """AbstractAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2414.AbstractAssembly':
        """AbstractAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow':
        return self._Cast_AbstractAssemblyPowerFlow(self)
