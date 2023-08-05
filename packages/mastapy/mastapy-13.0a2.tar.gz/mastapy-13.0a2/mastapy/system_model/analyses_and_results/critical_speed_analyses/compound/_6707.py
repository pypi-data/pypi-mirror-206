"""_6707.py

KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6578
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6673
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis',)


class KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis(_6673.ConicalGearSetCompoundCriticalSpeedAnalysis):
    """KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def conical_gear_set_compound_critical_speed_analysis(self):
            return self._parent._cast(_6673.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6699
            
            return self._parent._cast(_6699.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6737
            
            return self._parent._cast(_6737.SpecialisedAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def abstract_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6639
            
            return self._parent._cast(_6639.AbstractAssemblyCompoundCriticalSpeedAnalysis)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6710
            
            return self._parent._cast(_6710.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6713
            
            return self._parent._cast(_6713.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(self) -> 'KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_6578.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis]':
        """List[KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6578.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis]':
        """List[KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis':
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis(self)
