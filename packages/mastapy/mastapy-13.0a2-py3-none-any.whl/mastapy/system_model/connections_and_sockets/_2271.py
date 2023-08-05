"""_2271.py

PulleySocket
"""
from mastapy.system_model.connections_and_sockets import _2257
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'PulleySocket')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleySocket',)


class PulleySocket(_2257.CylindricalSocket):
    """PulleySocket

    This is a mastapy class.
    """

    TYPE = _PULLEY_SOCKET

    class _Cast_PulleySocket:
        """Special nested class for casting PulleySocket to subclasses."""

        def __init__(self, parent: 'PulleySocket'):
            self._parent = parent

        @property
        def cylindrical_socket(self):
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def cvt_pulley_socket(self):
            from mastapy.system_model.connections_and_sockets import _2255
            
            return self._parent._cast(_2255.CVTPulleySocket)

        @property
        def pulley_socket(self) -> 'PulleySocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PulleySocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PulleySocket._Cast_PulleySocket':
        return self._Cast_PulleySocket(self)
