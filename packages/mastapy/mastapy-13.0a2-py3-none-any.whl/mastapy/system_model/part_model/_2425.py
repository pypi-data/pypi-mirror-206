"""_2425.py

ComponentsConnectedResult
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2426
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENTS_CONNECTED_RESULT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ComponentsConnectedResult')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentsConnectedResult',)


class ComponentsConnectedResult(_0.APIBase):
    """ComponentsConnectedResult

    This is a mastapy class.
    """

    TYPE = _COMPONENTS_CONNECTED_RESULT

    class _Cast_ComponentsConnectedResult:
        """Special nested class for casting ComponentsConnectedResult to subclasses."""

        def __init__(self, parent: 'ComponentsConnectedResult'):
            self._parent = parent

        @property
        def components_connected_result(self) -> 'ComponentsConnectedResult':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentsConnectedResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_failed(self) -> 'bool':
        """bool: 'ConnectionFailed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionFailed

        if temp is None:
            return False

        return temp

    @property
    def failure_message(self) -> 'str':
        """str: 'FailureMessage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FailureMessage

        if temp is None:
            return ''

        return temp

    @property
    def was_connection_created(self) -> 'bool':
        """bool: 'WasConnectionCreated' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WasConnectionCreated

        if temp is None:
            return False

        return temp

    @property
    def created_socket_connection(self) -> '_2426.ConnectedSockets':
        """ConnectedSockets: 'CreatedSocketConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CreatedSocketConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ComponentsConnectedResult._Cast_ComponentsConnectedResult':
        return self._Cast_ComponentsConnectedResult(self)
