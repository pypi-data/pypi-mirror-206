"""_2276.py

ShaftToMountableComponentConnection
"""
from mastapy.system_model.connections_and_sockets import _2246
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ShaftToMountableComponentConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnection',)


class ShaftToMountableComponentConnection(_2246.AbstractShaftToMountableComponentConnection):
    """ShaftToMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION

    class _Cast_ShaftToMountableComponentConnection:
        """Special nested class for casting ShaftToMountableComponentConnection to subclasses."""

        def __init__(self, parent: 'ShaftToMountableComponentConnection'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection(self):
            return self._parent._cast(_2246.AbstractShaftToMountableComponentConnection)

        @property
        def connection(self):
            from mastapy.system_model.connections_and_sockets import _2253
            
            return self._parent._cast(_2253.Connection)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def coaxial_connection(self):
            from mastapy.system_model.connections_and_sockets import _2250
            
            return self._parent._cast(_2250.CoaxialConnection)

        @property
        def planetary_connection(self):
            from mastapy.system_model.connections_and_sockets import _2268
            
            return self._parent._cast(_2268.PlanetaryConnection)

        @property
        def cycloidal_disc_central_bearing_connection(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2316
            
            return self._parent._cast(_2316.CycloidalDiscCentralBearingConnection)

        @property
        def shaft_to_mountable_component_connection(self) -> 'ShaftToMountableComponentConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection':
        return self._Cast_ShaftToMountableComponentConnection(self)
