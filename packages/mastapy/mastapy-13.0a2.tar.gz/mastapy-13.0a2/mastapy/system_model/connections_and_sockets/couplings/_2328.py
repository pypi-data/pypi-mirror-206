"""_2328.py

CouplingSocket
"""
from mastapy.system_model.connections_and_sockets import _2257
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'CouplingSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingSocket',)


class CouplingSocket(_2257.CylindricalSocket):
    """CouplingSocket

    This is a mastapy class.
    """

    TYPE = _COUPLING_SOCKET

    class _Cast_CouplingSocket:
        """Special nested class for casting CouplingSocket to subclasses."""

        def __init__(self, parent: 'CouplingSocket'):
            self._parent = parent

        @property
        def cylindrical_socket(self):
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.Socket)

        @property
        def clutch_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2324
            
            return self._parent._cast(_2324.ClutchSocket)

        @property
        def concept_coupling_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2326
            
            return self._parent._cast(_2326.ConceptCouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2330
            
            return self._parent._cast(_2330.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2332
            
            return self._parent._cast(_2332.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2334
            
            return self._parent._cast(_2334.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2335
            
            return self._parent._cast(_2335.TorqueConverterTurbineSocket)

        @property
        def coupling_socket(self) -> 'CouplingSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CouplingSocket._Cast_CouplingSocket':
        return self._Cast_CouplingSocket(self)
