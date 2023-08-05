"""_5339.py

UnbalancedMassCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.part_model import _2457
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5210
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5340
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'UnbalancedMassCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassCompoundModalAnalysisAtASpeed',)


class UnbalancedMassCompoundModalAnalysisAtASpeed(_5340.VirtualComponentCompoundModalAnalysisAtASpeed):
    """UnbalancedMassCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_UnbalancedMassCompoundModalAnalysisAtASpeed:
        """Special nested class for casting UnbalancedMassCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'UnbalancedMassCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5340.VirtualComponentCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5295
            
            return self._parent._cast(_5295.MountableComponentCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5243
            
            return self._parent._cast(_5243.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5297
            
            return self._parent._cast(_5297.PartCompoundModalAnalysisAtASpeed)

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
        def unbalanced_mass_compound_modal_analysis_at_a_speed(self) -> 'UnbalancedMassCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'UnbalancedMassCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2457.UnbalancedMass':
        """UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5210.UnbalancedMassModalAnalysisAtASpeed]':
        """List[UnbalancedMassModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5210.UnbalancedMassModalAnalysisAtASpeed]':
        """List[UnbalancedMassModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'UnbalancedMassCompoundModalAnalysisAtASpeed._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed':
        return self._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed(self)
