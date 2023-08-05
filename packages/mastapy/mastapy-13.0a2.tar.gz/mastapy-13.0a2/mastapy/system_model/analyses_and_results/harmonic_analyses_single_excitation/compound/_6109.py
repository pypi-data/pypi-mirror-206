"""_6109.py

AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5979
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6137
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation',)


class AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation(_6137.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation):
    """AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6137.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6163
            
            return self._parent._cast(_6163.GearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6182
            
            return self._parent._cast(_6182.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def component_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6130
            
            return self._parent._cast(_6130.ComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def part_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6184
            
            return self._parent._cast(_6184.PartCompoundHarmonicAnalysisOfSingleExcitation)

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
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6116
            
            return self._parent._cast(_6116.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6119
            
            return self._parent._cast(_6119.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6120
            
            return self._parent._cast(_6120.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6121
            
            return self._parent._cast(_6121.BevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6167
            
            return self._parent._cast(_6167.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6204
            
            return self._parent._cast(_6204.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6210
            
            return self._parent._cast(_6210.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6213
            
            return self._parent._cast(_6213.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6216
            
            return self._parent._cast(_6216.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6217
            
            return self._parent._cast(_6217.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6231
            
            return self._parent._cast(_6231.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(self) -> 'AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5979.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation]':
        """List[AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5979.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation]':
        """List[AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation(self)
