"""_1595.py

MeasurementSettings
"""
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.units_and_measurements import _7522
from mastapy.utility import _1583
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_SETTINGS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'MeasurementSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementSettings',)


class MeasurementSettings(_1583.PerMachineSettings):
    """MeasurementSettings

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_SETTINGS

    class _Cast_MeasurementSettings:
        """Special nested class for casting MeasurementSettings to subclasses."""

        def __init__(self, parent: 'MeasurementSettings'):
            self._parent = parent

        @property
        def per_machine_settings(self):
            return self._parent._cast(_1583.PerMachineSettings)

        @property
        def persistent_singleton(self):
            from mastapy.utility import _1584
            
            return self._parent._cast(_1584.PersistentSingleton)

        @property
        def measurement_settings(self) -> 'MeasurementSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeasurementSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def large_number_cutoff(self) -> 'float':
        """float: 'LargeNumberCutoff' is the original name of this property."""

        temp = self.wrapped.LargeNumberCutoff

        if temp is None:
            return 0.0

        return temp

    @large_number_cutoff.setter
    def large_number_cutoff(self, value: 'float'):
        self.wrapped.LargeNumberCutoff = float(value) if value else 0.0

    @property
    def number_decimal_separator(self) -> 'str':
        """str: 'NumberDecimalSeparator' is the original name of this property."""

        temp = self.wrapped.NumberDecimalSeparator

        if temp is None:
            return ''

        return temp

    @number_decimal_separator.setter
    def number_decimal_separator(self, value: 'str'):
        self.wrapped.NumberDecimalSeparator = str(value) if value else ''

    @property
    def number_group_separator(self) -> 'str':
        """str: 'NumberGroupSeparator' is the original name of this property."""

        temp = self.wrapped.NumberGroupSeparator

        if temp is None:
            return ''

        return temp

    @number_group_separator.setter
    def number_group_separator(self, value: 'str'):
        self.wrapped.NumberGroupSeparator = str(value) if value else ''

    @property
    def sample_input(self) -> 'str':
        """str: 'SampleInput' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SampleInput

        if temp is None:
            return ''

        return temp

    @property
    def sample_output(self) -> 'str':
        """str: 'SampleOutput' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SampleOutput

        if temp is None:
            return ''

        return temp

    @property
    def selected_measurement(self) -> 'list_with_selected_item.ListWithSelectedItem_MeasurementBase':
        """list_with_selected_item.ListWithSelectedItem_MeasurementBase: 'SelectedMeasurement' is the original name of this property."""

        temp = self.wrapped.SelectedMeasurement

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_MeasurementBase)(temp) if temp is not None else None

    @selected_measurement.setter
    def selected_measurement(self, value: 'list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_MeasurementBase.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SelectedMeasurement = value

    @property
    def show_trailing_zeros(self) -> 'bool':
        """bool: 'ShowTrailingZeros' is the original name of this property."""

        temp = self.wrapped.ShowTrailingZeros

        if temp is None:
            return False

        return temp

    @show_trailing_zeros.setter
    def show_trailing_zeros(self, value: 'bool'):
        self.wrapped.ShowTrailingZeros = bool(value) if value else False

    @property
    def small_number_cutoff(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SmallNumberCutoff' is the original name of this property."""

        temp = self.wrapped.SmallNumberCutoff

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @small_number_cutoff.setter
    def small_number_cutoff(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SmallNumberCutoff = value

    @property
    def current_selected_measurement(self) -> '_1594.MeasurementBase':
        """MeasurementBase: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def default_to_imperial(self):
        """ 'DefaultToImperial' is the original name of this method."""

        self.wrapped.DefaultToImperial()

    def default_to_metric(self):
        """ 'DefaultToMetric' is the original name of this method."""

        self.wrapped.DefaultToMetric()

    def find_measurement_by_name(self, name: 'str') -> '_1594.MeasurementBase':
        """ 'FindMeasurementByName' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.utility.units_and_measurements.MeasurementBase
        """

        name = str(name)
        method_result = self.wrapped.FindMeasurementByName(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_measurement(self, measurement_type: '_7522.MeasurementType') -> '_1594.MeasurementBase':
        """ 'GetMeasurement' is the original name of this method.

        Args:
            measurement_type (mastapy.units_and_measurements.MeasurementType)

        Returns:
            mastapy.utility.units_and_measurements.MeasurementBase
        """

        measurement_type = conversion.mp_to_pn_enum(measurement_type, _7522.MeasurementType.type_())
        method_result = self.wrapped.GetMeasurement(measurement_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'MeasurementSettings._Cast_MeasurementSettings':
        return self._Cast_MeasurementSettings(self)
