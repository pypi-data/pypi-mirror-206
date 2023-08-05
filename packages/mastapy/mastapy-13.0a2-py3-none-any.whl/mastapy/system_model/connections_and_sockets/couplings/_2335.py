"""_2335.py

TorqueConverterTurbineSocket
"""
from mastapy.system_model.connections_and_sockets.couplings import _2328
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'TorqueConverterTurbineSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineSocket',)


class TorqueConverterTurbineSocket(_2328.CouplingSocket):
    """TorqueConverterTurbineSocket

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_SOCKET

    class _Cast_TorqueConverterTurbineSocket:
        """Special nested class for casting TorqueConverterTurbineSocket to subclasses."""

        def __init__(self, parent: 'TorqueConverterTurbineSocket'):
            self._parent = parent

        @property
        def coupling_socket(self):
            return self._parent._cast(_2328.CouplingSocket)

        @property
        def cylindrical_socket(self):
            from mastapy.system_model.connections_and_sockets import _2257
            
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def torque_converter_turbine_socket(self) -> 'TorqueConverterTurbineSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TorqueConverterTurbineSocket._Cast_TorqueConverterTurbineSocket':
        return self._Cast_TorqueConverterTurbineSocket(self)
