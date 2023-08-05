"""_4014.py

AGMAGleasonConicalGearPowerFlow
"""
from mastapy.system_model.part_model.gears import _2492
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4042
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'AGMAGleasonConicalGearPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearPowerFlow',)


class AGMAGleasonConicalGearPowerFlow(_4042.ConicalGearPowerFlow):
    """AGMAGleasonConicalGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_POWER_FLOW

    class _Cast_AGMAGleasonConicalGearPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearPowerFlow to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearPowerFlow'):
            self._parent = parent

        @property
        def conical_gear_power_flow(self):
            return self._parent._cast(_4042.ConicalGearPowerFlow)

        @property
        def gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4069
            
            return self._parent._cast(_4069.GearPowerFlow)

        @property
        def mountable_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4087
            
            return self._parent._cast(_4087.MountableComponentPowerFlow)

        @property
        def component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4034
            
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
        def hypoid_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4073
            
            return self._parent._cast(_4073.HypoidGearPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4112
            
            return self._parent._cast(_4112.SpiralBevelGearPowerFlow)

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
        def zerol_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4140
            
            return self._parent._cast(_4140.ZerolBevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(self) -> 'AGMAGleasonConicalGearPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2492.AGMAGleasonConicalGear':
        """AGMAGleasonConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow':
        return self._Cast_AGMAGleasonConicalGearPowerFlow(self)
