"""_1756.py

CustomReportItemContainerCollectionItem
"""
from mastapy.utility.report import _1753
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportItemContainerCollectionItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportItemContainerCollectionItem',)


class CustomReportItemContainerCollectionItem(_1753.CustomReportItemContainer):
    """CustomReportItemContainerCollectionItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_ITEM

    class _Cast_CustomReportItemContainerCollectionItem:
        """Special nested class for casting CustomReportItemContainerCollectionItem to subclasses."""

        def __init__(self, parent: 'CustomReportItemContainerCollectionItem'):
            self._parent = parent

        @property
        def custom_report_item_container(self):
            return self._parent._cast(_1753.CustomReportItemContainer)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def custom_report_column(self):
            from mastapy.utility.report import _1747
            
            return self._parent._cast(_1747.CustomReportColumn)

        @property
        def custom_report_tab(self):
            from mastapy.utility.report import _1764
            
            return self._parent._cast(_1764.CustomReportTab)

        @property
        def custom_report_item_container_collection_item(self) -> 'CustomReportItemContainerCollectionItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportItemContainerCollectionItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem':
        return self._Cast_CustomReportItemContainerCollectionItem(self)
