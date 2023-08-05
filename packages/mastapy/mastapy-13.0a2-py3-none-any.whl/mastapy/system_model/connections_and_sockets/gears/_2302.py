"""_2302.py

KlingelnbergHypoidGearTeethSocket
"""
from mastapy.system_model.connections_and_sockets.gears import _2298
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_HYPOID_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergHypoidGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergHypoidGearTeethSocket',)


class KlingelnbergHypoidGearTeethSocket(_2298.KlingelnbergConicalGearTeethSocket):
    """KlingelnbergHypoidGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_HYPOID_GEAR_TEETH_SOCKET

    class _Cast_KlingelnbergHypoidGearTeethSocket:
        """Special nested class for casting KlingelnbergHypoidGearTeethSocket to subclasses."""

        def __init__(self, parent: 'KlingelnbergHypoidGearTeethSocket'):
            self._parent = parent

        @property
        def klingelnberg_conical_gear_teeth_socket(self):
            return self._parent._cast(_2298.KlingelnbergConicalGearTeethSocket)

        @property
        def conical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2289
            
            return self._parent._cast(_2289.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2295
            
            return self._parent._cast(_2295.GearTeethSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(self) -> 'KlingelnbergHypoidGearTeethSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergHypoidGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergHypoidGearTeethSocket._Cast_KlingelnbergHypoidGearTeethSocket':
        return self._Cast_KlingelnbergHypoidGearTeethSocket(self)
