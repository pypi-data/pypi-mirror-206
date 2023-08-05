"""_2261.py

InnerShaftSocketBase
"""
from mastapy.system_model.connections_and_sockets import _2275
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INNER_SHAFT_SOCKET_BASE = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'InnerShaftSocketBase')


__docformat__ = 'restructuredtext en'
__all__ = ('InnerShaftSocketBase',)


class InnerShaftSocketBase(_2275.ShaftSocket):
    """InnerShaftSocketBase

    This is a mastapy class.
    """

    TYPE = _INNER_SHAFT_SOCKET_BASE

    class _Cast_InnerShaftSocketBase:
        """Special nested class for casting InnerShaftSocketBase to subclasses."""

        def __init__(self, parent: 'InnerShaftSocketBase'):
            self._parent = parent

        @property
        def shaft_socket(self):
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
        def inner_shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2260
            
            return self._parent._cast(_2260.InnerShaftSocket)

        @property
        def cycloidal_disc_axial_left_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2314
            
            return self._parent._cast(_2314.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_inner_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2317
            
            return self._parent._cast(_2317.CycloidalDiscInnerSocket)

        @property
        def inner_shaft_socket_base(self) -> 'InnerShaftSocketBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InnerShaftSocketBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'InnerShaftSocketBase._Cast_InnerShaftSocketBase':
        return self._Cast_InnerShaftSocketBase(self)
