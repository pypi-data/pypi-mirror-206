"""_6708.py

KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.part_model.gears import _2517
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6579
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6705
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis',)


class KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis(_6705.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis):
    """KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(self):
            return self._parent._cast(_6705.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6671
            
            return self._parent._cast(_6671.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6697
            
            return self._parent._cast(_6697.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6716
            
            return self._parent._cast(_6716.MountableComponentCompoundCriticalSpeedAnalysis)

        @property
        def component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6664
            
            return self._parent._cast(_6664.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6718
            
            return self._parent._cast(_6718.PartCompoundCriticalSpeedAnalysis)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(self) -> 'KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2517.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6579.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6579.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis(self)
