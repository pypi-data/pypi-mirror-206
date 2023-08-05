"""_1804.py

ColumnTitle
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COLUMN_TITLE = python_net_import('SMT.MastaAPI.Utility.FileAccessHelpers', 'ColumnTitle')


__docformat__ = 'restructuredtext en'
__all__ = ('ColumnTitle',)


class ColumnTitle(_0.APIBase):
    """ColumnTitle

    This is a mastapy class.
    """

    TYPE = _COLUMN_TITLE

    class _Cast_ColumnTitle:
        """Special nested class for casting ColumnTitle to subclasses."""

        def __init__(self, parent: 'ColumnTitle'):
            self._parent = parent

        @property
        def column_title(self) -> 'ColumnTitle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ColumnTitle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def column_number(self) -> 'int':
        """int: 'ColumnNumber' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ColumnNumber

        if temp is None:
            return 0

        return temp

    @property
    def title(self) -> 'str':
        """str: 'Title' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Title

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'ColumnTitle._Cast_ColumnTitle':
        return self._Cast_ColumnTitle(self)
