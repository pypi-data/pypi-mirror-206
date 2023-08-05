"""_1746.py

CustomReportChartItem
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility.report import _1738, _1762
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_CHART_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportChartItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportChartItem',)


class CustomReportChartItem(_1762.CustomReportPropertyItem):
    """CustomReportChartItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_CHART_ITEM

    class _Cast_CustomReportChartItem:
        """Special nested class for casting CustomReportChartItem to subclasses."""

        def __init__(self, parent: 'CustomReportChartItem'):
            self._parent = parent

        @property
        def custom_report_property_item(self):
            return self._parent._cast(_1762.CustomReportPropertyItem)

        @property
        def custom_report_chart_item(self) -> 'CustomReportChartItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportChartItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_marker(self) -> 'bool':
        """bool: 'HasMarker' is the original name of this property."""

        temp = self.wrapped.HasMarker

        if temp is None:
            return False

        return temp

    @has_marker.setter
    def has_marker(self, value: 'bool'):
        self.wrapped.HasMarker = bool(value) if value else False

    @property
    def marker_size(self) -> 'float':
        """float: 'MarkerSize' is the original name of this property."""

        temp = self.wrapped.MarkerSize

        if temp is None:
            return 0.0

        return temp

    @marker_size.setter
    def marker_size(self, value: 'float'):
        self.wrapped.MarkerSize = float(value) if value else 0.0

    @property
    def point_shape(self) -> '_1738.SMTChartPointShape':
        """SMTChartPointShape: 'PointShape' is the original name of this property."""

        temp = self.wrapped.PointShape

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1738.SMTChartPointShape)
        return constructor.new_from_mastapy_type(_1738.SMTChartPointShape)(value) if value is not None else None

    @point_shape.setter
    def point_shape(self, value: '_1738.SMTChartPointShape'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1738.SMTChartPointShape.type_())
        self.wrapped.PointShape = value

    @property
    def smooth_lines(self) -> 'bool':
        """bool: 'SmoothLines' is the original name of this property."""

        temp = self.wrapped.SmoothLines

        if temp is None:
            return False

        return temp

    @smooth_lines.setter
    def smooth_lines(self, value: 'bool'):
        self.wrapped.SmoothLines = bool(value) if value else False

    @property
    def cast_to(self) -> 'CustomReportChartItem._Cast_CustomReportChartItem':
        return self._Cast_CustomReportChartItem(self)
