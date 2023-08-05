"""_4702.py

AbstractShaftCompoundModalAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses import _4548
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4703
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'AbstractShaftCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftCompoundModalAnalysis',)


class AbstractShaftCompoundModalAnalysis(_4703.AbstractShaftOrHousingCompoundModalAnalysis):
    """AbstractShaftCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_MODAL_ANALYSIS

    class _Cast_AbstractShaftCompoundModalAnalysis:
        """Special nested class for casting AbstractShaftCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftCompoundModalAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(self):
            return self._parent._cast(_4703.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4726
            
            return self._parent._cast(_4726.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4780
            
            return self._parent._cast(_4780.PartCompoundModalAnalysis)

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
        def cycloidal_disc_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4746
            
            return self._parent._cast(_4746.CycloidalDiscCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4796
            
            return self._parent._cast(_4796.ShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(self) -> 'AbstractShaftCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4548.AbstractShaftModalAnalysis]':
        """List[AbstractShaftModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4548.AbstractShaftModalAnalysis]':
        """List[AbstractShaftModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis':
        return self._Cast_AbstractShaftCompoundModalAnalysis(self)
