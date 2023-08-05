"""_2323.py

ClutchConnection
"""
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.couplings import _2327
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ClutchConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnection',)


class ClutchConnection(_2327.CouplingConnection):
    """ClutchConnection

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION

    class _Cast_ClutchConnection:
        """Special nested class for casting ClutchConnection to subclasses."""

        def __init__(self, parent: 'ClutchConnection'):
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
        def clutch_connection(self) -> 'ClutchConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_torque_radius(self) -> 'float':
        """float: 'EffectiveTorqueRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveTorqueRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_capacity(self) -> 'float':
        """float: 'TorqueCapacity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueCapacity

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ClutchConnection._Cast_ClutchConnection':
        return self._Cast_ClutchConnection(self)
