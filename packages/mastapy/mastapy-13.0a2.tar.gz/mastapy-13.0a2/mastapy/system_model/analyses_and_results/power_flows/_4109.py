"""_4109.py

ShaftToMountableComponentConnectionPowerFlow
"""
from mastapy.system_model.connections_and_sockets import _2276
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4012
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ShaftToMountableComponentConnectionPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnectionPowerFlow',)


class ShaftToMountableComponentConnectionPowerFlow(_4012.AbstractShaftToMountableComponentConnectionPowerFlow):
    """ShaftToMountableComponentConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW

    class _Cast_ShaftToMountableComponentConnectionPowerFlow:
        """Special nested class for casting ShaftToMountableComponentConnectionPowerFlow to subclasses."""

        def __init__(self, parent: 'ShaftToMountableComponentConnectionPowerFlow'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(self):
            return self._parent._cast(_4012.AbstractShaftToMountableComponentConnectionPowerFlow)

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
        def coaxial_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4033
            
            return self._parent._cast(_4033.CoaxialConnectionPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4053
            
            return self._parent._cast(_4053.CycloidalDiscCentralBearingConnectionPowerFlow)

        @property
        def planetary_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4093
            
            return self._parent._cast(_4093.PlanetaryConnectionPowerFlow)

        @property
        def shaft_to_mountable_component_connection_power_flow(self) -> 'ShaftToMountableComponentConnectionPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2276.ShaftToMountableComponentConnection':
        """ShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow':
        return self._Cast_ShaftToMountableComponentConnectionPowerFlow(self)
