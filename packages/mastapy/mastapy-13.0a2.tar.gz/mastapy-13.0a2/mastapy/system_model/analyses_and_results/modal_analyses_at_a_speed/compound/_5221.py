"""_5221.py

AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5092
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5253
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed',)


class AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed(_5253.ConnectionCompoundModalAnalysisAtASpeed):
    """AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def connection_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5253.ConnectionCompoundModalAnalysisAtASpeed)

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
        def coaxial_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5242
            
            return self._parent._cast(_5242.CoaxialConnectionCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5262
            
            return self._parent._cast(_5262.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5264
            
            return self._parent._cast(_5264.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def planetary_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5301
            
            return self._parent._cast(_5301.PlanetaryConnectionCompoundModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5315
            
            return self._parent._cast(_5315.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(self) -> 'AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_5092.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed]':
        """List[AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5092.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed]':
        """List[AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed':
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed(self)
