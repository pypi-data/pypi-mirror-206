"""_1771.py

DynamicCustomReportItem
"""
from mastapy._internal import constructor
from mastapy.utility.report import _1752, _1760
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_CUSTOM_REPORT_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'DynamicCustomReportItem')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicCustomReportItem',)


class DynamicCustomReportItem(_1760.CustomReportNameableItem):
    """DynamicCustomReportItem

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_CUSTOM_REPORT_ITEM

    class _Cast_DynamicCustomReportItem:
        """Special nested class for casting DynamicCustomReportItem to subclasses."""

        def __init__(self, parent: 'DynamicCustomReportItem'):
            self._parent = parent

        @property
        def custom_report_nameable_item(self):
            return self._parent._cast(_1760.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def dynamic_custom_report_item(self) -> 'DynamicCustomReportItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicCustomReportItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_main_report_item(self) -> 'bool':
        """bool: 'IsMainReportItem' is the original name of this property."""

        temp = self.wrapped.IsMainReportItem

        if temp is None:
            return False

        return temp

    @is_main_report_item.setter
    def is_main_report_item(self, value: 'bool'):
        self.wrapped.IsMainReportItem = bool(value) if value else False

    @property
    def inner_item(self) -> '_1752.CustomReportItem':
        """CustomReportItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'DynamicCustomReportItem._Cast_DynamicCustomReportItem':
        return self._Cast_DynamicCustomReportItem(self)
