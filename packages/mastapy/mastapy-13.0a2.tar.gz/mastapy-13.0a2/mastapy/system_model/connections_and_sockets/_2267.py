"""_2267.py

OuterShaftSocketBase
"""
from mastapy.system_model.connections_and_sockets import _2275
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OUTER_SHAFT_SOCKET_BASE = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'OuterShaftSocketBase')


__docformat__ = 'restructuredtext en'
__all__ = ('OuterShaftSocketBase',)


class OuterShaftSocketBase(_2275.ShaftSocket):
    """OuterShaftSocketBase

    This is a mastapy class.
    """

    TYPE = _OUTER_SHAFT_SOCKET_BASE

    class _Cast_OuterShaftSocketBase:
        """Special nested class for casting OuterShaftSocketBase to subclasses."""

        def __init__(self, parent: 'OuterShaftSocketBase'):
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
        def outer_shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2266
            
            return self._parent._cast(_2266.OuterShaftSocket)

        @property
        def cycloidal_disc_axial_right_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2315
            
            return self._parent._cast(_2315.CycloidalDiscAxialRightSocket)

        @property
        def outer_shaft_socket_base(self) -> 'OuterShaftSocketBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OuterShaftSocketBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'OuterShaftSocketBase._Cast_OuterShaftSocketBase':
        return self._Cast_OuterShaftSocketBase(self)
