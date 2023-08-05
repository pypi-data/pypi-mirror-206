"""_2275.py

ShaftSocket
"""
from mastapy.system_model.connections_and_sockets import _2257
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ShaftSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftSocket',)


class ShaftSocket(_2257.CylindricalSocket):
    """ShaftSocket

    This is a mastapy class.
    """

    TYPE = _SHAFT_SOCKET

    class _Cast_ShaftSocket:
        """Special nested class for casting ShaftSocket to subclasses."""

        def __init__(self, parent: 'ShaftSocket'):
            self._parent = parent

        @property
        def cylindrical_socket(self):
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def inner_shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2260
            
            return self._parent._cast(_2260.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(self):
            from mastapy.system_model.connections_and_sockets import _2261
            
            return self._parent._cast(_2261.InnerShaftSocketBase)

        @property
        def outer_shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2266
            
            return self._parent._cast(_2266.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(self):
            from mastapy.system_model.connections_and_sockets import _2267
            
            return self._parent._cast(_2267.OuterShaftSocketBase)

        @property
        def cycloidal_disc_axial_left_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2314
            
            return self._parent._cast(_2314.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2315
            
            return self._parent._cast(_2315.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2317
            
            return self._parent._cast(_2317.CycloidalDiscInnerSocket)

        @property
        def shaft_socket(self) -> 'ShaftSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShaftSocket._Cast_ShaftSocket':
        return self._Cast_ShaftSocket(self)
