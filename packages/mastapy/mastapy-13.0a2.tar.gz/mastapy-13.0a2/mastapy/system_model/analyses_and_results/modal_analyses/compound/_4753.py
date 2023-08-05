"""_4753.py

ExternalCADModelCompoundModalAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2432
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4602
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'ExternalCADModelCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelCompoundModalAnalysis',)


class ExternalCADModelCompoundModalAnalysis(_4726.ComponentCompoundModalAnalysis):
    """ExternalCADModelCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_MODAL_ANALYSIS

    class _Cast_ExternalCADModelCompoundModalAnalysis:
        """Special nested class for casting ExternalCADModelCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'ExternalCADModelCompoundModalAnalysis'):
            self._parent = parent

        @property
        def component_compound_modal_analysis(self):
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
        def external_cad_model_compound_modal_analysis(self) -> 'ExternalCADModelCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ExternalCADModelCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2432.ExternalCADModel':
        """ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4602.ExternalCADModelModalAnalysis]':
        """List[ExternalCADModelModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4602.ExternalCADModelModalAnalysis]':
        """List[ExternalCADModelModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ExternalCADModelCompoundModalAnalysis._Cast_ExternalCADModelCompoundModalAnalysis':
        return self._Cast_ExternalCADModelCompoundModalAnalysis(self)
