"""_2334.py

TorqueConverterPumpSocket
"""
from mastapy.system_model.connections_and_sockets.couplings import _2328
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'TorqueConverterPumpSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpSocket',)


class TorqueConverterPumpSocket(_2328.CouplingSocket):
    """TorqueConverterPumpSocket

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_SOCKET

    class _Cast_TorqueConverterPumpSocket:
        """Special nested class for casting TorqueConverterPumpSocket to subclasses."""

        def __init__(self, parent: 'TorqueConverterPumpSocket'):
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
        def torque_converter_pump_socket(self) -> 'TorqueConverterPumpSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TorqueConverterPumpSocket._Cast_TorqueConverterPumpSocket':
        return self._Cast_TorqueConverterPumpSocket(self)
