"""_2265.py

MountableComponentSocket
"""
from mastapy.system_model.connections_and_sockets import _2257
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'MountableComponentSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentSocket',)


class MountableComponentSocket(_2257.CylindricalSocket):
    """MountableComponentSocket

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_SOCKET

    class _Cast_MountableComponentSocket:
        """Special nested class for casting MountableComponentSocket to subclasses."""

        def __init__(self, parent: 'MountableComponentSocket'):
            self._parent = parent

        @property
        def cylindrical_socket(self):
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def bearing_inner_socket(self):
            from mastapy.system_model.connections_and_sockets import _2247
            
            return self._parent._cast(_2247.BearingInnerSocket)

        @property
        def bearing_outer_socket(self):
            from mastapy.system_model.connections_and_sockets import _2248
            
            return self._parent._cast(_2248.BearingOuterSocket)

        @property
        def mountable_component_inner_socket(self):
            from mastapy.system_model.connections_and_sockets import _2263
            
            return self._parent._cast(_2263.MountableComponentInnerSocket)

        @property
        def mountable_component_outer_socket(self):
            from mastapy.system_model.connections_and_sockets import _2264
            
            return self._parent._cast(_2264.MountableComponentOuterSocket)

        @property
        def mountable_component_socket(self) -> 'MountableComponentSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MountableComponentSocket._Cast_MountableComponentSocket':
        return self._Cast_MountableComponentSocket(self)
