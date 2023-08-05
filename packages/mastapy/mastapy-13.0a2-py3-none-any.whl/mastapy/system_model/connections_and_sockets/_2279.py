"""_2279.py

SocketConnectionSelection
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SOCKET_CONNECTION_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'SocketConnectionSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('SocketConnectionSelection',)


class SocketConnectionSelection(_0.APIBase):
    """SocketConnectionSelection

    This is a mastapy class.
    """

    TYPE = _SOCKET_CONNECTION_SELECTION

    class _Cast_SocketConnectionSelection:
        """Special nested class for casting SocketConnectionSelection to subclasses."""

        def __init__(self, parent: 'SocketConnectionSelection'):
            self._parent = parent

        @property
        def socket_connection_selection(self) -> 'SocketConnectionSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SocketConnectionSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    def select(self):
        """ 'Select' is the original name of this method."""

        self.wrapped.Select()

    @property
    def cast_to(self) -> 'SocketConnectionSelection._Cast_SocketConnectionSelection':
        return self._Cast_SocketConnectionSelection(self)
