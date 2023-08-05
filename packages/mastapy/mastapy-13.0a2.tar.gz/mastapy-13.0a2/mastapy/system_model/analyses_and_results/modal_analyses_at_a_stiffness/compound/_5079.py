"""_5079.py

TorqueConverterPumpCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2587
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4950
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4999
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'TorqueConverterPumpCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpCompoundModalAnalysisAtAStiffness',)


class TorqueConverterPumpCompoundModalAnalysisAtAStiffness(_4999.CouplingHalfCompoundModalAnalysisAtAStiffness):
    """TorqueConverterPumpCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_TorqueConverterPumpCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting TorqueConverterPumpCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'TorqueConverterPumpCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4999.CouplingHalfCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5037
            
            return self._parent._cast(_5037.MountableComponentCompoundModalAnalysisAtAStiffness)

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
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(self) -> 'TorqueConverterPumpCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2587.TorqueConverterPump':
        """TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4950.TorqueConverterPumpModalAnalysisAtAStiffness]':
        """List[TorqueConverterPumpModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4950.TorqueConverterPumpModalAnalysisAtAStiffness]':
        """List[TorqueConverterPumpModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'TorqueConverterPumpCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterPumpCompoundModalAnalysisAtAStiffness':
        return self._Cast_TorqueConverterPumpCompoundModalAnalysisAtAStiffness(self)
