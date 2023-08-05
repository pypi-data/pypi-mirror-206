"""_1748.py

CustomReportColumns
"""
from mastapy._internal import constructor
from mastapy.utility.report import _1754, _1747
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_COLUMNS = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportColumns')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportColumns',)


class CustomReportColumns(_1754.CustomReportItemContainerCollection['_1747.CustomReportColumn']):
    """CustomReportColumns

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_COLUMNS

    class _Cast_CustomReportColumns:
        """Special nested class for casting CustomReportColumns to subclasses."""

        def __init__(self, parent: 'CustomReportColumns'):
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
        def custom_report_columns(self) -> 'CustomReportColumns':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportColumns.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_columns(self) -> 'int':
        """int: 'NumberOfColumns' is the original name of this property."""

        temp = self.wrapped.NumberOfColumns

        if temp is None:
            return 0

        return temp

    @number_of_columns.setter
    def number_of_columns(self, value: 'int'):
        self.wrapped.NumberOfColumns = int(value) if value else 0

    @property
    def show_adjustable_column_divider(self) -> 'bool':
        """bool: 'ShowAdjustableColumnDivider' is the original name of this property."""

        temp = self.wrapped.ShowAdjustableColumnDivider

        if temp is None:
            return False

        return temp

    @show_adjustable_column_divider.setter
    def show_adjustable_column_divider(self, value: 'bool'):
        self.wrapped.ShowAdjustableColumnDivider = bool(value) if value else False

    @property
    def cast_to(self) -> 'CustomReportColumns._Cast_CustomReportColumns':
        return self._Cast_CustomReportColumns(self)
