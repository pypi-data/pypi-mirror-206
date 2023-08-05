"""_5848.py

AbstractShaftOrHousingCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5651
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5871
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'AbstractShaftOrHousingCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingCompoundHarmonicAnalysis',)


class AbstractShaftOrHousingCompoundHarmonicAnalysis(_5871.ComponentCompoundHarmonicAnalysis):
    """AbstractShaftOrHousingCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def component_compound_harmonic_analysis(self):
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
        def abstract_shaft_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5847
            
            return self._parent._cast(_5847.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5891
            
            return self._parent._cast(_5891.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5902
            
            return self._parent._cast(_5902.FEPartCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5941
            
            return self._parent._cast(_5941.ShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(self) -> 'AbstractShaftOrHousingCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5651.AbstractShaftOrHousingHarmonicAnalysis]':
        """List[AbstractShaftOrHousingHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5651.AbstractShaftOrHousingHarmonicAnalysis]':
        """List[AbstractShaftOrHousingHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis':
        return self._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis(self)
