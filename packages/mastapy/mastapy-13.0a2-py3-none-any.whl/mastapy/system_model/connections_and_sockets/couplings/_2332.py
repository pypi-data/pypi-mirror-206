"""_2332.py

SpringDamperSocket
"""
from mastapy.system_model.connections_and_sockets.couplings import _2328
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'SpringDamperSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperSocket',)


class SpringDamperSocket(_2328.CouplingSocket):
    """SpringDamperSocket

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_SOCKET

    class _Cast_SpringDamperSocket:
        """Special nested class for casting SpringDamperSocket to subclasses."""

        def __init__(self, parent: 'SpringDamperSocket'):
            self._parent = parent

        @property
        def coupling_socket(self):
            return self._parent._cast(_2328.CouplingSocket)

        @property
        def cylindrical_socket(self):
            from mastapy.system_model.connections_and_sockets import _2257
            
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def spring_damper_socket(self) -> 'SpringDamperSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpringDamperSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SpringDamperSocket._Cast_SpringDamperSocket':
        return self._Cast_SpringDamperSocket(self)
