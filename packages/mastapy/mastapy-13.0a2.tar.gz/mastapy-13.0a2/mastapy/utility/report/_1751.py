"""_1751.py

CustomReportHtmlItem
"""
from mastapy.utility.report import _1749
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_HTML_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportHtmlItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportHtmlItem',)


class CustomReportHtmlItem(_1749.CustomReportDefinitionItem):
    """CustomReportHtmlItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_HTML_ITEM

    class _Cast_CustomReportHtmlItem:
        """Special nested class for casting CustomReportHtmlItem to subclasses."""

        def __init__(self, parent: 'CustomReportHtmlItem'):
            self._parent = parent

        @property
        def custom_report_definition_item(self):
            return self._parent._cast(_1749.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(self):
            from mastapy.utility.report import _1760
            
            return self._parent._cast(_1760.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def custom_report_html_item(self) -> 'CustomReportHtmlItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportHtmlItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportHtmlItem._Cast_CustomReportHtmlItem':
        return self._Cast_CustomReportHtmlItem(self)
