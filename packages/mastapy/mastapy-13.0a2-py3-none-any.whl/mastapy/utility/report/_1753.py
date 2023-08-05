"""_1753.py

CustomReportItemContainer
"""
from mastapy.utility.report import _1752
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportItemContainer')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportItemContainer',)


class CustomReportItemContainer(_1752.CustomReportItem):
    """CustomReportItemContainer

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER

    class _Cast_CustomReportItemContainer:
        """Special nested class for casting CustomReportItemContainer to subclasses."""

        def __init__(self, parent: 'CustomReportItemContainer'):
            self._parent = parent

        @property
        def custom_report_item(self):
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def custom_report(self):
            from mastapy.utility.report import _1743
            
            return self._parent._cast(_1743.CustomReport)

        @property
        def custom_report_column(self):
            from mastapy.utility.report import _1747
            
            return self._parent._cast(_1747.CustomReportColumn)

        @property
        def custom_report_item_container_collection_item(self):
            from mastapy.utility.report import _1756
            
            return self._parent._cast(_1756.CustomReportItemContainerCollectionItem)

        @property
        def custom_report_tab(self):
            from mastapy.utility.report import _1764
            
            return self._parent._cast(_1764.CustomReportTab)

        @property
        def custom_report_item_container(self) -> 'CustomReportItemContainer':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportItemContainer.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportItemContainer._Cast_CustomReportItemContainer':
        return self._Cast_CustomReportItemContainer(self)
