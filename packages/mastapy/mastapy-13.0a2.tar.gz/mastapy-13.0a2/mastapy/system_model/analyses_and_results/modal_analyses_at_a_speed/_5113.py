"""_5113.py

CoaxialConnectionModalAnalysisAtASpeed
"""
from mastapy.system_model.connections_and_sockets import _2250
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6800
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5186
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'CoaxialConnectionModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionModalAnalysisAtASpeed',)


class CoaxialConnectionModalAnalysisAtASpeed(_5186.ShaftToMountableComponentConnectionModalAnalysisAtASpeed):
    """CoaxialConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_CoaxialConnectionModalAnalysisAtASpeed:
        """Special nested class for casting CoaxialConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'CoaxialConnectionModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5186.ShaftToMountableComponentConnectionModalAnalysisAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5092
            
            return self._parent._cast(_5092.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed)

        @property
        def connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5124
            
            return self._parent._cast(_5124.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7503
            
            return self._parent._cast(_7503.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7500
            
            return self._parent._cast(_7500.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2628
            
            return self._parent._cast(_2628.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5133
            
            return self._parent._cast(_5133.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed)

        @property
        def coaxial_connection_modal_analysis_at_a_speed(self) -> 'CoaxialConnectionModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self) -> '_6800.CoaxialConnectionLoadCase':
        """CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed':
        return self._Cast_CoaxialConnectionModalAnalysisAtASpeed(self)
