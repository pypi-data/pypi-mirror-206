"""_5314.py

ShaftHubConnectionCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2577
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5184
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5254
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'ShaftHubConnectionCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionCompoundModalAnalysisAtASpeed',)


class ShaftHubConnectionCompoundModalAnalysisAtASpeed(_5254.ConnectorCompoundModalAnalysisAtASpeed):
    """ShaftHubConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_ShaftHubConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ShaftHubConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'ShaftHubConnectionCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def connector_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5254.ConnectorCompoundModalAnalysisAtASpeed)

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
        def shaft_hub_connection_compound_modal_analysis_at_a_speed(self) -> 'ShaftHubConnectionCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2577.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5184.ShaftHubConnectionModalAnalysisAtASpeed]':
        """List[ShaftHubConnectionModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[ShaftHubConnectionCompoundModalAnalysisAtASpeed]':
        """List[ShaftHubConnectionCompoundModalAnalysisAtASpeed]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5184.ShaftHubConnectionModalAnalysisAtASpeed]':
        """List[ShaftHubConnectionModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftHubConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftHubConnectionCompoundModalAnalysisAtASpeed':
        return self._Cast_ShaftHubConnectionCompoundModalAnalysisAtASpeed(self)
