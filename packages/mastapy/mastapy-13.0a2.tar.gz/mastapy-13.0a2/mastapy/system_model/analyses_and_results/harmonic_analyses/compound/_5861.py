"""_5861.py

BevelDifferentialSunGearCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5664
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5857
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'BevelDifferentialSunGearCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialSunGearCompoundHarmonicAnalysis',)


class BevelDifferentialSunGearCompoundHarmonicAnalysis(_5857.BevelDifferentialGearCompoundHarmonicAnalysis):
    """BevelDifferentialSunGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialSunGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'BevelDifferentialSunGearCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_harmonic_analysis(self):
            return self._parent._cast(_5857.BevelDifferentialGearCompoundHarmonicAnalysis)

        @property
        def bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5862
            
            return self._parent._cast(_5862.BevelGearCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5850
            
            return self._parent._cast(_5850.AGMAGleasonConicalGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5878
            
            return self._parent._cast(_5878.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5904
            
            return self._parent._cast(_5904.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5923
            
            return self._parent._cast(_5923.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5871
            
            return self._parent._cast(_5871.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5925
            
            return self._parent._cast(_5925.PartCompoundHarmonicAnalysis)

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
        def bevel_differential_sun_gear_compound_harmonic_analysis(self) -> 'BevelDifferentialSunGearCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialSunGearCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_5664.BevelDifferentialSunGearHarmonicAnalysis]':
        """List[BevelDifferentialSunGearHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5664.BevelDifferentialSunGearHarmonicAnalysis]':
        """List[BevelDifferentialSunGearHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis':
        return self._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis(self)
