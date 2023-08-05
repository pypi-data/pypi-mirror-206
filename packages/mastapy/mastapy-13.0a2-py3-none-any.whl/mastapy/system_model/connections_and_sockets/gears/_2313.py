"""_2313.py

ZerolBevelGearTeethSocket
"""
from mastapy.system_model.connections_and_sockets.gears import _2285
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ZerolBevelGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearTeethSocket',)


class ZerolBevelGearTeethSocket(_2285.BevelGearTeethSocket):
    """ZerolBevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_TEETH_SOCKET

    class _Cast_ZerolBevelGearTeethSocket:
        """Special nested class for casting ZerolBevelGearTeethSocket to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearTeethSocket'):
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
        def zerol_bevel_gear_teeth_socket(self) -> 'ZerolBevelGearTeethSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ZerolBevelGearTeethSocket._Cast_ZerolBevelGearTeethSocket':
        return self._Cast_ZerolBevelGearTeethSocket(self)
