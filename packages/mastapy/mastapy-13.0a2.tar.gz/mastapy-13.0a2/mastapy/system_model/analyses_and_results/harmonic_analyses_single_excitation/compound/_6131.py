"""_6131.py

ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2560
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6003
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation',)


class ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation(_6142.CouplingCompoundHarmonicAnalysisOfSingleExcitation):
    """ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6142.CouplingCompoundHarmonicAnalysisOfSingleExcitation)

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
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(self) -> 'ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2560.ConceptCoupling':
        """ConceptCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2560.ConceptCoupling':
        """ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6003.ConceptCouplingHarmonicAnalysisOfSingleExcitation]':
        """List[ConceptCouplingHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6003.ConceptCouplingHarmonicAnalysisOfSingleExcitation]':
        """List[ConceptCouplingHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation(self)
