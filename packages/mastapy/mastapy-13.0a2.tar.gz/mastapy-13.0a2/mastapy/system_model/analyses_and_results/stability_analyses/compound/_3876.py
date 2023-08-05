"""_3876.py

AbstractShaftOrHousingCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3743
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3899
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'AbstractShaftOrHousingCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingCompoundStabilityAnalysis',)


class AbstractShaftOrHousingCompoundStabilityAnalysis(_3899.ComponentCompoundStabilityAnalysis):
    """AbstractShaftOrHousingCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STABILITY_ANALYSIS

    class _Cast_AbstractShaftOrHousingCompoundStabilityAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def component_compound_stability_analysis(self):
            return self._parent._cast(_3899.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3953
            
            return self._parent._cast(_3953.PartCompoundStabilityAnalysis)

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
        def abstract_shaft_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3875
            
            return self._parent._cast(_3875.AbstractShaftCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3919
            
            return self._parent._cast(_3919.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3930
            
            return self._parent._cast(_3930.FEPartCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3969
            
            return self._parent._cast(_3969.ShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(self) -> 'AbstractShaftOrHousingCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3743.AbstractShaftOrHousingStabilityAnalysis]':
        """List[AbstractShaftOrHousingStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3743.AbstractShaftOrHousingStabilityAnalysis]':
        """List[AbstractShaftOrHousingStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis':
        return self._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis(self)
