"""_4962.py

AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4832
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4985
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness',)


class AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness(_4985.ComponentCompoundModalAnalysisAtAStiffness):
    """AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def component_compound_modal_analysis_at_a_stiffness(self):
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
        def abstract_shaft_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4961
            
            return self._parent._cast(_4961.AbstractShaftCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5005
            
            return self._parent._cast(_5005.CycloidalDiscCompoundModalAnalysisAtAStiffness)

        @property
        def fe_part_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5016
            
            return self._parent._cast(_5016.FEPartCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5055
            
            return self._parent._cast(_5055.ShaftCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(self) -> 'AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4832.AbstractShaftOrHousingModalAnalysisAtAStiffness]':
        """List[AbstractShaftOrHousingModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4832.AbstractShaftOrHousingModalAnalysisAtAStiffness]':
        """List[AbstractShaftOrHousingModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness':
        return self._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness(self)
