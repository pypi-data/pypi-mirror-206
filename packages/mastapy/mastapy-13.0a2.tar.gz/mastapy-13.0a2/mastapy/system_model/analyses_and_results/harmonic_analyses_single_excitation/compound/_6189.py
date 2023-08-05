"""_6189.py

PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6060
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6154
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation',)


class PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation(_6154.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation):
    """PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6154.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6165
            
            return self._parent._cast(_6165.GearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6203
            
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
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(self) -> 'PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6060.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation]':
        """List[PlanetaryGearSetHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6060.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation]':
        """List[PlanetaryGearSetHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation(self)
