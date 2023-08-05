"""_2330.py

PartToPartShearCouplingSocket
"""
from mastapy.system_model.connections_and_sockets.couplings import _2328
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'PartToPartShearCouplingSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingSocket',)


class PartToPartShearCouplingSocket(_2328.CouplingSocket):
    """PartToPartShearCouplingSocket

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_SOCKET

    class _Cast_PartToPartShearCouplingSocket:
        """Special nested class for casting PartToPartShearCouplingSocket to subclasses."""

        def __init__(self, parent: 'PartToPartShearCouplingSocket'):
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
        def part_to_part_shear_coupling_socket(self) -> 'PartToPartShearCouplingSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PartToPartShearCouplingSocket._Cast_PartToPartShearCouplingSocket':
        return self._Cast_PartToPartShearCouplingSocket(self)
