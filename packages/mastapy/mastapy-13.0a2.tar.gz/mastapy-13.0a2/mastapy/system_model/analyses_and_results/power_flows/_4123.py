"""_4123.py

StraightBevelPlanetGearPowerFlow
"""
from mastapy.system_model.part_model.gears import _2528
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4118
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'StraightBevelPlanetGearPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelPlanetGearPowerFlow',)


class StraightBevelPlanetGearPowerFlow(_4118.StraightBevelDiffGearPowerFlow):
    """StraightBevelPlanetGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_POWER_FLOW

    class _Cast_StraightBevelPlanetGearPowerFlow:
        """Special nested class for casting StraightBevelPlanetGearPowerFlow to subclasses."""

        def __init__(self, parent: 'StraightBevelPlanetGearPowerFlow'):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_power_flow(self):
            return self._parent._cast(_4118.StraightBevelDiffGearPowerFlow)

        @property
        def bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4026
            
            return self._parent._cast(_4026.BevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4014
            
            return self._parent._cast(_4014.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4042
            
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
        def straight_bevel_planet_gear_power_flow(self) -> 'StraightBevelPlanetGearPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelPlanetGearPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2528.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow':
        return self._Cast_StraightBevelPlanetGearPowerFlow(self)
