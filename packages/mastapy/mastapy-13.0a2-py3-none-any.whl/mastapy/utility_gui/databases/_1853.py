"""_1853.py

DatabaseWithSelectedItem
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')


__docformat__ = 'restructuredtext en'
__all__ = ('DatabaseWithSelectedItem',)


class DatabaseWithSelectedItem(_0.APIBase):
    """DatabaseWithSelectedItem

    This is a mastapy class.
    """

    TYPE = _DATABASE_WITH_SELECTED_ITEM

    class _Cast_DatabaseWithSelectedItem:
        """Special nested class for casting DatabaseWithSelectedItem to subclasses."""

        def __init__(self, parent: 'DatabaseWithSelectedItem'):
            self._parent = parent

        @property
        def database_with_selected_item(self) -> 'DatabaseWithSelectedItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DatabaseWithSelectedItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def items(self) -> 'List[str]':
        """List[str]: 'Items' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Items

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    @property
    def selected_item_name(self) -> 'str':
        """str: 'SelectedItemName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedItemName

        if temp is None:
            return ''

        return temp

    def set_selected_item(self, item_name: 'str'):
        """ 'SetSelectedItem' is the original name of this method.

        Args:
            item_name (str)
        """

        item_name = str(item_name)
        self.wrapped.SetSelectedItem(item_name if item_name else '')

    @property
    def cast_to(self) -> 'DatabaseWithSelectedItem._Cast_DatabaseWithSelectedItem':
        return self._Cast_DatabaseWithSelectedItem(self)
