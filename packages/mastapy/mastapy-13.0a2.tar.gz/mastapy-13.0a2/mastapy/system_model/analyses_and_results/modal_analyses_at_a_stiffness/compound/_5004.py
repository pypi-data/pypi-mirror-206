"""_5004.py

CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4874
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4984
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness',)


class CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness(_4984.CoaxialConnectionCompoundModalAnalysisAtAStiffness):
    """CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4984.CoaxialConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5057
            
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
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(self) -> 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4874.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness]':
        """List[CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4874.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness]':
        """List[CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness':
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness(self)
