"""_2333.py

TorqueConverterConnection
"""
from mastapy.system_model.connections_and_sockets.couplings import _2327
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'TorqueConverterConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnection',)


class TorqueConverterConnection(_2327.CouplingConnection):
    """TorqueConverterConnection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION

    class _Cast_TorqueConverterConnection:
        """Special nested class for casting TorqueConverterConnection to subclasses."""

        def __init__(self, parent: 'TorqueConverterConnection'):
            self._parent = parent

        @property
        def coupling_connection(self):
            return self._parent._cast(_2327.CouplingConnection)

        @property
        def inter_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2262
            
            return self._parent._cast(_2262.InterMountableComponentConnection)

        @property
        def connection(self):
            from mastapy.system_model.connections_and_sockets import _2253
            
            return self._parent._cast(_2253.Connection)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def torque_converter_connection(self) -> 'TorqueConverterConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TorqueConverterConnection._Cast_TorqueConverterConnection':
        return self._Cast_TorqueConverterConnection(self)
