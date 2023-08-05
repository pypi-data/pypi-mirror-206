"""_6107.py

AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5977
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6130
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation',)


class AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation(_6130.ComponentCompoundHarmonicAnalysisOfSingleExcitation):
    """AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def component_compound_harmonic_analysis_of_single_excitation(self):
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
        def abstract_shaft_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6106
            
            return self._parent._cast(_6106.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6150
            
            return self._parent._cast(_6150.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def fe_part_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6161
            
            return self._parent._cast(_6161.FEPartCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6200
            
            return self._parent._cast(_6200.ShaftCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(self) -> 'AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5977.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation]':
        """List[AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5977.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation]':
        """List[AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation(self)
