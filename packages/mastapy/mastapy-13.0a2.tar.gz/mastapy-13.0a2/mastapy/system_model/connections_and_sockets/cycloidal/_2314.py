"""_2314.py

CycloidalDiscAxialLeftSocket
"""
from mastapy.system_model.connections_and_sockets import _2261
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_AXIAL_LEFT_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'CycloidalDiscAxialLeftSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscAxialLeftSocket',)


class CycloidalDiscAxialLeftSocket(_2261.InnerShaftSocketBase):
    """CycloidalDiscAxialLeftSocket

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_AXIAL_LEFT_SOCKET

    class _Cast_CycloidalDiscAxialLeftSocket:
        """Special nested class for casting CycloidalDiscAxialLeftSocket to subclasses."""

        def __init__(self, parent: 'CycloidalDiscAxialLeftSocket'):
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
        def cycloidal_disc_axial_left_socket(self) -> 'CycloidalDiscAxialLeftSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscAxialLeftSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CycloidalDiscAxialLeftSocket._Cast_CycloidalDiscAxialLeftSocket':
        return self._Cast_CycloidalDiscAxialLeftSocket(self)
