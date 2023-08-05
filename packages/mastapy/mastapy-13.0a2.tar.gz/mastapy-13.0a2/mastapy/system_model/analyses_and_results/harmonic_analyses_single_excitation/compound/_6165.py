"""_6165.py

GearSetCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6035
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6203
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'GearSetCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetCompoundHarmonicAnalysisOfSingleExcitation',)


class GearSetCompoundHarmonicAnalysisOfSingleExcitation(_6203.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation):
    """GearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_GearSetCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearSetCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'GearSetCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6203.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6105
            
            return self._parent._cast(_6105.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation)

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
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6111
            
            return self._parent._cast(_6111.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6118
            
            return self._parent._cast(_6118.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6123
            
            return self._parent._cast(_6123.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6136
            
            return self._parent._cast(_6136.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6139
            
            return self._parent._cast(_6139.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6154
            
            return self._parent._cast(_6154.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6160
            
            return self._parent._cast(_6160.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6169
            
            return self._parent._cast(_6169.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6173
            
            return self._parent._cast(_6173.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6176
            
            return self._parent._cast(_6176.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6179
            
            return self._parent._cast(_6179.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6189
            
            return self._parent._cast(_6189.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6206
            
            return self._parent._cast(_6206.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6212
            
            return self._parent._cast(_6212.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6215
            
            return self._parent._cast(_6215.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6230
            
            return self._parent._cast(_6230.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6233
            
            return self._parent._cast(_6233.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(self) -> 'GearSetCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_6035.GearSetHarmonicAnalysisOfSingleExcitation]':
        """List[GearSetHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6035.GearSetHarmonicAnalysisOfSingleExcitation]':
        """List[GearSetHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearSetCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_GearSetCompoundHarmonicAnalysisOfSingleExcitation(self)
