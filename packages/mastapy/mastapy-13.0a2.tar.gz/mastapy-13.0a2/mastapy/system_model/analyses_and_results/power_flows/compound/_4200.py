"""_4200.py

GearCompoundPowerFlow
"""
from typing import List

from mastapy.gears.rating import _354
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4069
from mastapy.system_model.analyses_and_results.power_flows.compound import _4219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'GearCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundPowerFlow',)


class GearCompoundPowerFlow(_4219.MountableComponentCompoundPowerFlow):
    """GearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_POWER_FLOW

    class _Cast_GearCompoundPowerFlow:
        """Special nested class for casting GearCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'GearCompoundPowerFlow'):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(self):
            return self._parent._cast(_4219.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4167
            
            return self._parent._cast(_4167.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4221
            
            return self._parent._cast(_4221.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4146
            
            return self._parent._cast(_4146.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4153
            
            return self._parent._cast(_4153.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4156
            
            return self._parent._cast(_4156.BevelDifferentialPlanetGearCompoundPowerFlow)

        @property
        def bevel_differential_sun_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4157
            
            return self._parent._cast(_4157.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4158
            
            return self._parent._cast(_4158.BevelGearCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4171
            
            return self._parent._cast(_4171.ConceptGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4174
            
            return self._parent._cast(_4174.ConicalGearCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4189
            
            return self._parent._cast(_4189.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4192
            
            return self._parent._cast(_4192.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4195
            
            return self._parent._cast(_4195.FaceGearCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4204
            
            return self._parent._cast(_4204.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4208
            
            return self._parent._cast(_4208.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4211
            
            return self._parent._cast(_4211.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4214
            
            return self._parent._cast(_4214.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4241
            
            return self._parent._cast(_4241.SpiralBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4247
            
            return self._parent._cast(_4247.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4250
            
            return self._parent._cast(_4250.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4253
            
            return self._parent._cast(_4253.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4254
            
            return self._parent._cast(_4254.StraightBevelSunGearCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4265
            
            return self._parent._cast(_4265.WormGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4268
            
            return self._parent._cast(_4268.ZerolBevelGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(self) -> 'GearCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self) -> '_354.GearDutyCycleRating':
        """GearDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases(self) -> 'List[_4069.GearPowerFlow]':
        """List[GearPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4069.GearPowerFlow]':
        """List[GearPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundPowerFlow._Cast_GearCompoundPowerFlow':
        return self._Cast_GearCompoundPowerFlow(self)
