"""_6119.py

BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5989
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6116
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation',)


class BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation(_6116.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation):
    """BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6116.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6121
            
            return self._parent._cast(_6121.BevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6109
            
            return self._parent._cast(_6109.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6137
            
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
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(self) -> 'BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_5989.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation]':
        """List[BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5989.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation]':
        """List[BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation(self)
