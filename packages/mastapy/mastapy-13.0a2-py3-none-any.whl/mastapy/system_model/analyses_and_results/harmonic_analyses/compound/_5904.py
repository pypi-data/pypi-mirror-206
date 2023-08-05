"""_5904.py

GearCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5722
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5923
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'GearCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundHarmonicAnalysis',)


class GearCompoundHarmonicAnalysis(_5923.MountableComponentCompoundHarmonicAnalysis):
    """GearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_GearCompoundHarmonicAnalysis:
        """Special nested class for casting GearCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'GearCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis(self):
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
        def agma_gleason_conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5850
            
            return self._parent._cast(_5850.AGMAGleasonConicalGearCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5857
            
            return self._parent._cast(_5857.BevelDifferentialGearCompoundHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5860
            
            return self._parent._cast(_5860.BevelDifferentialPlanetGearCompoundHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5861
            
            return self._parent._cast(_5861.BevelDifferentialSunGearCompoundHarmonicAnalysis)

        @property
        def bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5862
            
            return self._parent._cast(_5862.BevelGearCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5875
            
            return self._parent._cast(_5875.ConceptGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5878
            
            return self._parent._cast(_5878.ConicalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5893
            
            return self._parent._cast(_5893.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5896
            
            return self._parent._cast(_5896.CylindricalPlanetGearCompoundHarmonicAnalysis)

        @property
        def face_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5899
            
            return self._parent._cast(_5899.FaceGearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5908
            
            return self._parent._cast(_5908.HypoidGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5912
            
            return self._parent._cast(_5912.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5915
            
            return self._parent._cast(_5915.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5918
            
            return self._parent._cast(_5918.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5945
            
            return self._parent._cast(_5945.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5951
            
            return self._parent._cast(_5951.StraightBevelDiffGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5954
            
            return self._parent._cast(_5954.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5957
            
            return self._parent._cast(_5957.StraightBevelPlanetGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5958
            
            return self._parent._cast(_5958.StraightBevelSunGearCompoundHarmonicAnalysis)

        @property
        def worm_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5969
            
            return self._parent._cast(_5969.WormGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5972
            
            return self._parent._cast(_5972.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(self) -> 'GearCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5722.GearHarmonicAnalysis]':
        """List[GearHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5722.GearHarmonicAnalysis]':
        """List[GearHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis':
        return self._Cast_GearCompoundHarmonicAnalysis(self)
