"""_6960.py

MultiTimeSeriesDataInputFileOptions
"""
from mastapy._internal import constructor
from mastapy.utility.file_access_helpers import _1805
from mastapy.utility_gui import _1834
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_TIME_SERIES_DATA_INPUT_FILE_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'MultiTimeSeriesDataInputFileOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('MultiTimeSeriesDataInputFileOptions',)


class MultiTimeSeriesDataInputFileOptions(_1834.DataInputFileOptions):
    """MultiTimeSeriesDataInputFileOptions

    This is a mastapy class.
    """

    TYPE = _MULTI_TIME_SERIES_DATA_INPUT_FILE_OPTIONS

    class _Cast_MultiTimeSeriesDataInputFileOptions:
        """Special nested class for casting MultiTimeSeriesDataInputFileOptions to subclasses."""

        def __init__(self, parent: 'MultiTimeSeriesDataInputFileOptions'):
            self._parent = parent

        @property
        def data_input_file_options(self):
            return self._parent._cast(_1834.DataInputFileOptions)

        @property
        def multi_time_series_data_input_file_options(self) -> 'MultiTimeSeriesDataInputFileOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MultiTimeSeriesDataInputFileOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duration(self) -> 'float':
        """float: 'Duration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @property
    def duration_scaling(self) -> 'float':
        """float: 'DurationScaling' is the original name of this property."""

        temp = self.wrapped.DurationScaling

        if temp is None:
            return 0.0

        return temp

    @duration_scaling.setter
    def duration_scaling(self, value: 'float'):
        self.wrapped.DurationScaling = float(value) if value else 0.0

    @property
    def proportion_of_duty_cycle(self) -> 'float':
        """float: 'ProportionOfDutyCycle' is the original name of this property."""

        temp = self.wrapped.ProportionOfDutyCycle

        if temp is None:
            return 0.0

        return temp

    @proportion_of_duty_cycle.setter
    def proportion_of_duty_cycle(self, value: 'float'):
        self.wrapped.ProportionOfDutyCycle = float(value) if value else 0.0

    @property
    def delimiter_options(self) -> '_1805.TextFileDelimiterOptions':
        """TextFileDelimiterOptions: 'DelimiterOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DelimiterOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MultiTimeSeriesDataInputFileOptions._Cast_MultiTimeSeriesDataInputFileOptions':
        return self._Cast_MultiTimeSeriesDataInputFileOptions(self)
