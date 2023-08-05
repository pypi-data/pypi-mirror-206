"""_2309.py

StraightBevelGearTeethSocket
"""
from mastapy.system_model.connections_and_sockets.gears import _2285
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'StraightBevelGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearTeethSocket',)


class StraightBevelGearTeethSocket(_2285.BevelGearTeethSocket):
    """StraightBevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_TEETH_SOCKET

    class _Cast_StraightBevelGearTeethSocket:
        """Special nested class for casting StraightBevelGearTeethSocket to subclasses."""

        def __init__(self, parent: 'StraightBevelGearTeethSocket'):
            self._parent = parent

        @property
        def bevel_gear_teeth_socket(self):
            return self._parent._cast(_2285.BevelGearTeethSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2281
            
            return self._parent._cast(_2281.AGMAGleasonConicalGearTeethSocket)

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
        def straight_bevel_gear_teeth_socket(self) -> 'StraightBevelGearTeethSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'StraightBevelGearTeethSocket._Cast_StraightBevelGearTeethSocket':
        return self._Cast_StraightBevelGearTeethSocket(self)
