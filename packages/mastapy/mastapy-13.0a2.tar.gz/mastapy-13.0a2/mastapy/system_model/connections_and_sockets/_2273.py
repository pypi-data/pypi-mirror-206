"""_2273.py

RollingRingConnection
"""
from mastapy.system_model.connections_and_sockets import _2262
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'RollingRingConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingConnection',)


class RollingRingConnection(_2262.InterMountableComponentConnection):
    """RollingRingConnection

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION

    class _Cast_RollingRingConnection:
        """Special nested class for casting RollingRingConnection to subclasses."""

        def __init__(self, parent: 'RollingRingConnection'):
            self._parent = parent

        @property
        def inter_mountable_component_connection(self):
            return self._parent._cast(_2262.InterMountableComponentConnection)

        @property
        def connection(self):
            from mastapy.system_model.connections_and_sockets import _2253
            
            return self._parent._cast(_2253.Connection)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def rolling_ring_connection(self) -> 'RollingRingConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingRingConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RollingRingConnection._Cast_RollingRingConnection':
        return self._Cast_RollingRingConnection(self)
