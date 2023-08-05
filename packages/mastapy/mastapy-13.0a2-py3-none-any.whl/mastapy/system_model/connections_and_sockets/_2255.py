"""_2255.py

CVTPulleySocket
"""
from mastapy.system_model.connections_and_sockets import _2271
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CVTPulleySocket')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleySocket',)


class CVTPulleySocket(_2271.PulleySocket):
    """CVTPulleySocket

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_SOCKET

    class _Cast_CVTPulleySocket:
        """Special nested class for casting CVTPulleySocket to subclasses."""

        def __init__(self, parent: 'CVTPulleySocket'):
            self._parent = parent

        @property
        def pulley_socket(self):
            return self._parent._cast(_2271.PulleySocket)

        @property
        def cylindrical_socket(self):
            from mastapy.system_model.connections_and_sockets import _2257
            
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def cvt_pulley_socket(self) -> 'CVTPulleySocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTPulleySocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CVTPulleySocket._Cast_CVTPulleySocket':
        return self._Cast_CVTPulleySocket(self)
