"""_2317.py

CycloidalDiscInnerSocket
"""
from mastapy.system_model.connections_and_sockets import _2261
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_INNER_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'CycloidalDiscInnerSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscInnerSocket',)


class CycloidalDiscInnerSocket(_2261.InnerShaftSocketBase):
    """CycloidalDiscInnerSocket

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_INNER_SOCKET

    class _Cast_CycloidalDiscInnerSocket:
        """Special nested class for casting CycloidalDiscInnerSocket to subclasses."""

        def __init__(self, parent: 'CycloidalDiscInnerSocket'):
            self._parent = parent

        @property
        def inner_shaft_socket_base(self):
            return self._parent._cast(_2261.InnerShaftSocketBase)

        @property
        def shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2275
            
            return self._parent._cast(_2275.ShaftSocket)

        @property
        def cylindrical_socket(self):
            from mastapy.system_model.connections_and_sockets import _2257
            
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def cycloidal_disc_inner_socket(self) -> 'CycloidalDiscInnerSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscInnerSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CycloidalDiscInnerSocket._Cast_CycloidalDiscInnerSocket':
        return self._Cast_CycloidalDiscInnerSocket(self)
