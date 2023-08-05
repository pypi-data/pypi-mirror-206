"""_2259.py

ElectricMachineStatorSocket
"""
from mastapy.system_model.connections_and_sockets import _2277
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_STATOR_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ElectricMachineStatorSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineStatorSocket',)


class ElectricMachineStatorSocket(_2277.Socket):
    """ElectricMachineStatorSocket

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_STATOR_SOCKET

    class _Cast_ElectricMachineStatorSocket:
        """Special nested class for casting ElectricMachineStatorSocket to subclasses."""

        def __init__(self, parent: 'ElectricMachineStatorSocket'):
            self._parent = parent

        @property
        def socket(self):
            return self._parent._cast(_2277.Socket)

        @property
        def electric_machine_stator_socket(self) -> 'ElectricMachineStatorSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineStatorSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineStatorSocket._Cast_ElectricMachineStatorSocket':
        return self._Cast_ElectricMachineStatorSocket(self)
