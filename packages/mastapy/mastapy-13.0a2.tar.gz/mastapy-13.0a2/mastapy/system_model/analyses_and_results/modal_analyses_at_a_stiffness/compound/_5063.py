"""_5063.py

SpringDamperConnectionCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2331
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4933
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4998
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'SpringDamperConnectionCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionCompoundModalAnalysisAtAStiffness',)


class SpringDamperConnectionCompoundModalAnalysisAtAStiffness(_4998.CouplingConnectionCompoundModalAnalysisAtAStiffness):
    """SpringDamperConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_SpringDamperConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting SpringDamperConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'SpringDamperConnectionCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4998.CouplingConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5025
            
            return self._parent._cast(_5025.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4995
            
            return self._parent._cast(_4995.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_stiffness(self) -> 'SpringDamperConnectionCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2331.SpringDamperConnection':
        """SpringDamperConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2331.SpringDamperConnection':
        """SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4933.SpringDamperConnectionModalAnalysisAtAStiffness]':
        """List[SpringDamperConnectionModalAnalysisAtAStiffness]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4933.SpringDamperConnectionModalAnalysisAtAStiffness]':
        """List[SpringDamperConnectionModalAnalysisAtAStiffness]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpringDamperConnectionCompoundModalAnalysisAtAStiffness._Cast_SpringDamperConnectionCompoundModalAnalysisAtAStiffness':
        return self._Cast_SpringDamperConnectionCompoundModalAnalysisAtAStiffness(self)
