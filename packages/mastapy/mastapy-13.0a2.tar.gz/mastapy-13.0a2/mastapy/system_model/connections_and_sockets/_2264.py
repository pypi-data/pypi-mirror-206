"""_2264.py

MountableComponentOuterSocket
"""
from mastapy.system_model.connections_and_sockets import _2265
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_OUTER_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'MountableComponentOuterSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentOuterSocket',)


class MountableComponentOuterSocket(_2265.MountableComponentSocket):
    """MountableComponentOuterSocket

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_OUTER_SOCKET

    class _Cast_MountableComponentOuterSocket:
        """Special nested class for casting MountableComponentOuterSocket to subclasses."""

        def __init__(self, parent: 'MountableComponentOuterSocket'):
            self._parent = parent

        @property
        def mountable_component_socket(self):
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
        def bearing_outer_socket(self):
            from mastapy.system_model.connections_and_sockets import _2248
            
            return self._parent._cast(_2248.BearingOuterSocket)

        @property
        def mountable_component_outer_socket(self) -> 'MountableComponentOuterSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentOuterSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MountableComponentOuterSocket._Cast_MountableComponentOuterSocket':
        return self._Cast_MountableComponentOuterSocket(self)
