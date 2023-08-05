"""_2291.py

CylindricalGearTeethSocket
"""
from mastapy.system_model.connections_and_sockets import _2257
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'CylindricalGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearTeethSocket',)


class CylindricalGearTeethSocket(_2257.CylindricalSocket):
    """CylindricalGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TEETH_SOCKET

    class _Cast_CylindricalGearTeethSocket:
        """Special nested class for casting CylindricalGearTeethSocket to subclasses."""

        def __init__(self, parent: 'CylindricalGearTeethSocket'):
            self._parent = parent

        @property
        def cylindrical_socket(self):
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def cylindrical_gear_teeth_socket(self) -> 'CylindricalGearTeethSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearTeethSocket._Cast_CylindricalGearTeethSocket':
        return self._Cast_CylindricalGearTeethSocket(self)
