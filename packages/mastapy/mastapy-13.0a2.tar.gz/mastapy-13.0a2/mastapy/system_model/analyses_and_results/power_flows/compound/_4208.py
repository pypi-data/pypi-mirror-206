"""_4208.py

KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4077
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4174
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'KlingelnbergCycloPalloidConicalGearCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearCompoundPowerFlow',)


class KlingelnbergCycloPalloidConicalGearCompoundPowerFlow(_4174.ConicalGearCompoundPowerFlow):
    """KlingelnbergCycloPalloidConicalGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_POWER_FLOW

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearCompoundPowerFlow'):
            self._parent = parent

        @property
        def conical_gear_compound_power_flow(self):
            return self._parent._cast(_4174.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4200
            
            return self._parent._cast(_4200.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4219
            
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
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4211
            
            return self._parent._cast(_4211.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4214
            
            return self._parent._cast(_4214.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(self) -> 'KlingelnbergCycloPalloidConicalGearCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4077.KlingelnbergCycloPalloidConicalGearPowerFlow]':
        """List[KlingelnbergCycloPalloidConicalGearPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4077.KlingelnbergCycloPalloidConicalGearPowerFlow]':
        """List[KlingelnbergCycloPalloidConicalGearPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow':
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow(self)
