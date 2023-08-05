"""_1769.py

CustomTable
"""
from mastapy._internal import constructor
from mastapy.utility.report import _1758, _1767
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_TABLE = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomTable')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomTable',)


class CustomTable(_1758.CustomReportMultiPropertyItem['_1767.CustomRow']):
    """CustomTable

    This is a mastapy class.
    """

    TYPE = _CUSTOM_TABLE

    class _Cast_CustomTable:
        """Special nested class for casting CustomTable to subclasses."""

        def __init__(self, parent: 'CustomTable'):
            self._parent = parent

        @property
        def custom_report_multi_property_item(self):
            return self._parent._cast(_1758.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(self):
            from mastapy.utility.report import _1759
            
            return self._parent._cast(_1759.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(self):
            from mastapy.utility.report import _1760
            
            return self._parent._cast(_1760.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def cylindrical_gear_table_with_mg_charts(self):
            from mastapy.gears.gear_designs.cylindrical import _1029
            
            return self._parent._cast(_1029.CylindricalGearTableWithMGCharts)

        @property
        def custom_table_and_chart(self):
            from mastapy.utility_gui.charts import _1841
            
            return self._parent._cast(_1841.CustomTableAndChart)

        @property
        def custom_table(self) -> 'CustomTable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomTable.TYPE'):
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
    def cast_to(self) -> 'CustomTable._Cast_CustomTable':
        return self._Cast_CustomTable(self)
