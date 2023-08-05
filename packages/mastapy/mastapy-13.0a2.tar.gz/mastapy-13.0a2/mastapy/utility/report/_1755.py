"""_1755.py

CustomReportItemContainerCollectionBase
"""
from mastapy.utility.report import _1752
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_BASE = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportItemContainerCollectionBase')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportItemContainerCollectionBase',)


class CustomReportItemContainerCollectionBase(_1752.CustomReportItem):
    """CustomReportItemContainerCollectionBase

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_BASE

    class _Cast_CustomReportItemContainerCollectionBase:
        """Special nested class for casting CustomReportItemContainerCollectionBase to subclasses."""

        def __init__(self, parent: 'CustomReportItemContainerCollectionBase'):
            self._parent = parent

        @property
        def custom_report_item(self):
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def custom_report_columns(self):
            from mastapy.utility.report import _1748
            
            return self._parent._cast(_1748.CustomReportColumns)

        @property
        def custom_report_item_container_collection(self):
            from mastapy.utility.report import _1754
            
            return self._parent._cast(_1754.CustomReportItemContainerCollection)

        @property
        def custom_report_tabs(self):
            from mastapy.utility.report import _1765
            
            return self._parent._cast(_1765.CustomReportTabs)

        @property
        def custom_report_item_container_collection_base(self) -> 'CustomReportItemContainerCollectionBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportItemContainerCollectionBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportItemContainerCollectionBase._Cast_CustomReportItemContainerCollectionBase':
        return self._Cast_CustomReportItemContainerCollectionBase(self)
