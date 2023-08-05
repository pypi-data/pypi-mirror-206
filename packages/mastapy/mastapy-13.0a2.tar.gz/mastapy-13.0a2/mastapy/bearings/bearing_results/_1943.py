"""_1943.py

LoadedRollerElementChartReporter
"""
from mastapy._internal import constructor
from mastapy.utility.report import _1745
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_ELEMENT_CHART_REPORTER = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedRollerElementChartReporter')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedRollerElementChartReporter',)


class LoadedRollerElementChartReporter(_1745.CustomReportChart):
    """LoadedRollerElementChartReporter

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_ELEMENT_CHART_REPORTER

    class _Cast_LoadedRollerElementChartReporter:
        """Special nested class for casting LoadedRollerElementChartReporter to subclasses."""

        def __init__(self, parent: 'LoadedRollerElementChartReporter'):
            self._parent = parent

        @property
        def custom_report_chart(self):
            return self._parent._cast(_1745.CustomReportChart)

        @property
        def custom_report_multi_property_item(self):
            from mastapy.utility.report import _1758, _1746
            
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
        def loaded_roller_element_chart_reporter(self) -> 'LoadedRollerElementChartReporter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedRollerElementChartReporter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def only_show_roller_with_highest_load(self) -> 'bool':
        """bool: 'OnlyShowRollerWithHighestLoad' is the original name of this property."""

        temp = self.wrapped.OnlyShowRollerWithHighestLoad

        if temp is None:
            return False

        return temp

    @only_show_roller_with_highest_load.setter
    def only_show_roller_with_highest_load(self, value: 'bool'):
        self.wrapped.OnlyShowRollerWithHighestLoad = bool(value) if value else False

    @property
    def start_y_axis_at_zero(self) -> 'bool':
        """bool: 'StartYAxisAtZero' is the original name of this property."""

        temp = self.wrapped.StartYAxisAtZero

        if temp is None:
            return False

        return temp

    @start_y_axis_at_zero.setter
    def start_y_axis_at_zero(self, value: 'bool'):
        self.wrapped.StartYAxisAtZero = bool(value) if value else False

    @property
    def cast_to(self) -> 'LoadedRollerElementChartReporter._Cast_LoadedRollerElementChartReporter':
        return self._Cast_LoadedRollerElementChartReporter(self)
