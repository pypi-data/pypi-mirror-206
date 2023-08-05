"""_2320.py

CycloidalDiscPlanetaryBearingSocket
"""
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2270
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'CycloidalDiscPlanetaryBearingSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscPlanetaryBearingSocket',)


class CycloidalDiscPlanetaryBearingSocket(_2270.PlanetarySocketBase):
    """CycloidalDiscPlanetaryBearingSocket

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_SOCKET

    class _Cast_CycloidalDiscPlanetaryBearingSocket:
        """Special nested class for casting CycloidalDiscPlanetaryBearingSocket to subclasses."""

        def __init__(self, parent: 'CycloidalDiscPlanetaryBearingSocket'):
            self._parent = parent

        @property
        def planetary_socket_base(self):
            return self._parent._cast(_2270.PlanetarySocketBase)

        @property
        def cylindrical_socket(self):
            from mastapy.system_model.connections_and_sockets import _2257
            
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def cycloidal_disc_planetary_bearing_socket(self) -> 'CycloidalDiscPlanetaryBearingSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscPlanetaryBearingSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_for_eccentric_bearing(self) -> 'bool':
        """bool: 'IsForEccentricBearing' is the original name of this property."""

        temp = self.wrapped.IsForEccentricBearing

        if temp is None:
            return False

        return temp

    @is_for_eccentric_bearing.setter
    def is_for_eccentric_bearing(self, value: 'bool'):
        self.wrapped.IsForEccentricBearing = bool(value) if value else False

    @property
    def cast_to(self) -> 'CycloidalDiscPlanetaryBearingSocket._Cast_CycloidalDiscPlanetaryBearingSocket':
        return self._Cast_CycloidalDiscPlanetaryBearingSocket(self)
