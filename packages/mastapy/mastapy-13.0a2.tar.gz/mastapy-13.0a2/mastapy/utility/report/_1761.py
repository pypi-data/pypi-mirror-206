"""_1761.py

CustomReportNamedItem
"""
from mastapy.utility.report import _1760
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_NAMED_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportNamedItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportNamedItem',)


class CustomReportNamedItem(_1760.CustomReportNameableItem):
    """CustomReportNamedItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_NAMED_ITEM

    class _Cast_CustomReportNamedItem:
        """Special nested class for casting CustomReportNamedItem to subclasses."""

        def __init__(self, parent: 'CustomReportNamedItem'):
            self._parent = parent

        @property
        def custom_report_nameable_item(self):
            return self._parent._cast(_1760.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def custom_report_named_item(self) -> 'CustomReportNamedItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportNamedItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportNamedItem._Cast_CustomReportNamedItem':
        return self._Cast_CustomReportNamedItem(self)
