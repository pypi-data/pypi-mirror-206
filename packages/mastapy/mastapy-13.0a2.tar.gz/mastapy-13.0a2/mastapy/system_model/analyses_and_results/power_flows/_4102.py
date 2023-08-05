"""_4102.py

RingPinsToDiscConnectionPowerFlow
"""
from mastapy.system_model.connections_and_sockets.cycloidal import _2322
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6908
from mastapy.system_model.analyses_and_results.power_flows import _4075
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'RingPinsToDiscConnectionPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsToDiscConnectionPowerFlow',)


class RingPinsToDiscConnectionPowerFlow(_4075.InterMountableComponentConnectionPowerFlow):
    """RingPinsToDiscConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_POWER_FLOW

    class _Cast_RingPinsToDiscConnectionPowerFlow:
        """Special nested class for casting RingPinsToDiscConnectionPowerFlow to subclasses."""

        def __init__(self, parent: 'RingPinsToDiscConnectionPowerFlow'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_power_flow(self):
            return self._parent._cast(_4075.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4044
            
            return self._parent._cast(_4044.ConnectionPowerFlow)

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
        def ring_pins_to_disc_connection_power_flow(self) -> 'RingPinsToDiscConnectionPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingPinsToDiscConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2322.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6908.RingPinsToDiscConnectionLoadCase':
        """RingPinsToDiscConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow':
        return self._Cast_RingPinsToDiscConnectionPowerFlow(self)
