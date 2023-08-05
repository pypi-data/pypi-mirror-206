"""_2249.py

BeltConnection
"""
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2262
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'BeltConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnection',)


class BeltConnection(_2262.InterMountableComponentConnection):
    """BeltConnection

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION

    class _Cast_BeltConnection:
        """Special nested class for casting BeltConnection to subclasses."""

        def __init__(self, parent: 'BeltConnection'):
            self._parent = parent

        @property
        def inter_mountable_component_connection(self):
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
        def cvt_belt_connection(self):
            from mastapy.system_model.connections_and_sockets import _2254
            
            return self._parent._cast(_2254.CVTBeltConnection)

        @property
        def belt_connection(self) -> 'BeltConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stiffness_of_strand(self) -> 'float':
        """float: 'StiffnessOfStrand' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessOfStrand

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'BeltConnection._Cast_BeltConnection':
        return self._Cast_BeltConnection(self)
