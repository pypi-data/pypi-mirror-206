"""_2285.py

BevelGearTeethSocket
"""
from mastapy.system_model.connections_and_sockets.gears import _2281
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearTeethSocket',)


class BevelGearTeethSocket(_2281.AGMAGleasonConicalGearTeethSocket):
    """BevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_TEETH_SOCKET

    class _Cast_BevelGearTeethSocket:
        """Special nested class for casting BevelGearTeethSocket to subclasses."""

        def __init__(self, parent: 'BevelGearTeethSocket'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_teeth_socket(self):
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
        def bevel_differential_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2283
            
            return self._parent._cast(_2283.BevelDifferentialGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2305
            
            return self._parent._cast(_2305.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2307
            
            return self._parent._cast(_2307.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2309
            
            return self._parent._cast(_2309.StraightBevelGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2313
            
            return self._parent._cast(_2313.ZerolBevelGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(self) -> 'BevelGearTeethSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelGearTeethSocket._Cast_BevelGearTeethSocket':
        return self._Cast_BevelGearTeethSocket(self)
