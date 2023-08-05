"""_4805.py

SpringDamperHalfCompoundModalAnalysis
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2580
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4660
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4740
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'SpringDamperHalfCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfCompoundModalAnalysis',)


class SpringDamperHalfCompoundModalAnalysis(_4740.CouplingHalfCompoundModalAnalysis):
    """SpringDamperHalfCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_MODAL_ANALYSIS

    class _Cast_SpringDamperHalfCompoundModalAnalysis:
        """Special nested class for casting SpringDamperHalfCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'SpringDamperHalfCompoundModalAnalysis'):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis(self):
            return self._parent._cast(_4740.CouplingHalfCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4778
            
            return self._parent._cast(_4778.MountableComponentCompoundModalAnalysis)

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
        def spring_damper_half_compound_modal_analysis(self) -> 'SpringDamperHalfCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfCompoundModalAnalysis.TYPE'):
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
    def component_analysis_cases_ready(self) -> 'List[_4660.SpringDamperHalfModalAnalysis]':
        """List[SpringDamperHalfModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4660.SpringDamperHalfModalAnalysis]':
        """List[SpringDamperHalfModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpringDamperHalfCompoundModalAnalysis._Cast_SpringDamperHalfCompoundModalAnalysis':
        return self._Cast_SpringDamperHalfCompoundModalAnalysis(self)
