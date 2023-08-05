"""_2274.py

RollingRingSocket
"""
from mastapy.system_model.connections_and_sockets import _2257
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'RollingRingSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingSocket',)


class RollingRingSocket(_2257.CylindricalSocket):
    """RollingRingSocket

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_SOCKET

    class _Cast_RollingRingSocket:
        """Special nested class for casting RollingRingSocket to subclasses."""

        def __init__(self, parent: 'RollingRingSocket'):
            self._parent = parent

        @property
        def cylindrical_socket(self):
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def rolling_ring_socket(self) -> 'RollingRingSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingRingSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RollingRingSocket._Cast_RollingRingSocket':
        return self._Cast_RollingRingSocket(self)
