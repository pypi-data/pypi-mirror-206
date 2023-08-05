"""_6654.py

BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6523
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6650
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'BevelDifferentialSunGearCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialSunGearCompoundCriticalSpeedAnalysis',)


class BevelDifferentialSunGearCompoundCriticalSpeedAnalysis(_6650.BevelDifferentialGearCompoundCriticalSpeedAnalysis):
    """BevelDifferentialSunGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialSunGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'BevelDifferentialSunGearCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(self):
            return self._parent._cast(_6650.BevelDifferentialGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6655
            
            return self._parent._cast(_6655.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6643
            
            return self._parent._cast(_6643.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis)

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
        def bevel_differential_sun_gear_compound_critical_speed_analysis(self) -> 'BevelDifferentialSunGearCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialSunGearCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_6523.BevelDifferentialSunGearCriticalSpeedAnalysis]':
        """List[BevelDifferentialSunGearCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6523.BevelDifferentialSunGearCriticalSpeedAnalysis]':
        """List[BevelDifferentialSunGearCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis':
        return self._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis(self)
