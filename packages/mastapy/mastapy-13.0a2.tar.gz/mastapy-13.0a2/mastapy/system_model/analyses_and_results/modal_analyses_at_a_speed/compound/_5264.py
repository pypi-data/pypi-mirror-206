"""_5264.py

CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.connections_and_sockets.cycloidal import _2319
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5135
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5221
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed',)


class CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed(_5221.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed):
    """CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5221.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5253
            
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
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_speed(self) -> 'CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2319.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2319.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5135.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed]':
        """List[CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5135.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed]':
        """List[CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed':
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed(self)
