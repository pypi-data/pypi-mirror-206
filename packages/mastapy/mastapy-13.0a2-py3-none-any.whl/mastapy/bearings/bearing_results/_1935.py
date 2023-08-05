"""_1935.py

LoadedBearingTemperatureChart
"""
from mastapy._internal import constructor
from mastapy.utility.report import _1745
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_TEMPERATURE_CHART = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedBearingTemperatureChart')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBearingTemperatureChart',)


class LoadedBearingTemperatureChart(_1745.CustomReportChart):
    """LoadedBearingTemperatureChart

    This is a mastapy class.
    """

    TYPE = _LOADED_BEARING_TEMPERATURE_CHART

    class _Cast_LoadedBearingTemperatureChart:
        """Special nested class for casting LoadedBearingTemperatureChart to subclasses."""

        def __init__(self, parent: 'LoadedBearingTemperatureChart'):
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
        def loaded_bearing_temperature_chart(self) -> 'LoadedBearingTemperatureChart':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedBearingTemperatureChart.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_temperature(self) -> 'float':
        """float: 'MaximumTemperature' is the original name of this property."""

        temp = self.wrapped.MaximumTemperature

        if temp is None:
            return 0.0

        return temp

    @maximum_temperature.setter
    def maximum_temperature(self, value: 'float'):
        self.wrapped.MaximumTemperature = float(value) if value else 0.0

    @property
    def minimum_temperature(self) -> 'float':
        """float: 'MinimumTemperature' is the original name of this property."""

        temp = self.wrapped.MinimumTemperature

        if temp is None:
            return 0.0

        return temp

    @minimum_temperature.setter
    def minimum_temperature(self, value: 'float'):
        self.wrapped.MinimumTemperature = float(value) if value else 0.0

    @property
    def number_of_steps(self) -> 'int':
        """int: 'NumberOfSteps' is the original name of this property."""

        temp = self.wrapped.NumberOfSteps

        if temp is None:
            return 0

        return temp

    @number_of_steps.setter
    def number_of_steps(self, value: 'int'):
        self.wrapped.NumberOfSteps = int(value) if value else 0

    @property
    def cast_to(self) -> 'LoadedBearingTemperatureChart._Cast_LoadedBearingTemperatureChart':
        return self._Cast_LoadedBearingTemperatureChart(self)
