"""_5941.py

ShaftCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.part_model.shaft_model import _2462
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5773
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5847
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'ShaftCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftCompoundHarmonicAnalysis',)


class ShaftCompoundHarmonicAnalysis(_5847.AbstractShaftCompoundHarmonicAnalysis):
    """ShaftCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_ShaftCompoundHarmonicAnalysis:
        """Special nested class for casting ShaftCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'ShaftCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_compound_harmonic_analysis(self):
            return self._parent._cast(_5847.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5848
            
            return self._parent._cast(_5848.AbstractShaftOrHousingCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5871
            
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
        def shaft_compound_harmonic_analysis(self) -> 'ShaftCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2462.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5773.ShaftHarmonicAnalysis]':
        """List[ShaftHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[ShaftCompoundHarmonicAnalysis]':
        """List[ShaftCompoundHarmonicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5773.ShaftHarmonicAnalysis]':
        """List[ShaftHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftCompoundHarmonicAnalysis._Cast_ShaftCompoundHarmonicAnalysis':
        return self._Cast_ShaftCompoundHarmonicAnalysis(self)
