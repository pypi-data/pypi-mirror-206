"""_1765.py

CustomReportTabs
"""
from mastapy._internal import constructor
from mastapy.utility.report import _1754, _1764
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_TABS = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportTabs')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportTabs',)


class CustomReportTabs(_1754.CustomReportItemContainerCollection['_1764.CustomReportTab']):
    """CustomReportTabs

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_TABS

    class _Cast_CustomReportTabs:
        """Special nested class for casting CustomReportTabs to subclasses."""

        def __init__(self, parent: 'CustomReportTabs'):
            self._parent = parent

        @property
        def custom_report_item_container_collection(self):
            return self._parent._cast(_1754.CustomReportItemContainerCollection)

        @property
        def custom_report_item_container_collection_base(self):
            from mastapy.utility.report import _1755
            
            return self._parent._cast(_1755.CustomReportItemContainerCollectionBase)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def custom_report_tabs(self) -> 'CustomReportTabs':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportTabs.TYPE'):
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
    def number_of_tabs(self) -> 'int':
        """int: 'NumberOfTabs' is the original name of this property."""

        temp = self.wrapped.NumberOfTabs

        if temp is None:
            return 0

        return temp

    @number_of_tabs.setter
    def number_of_tabs(self, value: 'int'):
        self.wrapped.NumberOfTabs = int(value) if value else 0

    @property
    def scroll_content(self) -> 'bool':
        """bool: 'ScrollContent' is the original name of this property."""

        temp = self.wrapped.ScrollContent

        if temp is None:
            return False

        return temp

    @scroll_content.setter
    def scroll_content(self, value: 'bool'):
        self.wrapped.ScrollContent = bool(value) if value else False

    @property
    def cast_to(self) -> 'CustomReportTabs._Cast_CustomReportTabs':
        return self._Cast_CustomReportTabs(self)
