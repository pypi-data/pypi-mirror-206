"""_6199.py

RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6070
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6112
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation',)


class RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation(_6112.AssemblyCompoundHarmonicAnalysisOfSingleExcitation):
    """RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def assembly_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6112.AssemblyCompoundHarmonicAnalysisOfSingleExcitation)

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
        def root_assembly_compound_harmonic_analysis_of_single_excitation(self) -> 'RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6070.RootAssemblyHarmonicAnalysisOfSingleExcitation]':
        """List[RootAssemblyHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6070.RootAssemblyHarmonicAnalysisOfSingleExcitation]':
        """List[RootAssemblyHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation(self)
