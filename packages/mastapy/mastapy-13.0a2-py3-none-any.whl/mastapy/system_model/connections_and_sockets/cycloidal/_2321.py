"""_2321.py

RingPinsSocket
"""
from mastapy.system_model.connections_and_sockets import _2257
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'RingPinsSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsSocket',)


class RingPinsSocket(_2257.CylindricalSocket):
    """RingPinsSocket

    This is a mastapy class.
    """

    TYPE = _RING_PINS_SOCKET

    class _Cast_RingPinsSocket:
        """Special nested class for casting RingPinsSocket to subclasses."""

        def __init__(self, parent: 'RingPinsSocket'):
            self._parent = parent

        @property
        def cylindrical_socket(self):
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def ring_pins_socket(self) -> 'RingPinsSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingPinsSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RingPinsSocket._Cast_RingPinsSocket':
        return self._Cast_RingPinsSocket(self)
