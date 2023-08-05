"""_1754.py

CustomReportItemContainerCollection
"""
from typing import TypeVar, Generic

from mastapy.utility.report import _1755, _1756
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportItemContainerCollection')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportItemContainerCollection',)


T = TypeVar('T', bound='_1756.CustomReportItemContainerCollectionItem')


class CustomReportItemContainerCollection(_1755.CustomReportItemContainerCollectionBase, Generic[T]):
    """CustomReportItemContainerCollection

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION

    class _Cast_CustomReportItemContainerCollection:
        """Special nested class for casting CustomReportItemContainerCollection to subclasses."""

        def __init__(self, parent: 'CustomReportItemContainerCollection'):
            self._parent = parent

        @property
        def custom_report_item_container_collection_base(self):
            return self._parent._cast(_1755.CustomReportItemContainerCollectionBase)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def custom_report_columns(self):
            from mastapy.utility.report import _1748
            
            return self._parent._cast(_1748.CustomReportColumns)

        @property
        def custom_report_tabs(self):
            from mastapy.utility.report import _1765
            
            return self._parent._cast(_1765.CustomReportTabs)

        @property
        def custom_report_item_container_collection(self) -> 'CustomReportItemContainerCollection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportItemContainerCollection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportItemContainerCollection._Cast_CustomReportItemContainerCollection':
        return self._Cast_CustomReportItemContainerCollection(self)
