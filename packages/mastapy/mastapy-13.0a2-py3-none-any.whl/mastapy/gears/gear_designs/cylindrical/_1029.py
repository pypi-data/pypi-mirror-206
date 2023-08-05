"""_1029.py

CylindricalGearTableWithMGCharts
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs.cylindrical import _1028
from mastapy.utility.report import _1769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TABLE_WITH_MG_CHARTS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearTableWithMGCharts')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearTableWithMGCharts',)


class CylindricalGearTableWithMGCharts(_1769.CustomTable):
    """CylindricalGearTableWithMGCharts

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TABLE_WITH_MG_CHARTS

    class _Cast_CylindricalGearTableWithMGCharts:
        """Special nested class for casting CylindricalGearTableWithMGCharts to subclasses."""

        def __init__(self, parent: 'CylindricalGearTableWithMGCharts'):
            self._parent = parent

        @property
        def custom_table(self):
            return self._parent._cast(_1769.CustomTable)

        @property
        def custom_report_multi_property_item(self):
            from mastapy.utility.report import _1758, _1767
            
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
        def cylindrical_gear_table_with_mg_charts(self) -> 'CylindricalGearTableWithMGCharts':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearTableWithMGCharts.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chart_height(self) -> 'int':
        """int: 'ChartHeight' is the original name of this property."""

        temp = self.wrapped.ChartHeight

        if temp is None:
            return 0

        return temp

    @chart_height.setter
    def chart_height(self, value: 'int'):
        self.wrapped.ChartHeight = int(value) if value else 0

    @property
    def chart_width(self) -> 'int':
        """int: 'ChartWidth' is the original name of this property."""

        temp = self.wrapped.ChartWidth

        if temp is None:
            return 0

        return temp

    @chart_width.setter
    def chart_width(self, value: 'int'):
        self.wrapped.ChartWidth = int(value) if value else 0

    @property
    def item_detail(self) -> '_1028.CylindricalGearTableMGItemDetail':
        """CylindricalGearTableMGItemDetail: 'ItemDetail' is the original name of this property."""

        temp = self.wrapped.ItemDetail

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1028.CylindricalGearTableMGItemDetail)
        return constructor.new_from_mastapy_type(_1028.CylindricalGearTableMGItemDetail)(value) if value is not None else None

    @item_detail.setter
    def item_detail(self, value: '_1028.CylindricalGearTableMGItemDetail'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1028.CylindricalGearTableMGItemDetail.type_())
        self.wrapped.ItemDetail = value

    @property
    def cast_to(self) -> 'CylindricalGearTableWithMGCharts._Cast_CylindricalGearTableWithMGCharts':
        return self._Cast_CylindricalGearTableWithMGCharts(self)
