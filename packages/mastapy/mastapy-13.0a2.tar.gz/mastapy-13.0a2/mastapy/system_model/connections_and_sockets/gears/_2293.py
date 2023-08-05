"""_2293.py

FaceGearTeethSocket
"""
from mastapy.system_model.connections_and_sockets.gears import _2295
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'FaceGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearTeethSocket',)


class FaceGearTeethSocket(_2295.GearTeethSocket):
    """FaceGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_TEETH_SOCKET

    class _Cast_FaceGearTeethSocket:
        """Special nested class for casting FaceGearTeethSocket to subclasses."""

        def __init__(self, parent: 'FaceGearTeethSocket'):
            self._parent = parent

        @property
        def gear_teeth_socket(self):
            return self._parent._cast(_2295.GearTeethSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def face_gear_teeth_socket(self) -> 'FaceGearTeethSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FaceGearTeethSocket._Cast_FaceGearTeethSocket':
        return self._Cast_FaceGearTeethSocket(self)
