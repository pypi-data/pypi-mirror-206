"""_4982.py

ClutchConnectionCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2323
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4851
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4998
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'ClutchConnectionCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionCompoundModalAnalysisAtAStiffness',)


class ClutchConnectionCompoundModalAnalysisAtAStiffness(_4998.CouplingConnectionCompoundModalAnalysisAtAStiffness):
    """ClutchConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_ClutchConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting ClutchConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'ClutchConnectionCompoundModalAnalysisAtAStiffness'):
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
        def clutch_connection_compound_modal_analysis_at_a_stiffness(self) -> 'ClutchConnectionCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchConnectionCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2323.ClutchConnection':
        """ClutchConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2323.ClutchConnection':
        """ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4851.ClutchConnectionModalAnalysisAtAStiffness]':
        """List[ClutchConnectionModalAnalysisAtAStiffness]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4851.ClutchConnectionModalAnalysisAtAStiffness]':
        """List[ClutchConnectionModalAnalysisAtAStiffness]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ClutchConnectionCompoundModalAnalysisAtAStiffness._Cast_ClutchConnectionCompoundModalAnalysisAtAStiffness':
        return self._Cast_ClutchConnectionCompoundModalAnalysisAtAStiffness(self)
