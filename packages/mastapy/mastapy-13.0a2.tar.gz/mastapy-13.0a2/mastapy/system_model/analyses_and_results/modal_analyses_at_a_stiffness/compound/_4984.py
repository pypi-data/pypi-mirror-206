"""_4984.py

CoaxialConnectionCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.connections_and_sockets import _2250
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4854
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5057
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'CoaxialConnectionCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionCompoundModalAnalysisAtAStiffness',)


class CoaxialConnectionCompoundModalAnalysisAtAStiffness(_5057.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness):
    """CoaxialConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CoaxialConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'CoaxialConnectionCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_5057.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4963
            
            return self._parent._cast(_4963.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness)

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
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5004
            
            return self._parent._cast(_5004.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(self) -> 'CoaxialConnectionCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2250.CoaxialConnection':
        """CoaxialConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2250.CoaxialConnection':
        """CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4854.CoaxialConnectionModalAnalysisAtAStiffness]':
        """List[CoaxialConnectionModalAnalysisAtAStiffness]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4854.CoaxialConnectionModalAnalysisAtAStiffness]':
        """List[CoaxialConnectionModalAnalysisAtAStiffness]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CoaxialConnectionCompoundModalAnalysisAtAStiffness._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness':
        return self._Cast_CoaxialConnectionCompoundModalAnalysisAtAStiffness(self)
