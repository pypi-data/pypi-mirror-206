"""_2247.py

BearingInnerSocket
"""
from mastapy.system_model.connections_and_sockets import _2263
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_INNER_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'BearingInnerSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingInnerSocket',)


class BearingInnerSocket(_2263.MountableComponentInnerSocket):
    """BearingInnerSocket

    This is a mastapy class.
    """

    TYPE = _BEARING_INNER_SOCKET

    class _Cast_BearingInnerSocket:
        """Special nested class for casting BearingInnerSocket to subclasses."""

        def __init__(self, parent: 'BearingInnerSocket'):
            self._parent = parent

        @property
        def mountable_component_inner_socket(self):
            return self._parent._cast(_2263.MountableComponentInnerSocket)

        @property
        def mountable_component_socket(self):
            from mastapy.system_model.connections_and_sockets import _2265
            
            return self._parent._cast(_2265.MountableComponentSocket)

        @property
        def cylindrical_socket(self):
            from mastapy.system_model.connections_and_sockets import _2257
            
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def bearing_inner_socket(self) -> 'BearingInnerSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingInnerSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BearingInnerSocket._Cast_BearingInnerSocket':
        return self._Cast_BearingInnerSocket(self)
