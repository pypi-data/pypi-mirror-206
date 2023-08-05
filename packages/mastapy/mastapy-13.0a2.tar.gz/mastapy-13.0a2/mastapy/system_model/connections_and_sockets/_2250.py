"""_2250.py

CoaxialConnection
"""
from mastapy.system_model.connections_and_sockets import _2276
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CoaxialConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnection',)


class CoaxialConnection(_2276.ShaftToMountableComponentConnection):
    """CoaxialConnection

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION

    class _Cast_CoaxialConnection:
        """Special nested class for casting CoaxialConnection to subclasses."""

        def __init__(self, parent: 'CoaxialConnection'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection(self):
            return self._parent._cast(_2276.ShaftToMountableComponentConnection)

        @property
        def abstract_shaft_to_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2246
            
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
        def cycloidal_disc_central_bearing_connection(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2316
            
            return self._parent._cast(_2316.CycloidalDiscCentralBearingConnection)

        @property
        def coaxial_connection(self) -> 'CoaxialConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CoaxialConnection._Cast_CoaxialConnection':
        return self._Cast_CoaxialConnection(self)
