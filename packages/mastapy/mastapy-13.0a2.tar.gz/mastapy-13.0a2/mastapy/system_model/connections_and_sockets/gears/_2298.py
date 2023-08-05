"""_2298.py

KlingelnbergConicalGearTeethSocket
"""
from mastapy.system_model.connections_and_sockets.gears import _2289
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergConicalGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergConicalGearTeethSocket',)


class KlingelnbergConicalGearTeethSocket(_2289.ConicalGearTeethSocket):
    """KlingelnbergConicalGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_GEAR_TEETH_SOCKET

    class _Cast_KlingelnbergConicalGearTeethSocket:
        """Special nested class for casting KlingelnbergConicalGearTeethSocket to subclasses."""

        def __init__(self, parent: 'KlingelnbergConicalGearTeethSocket'):
            self._parent = parent

        @property
        def conical_gear_teeth_socket(self):
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
        def klingelnberg_hypoid_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2302
            
            return self._parent._cast(_2302.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2303
            
            return self._parent._cast(_2303.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(self) -> 'KlingelnbergConicalGearTeethSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergConicalGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergConicalGearTeethSocket._Cast_KlingelnbergConicalGearTeethSocket':
        return self._Cast_KlingelnbergConicalGearTeethSocket(self)
