"""_2266.py

OuterShaftSocket
"""
from mastapy.system_model.connections_and_sockets import _2267
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OUTER_SHAFT_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'OuterShaftSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('OuterShaftSocket',)


class OuterShaftSocket(_2267.OuterShaftSocketBase):
    """OuterShaftSocket

    This is a mastapy class.
    """

    TYPE = _OUTER_SHAFT_SOCKET

    class _Cast_OuterShaftSocket:
        """Special nested class for casting OuterShaftSocket to subclasses."""

        def __init__(self, parent: 'OuterShaftSocket'):
            self._parent = parent

        @property
        def outer_shaft_socket_base(self):
            return self._parent._cast(_2267.OuterShaftSocketBase)

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
        def outer_shaft_socket(self) -> 'OuterShaftSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OuterShaftSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'OuterShaftSocket._Cast_OuterShaftSocket':
        return self._Cast_OuterShaftSocket(self)
