"""_6193.py

PulleyCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2569
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6064
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6144
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'PulleyCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyCompoundHarmonicAnalysisOfSingleExcitation',)


class PulleyCompoundHarmonicAnalysisOfSingleExcitation(_6144.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation):
    """PulleyCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_PulleyCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PulleyCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'PulleyCompoundHarmonicAnalysisOfSingleExcitation'):
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
        def cvt_pulley_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6147
            
            return self._parent._cast(_6147.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_compound_harmonic_analysis_of_single_excitation(self) -> 'PulleyCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PulleyCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2569.Pulley':
        """Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6064.PulleyHarmonicAnalysisOfSingleExcitation]':
        """List[PulleyHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6064.PulleyHarmonicAnalysisOfSingleExcitation]':
        """List[PulleyHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_PulleyCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_PulleyCompoundHarmonicAnalysisOfSingleExcitation(self)
