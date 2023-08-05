"""_5005.py

CycloidalDiscCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.part_model.cycloidal import _2548
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4875
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4961
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'CycloidalDiscCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCompoundModalAnalysisAtAStiffness',)


class CycloidalDiscCompoundModalAnalysisAtAStiffness(_4961.AbstractShaftCompoundModalAnalysisAtAStiffness):
    """CycloidalDiscCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_CycloidalDiscCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CycloidalDiscCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def abstract_shaft_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4961.AbstractShaftCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4962
            
            return self._parent._cast(_4962.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness)

        @property
        def component_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4985
            
            return self._parent._cast(_4985.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5039
            
            return self._parent._cast(_5039.PartCompoundModalAnalysisAtAStiffness)

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
        def cycloidal_disc_compound_modal_analysis_at_a_stiffness(self) -> 'CycloidalDiscCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2548.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4875.CycloidalDiscModalAnalysisAtAStiffness]':
        """List[CycloidalDiscModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4875.CycloidalDiscModalAnalysisAtAStiffness]':
        """List[CycloidalDiscModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCompoundModalAnalysisAtAStiffness':
        return self._Cast_CycloidalDiscCompoundModalAnalysisAtAStiffness(self)
