"""_6209.py

SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2580
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6079
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6144
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation',)


class SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation(_6144.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation):
    """SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6144.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation)

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
        def spring_damper_half_compound_harmonic_analysis_of_single_excitation(self) -> 'SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2580.SpringDamperHalf':
        """SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6079.SpringDamperHalfHarmonicAnalysisOfSingleExcitation]':
        """List[SpringDamperHalfHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6079.SpringDamperHalfHarmonicAnalysisOfSingleExcitation]':
        """List[SpringDamperHalfHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation(self)
