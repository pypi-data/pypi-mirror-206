"""_1368.py

HarmonicLoadDataBase
"""
from typing import List

from mastapy._internal.implicit import enum_with_selected_value
from mastapy.electric_machines.harmonic_load_data import _1370
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.math_utility import _1501
from mastapy.units_and_measurements import _7522
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_ARRAY = python_net_import('System', 'Array')
_DOUBLE = python_net_import('System', 'Double')
_STRING = python_net_import('System', 'String')
_FOURIER_SERIES = python_net_import('SMT.MastaAPI.MathUtility', 'FourierSeries')
_LIST = python_net_import('System.Collections.Generic', 'List')
_MEASUREMENT_TYPE = python_net_import('SMT.MastaAPIUtility.UnitsAndMeasurements', 'MeasurementType')
_HARMONIC_LOAD_DATA_BASE = python_net_import('SMT.MastaAPI.ElectricMachines.HarmonicLoadData', 'HarmonicLoadDataBase')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicLoadDataBase',)


class HarmonicLoadDataBase(_0.APIBase):
    """HarmonicLoadDataBase

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_BASE

    class _Cast_HarmonicLoadDataBase:
        """Special nested class for casting HarmonicLoadDataBase to subclasses."""

        def __init__(self, parent: 'HarmonicLoadDataBase'):
            self._parent = parent

        @property
        def dynamic_force_results(self):
            from mastapy.electric_machines.results import _1310
            
            return self._parent._cast(_1310.DynamicForceResults)

        @property
        def electric_machine_harmonic_load_data_base(self):
            from mastapy.electric_machines.harmonic_load_data import _1366
            
            return self._parent._cast(_1366.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(self):
            from mastapy.electric_machines.harmonic_load_data import _1371
            
            return self._parent._cast(_1371.SpeedDependentHarmonicLoadData)

        @property
        def conical_gear_set_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6811
            
            return self._parent._cast(_6811.ConicalGearSetHarmonicLoadData)

        @property
        def cylindrical_gear_set_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6828
            
            return self._parent._cast(_6828.CylindricalGearSetHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6835
            
            return self._parent._cast(_6835.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_from_excel(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6836
            
            return self._parent._cast(_6836.ElectricMachineHarmonicLoadDataFromExcel)

        @property
        def electric_machine_harmonic_load_data_from_flux(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6837
            
            return self._parent._cast(_6837.ElectricMachineHarmonicLoadDataFromFlux)

        @property
        def electric_machine_harmonic_load_data_from_jmag(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6838
            
            return self._parent._cast(_6838.ElectricMachineHarmonicLoadDataFromJMAG)

        @property
        def electric_machine_harmonic_load_data_from_masta(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6839
            
            return self._parent._cast(_6839.ElectricMachineHarmonicLoadDataFromMasta)

        @property
        def electric_machine_harmonic_load_data_from_motor_cad(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6840
            
            return self._parent._cast(_6840.ElectricMachineHarmonicLoadDataFromMotorCAD)

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6841
            
            return self._parent._cast(_6841.ElectricMachineHarmonicLoadDataFromMotorPackages)

        @property
        def gear_set_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6858
            
            return self._parent._cast(_6858.GearSetHarmonicLoadData)

        @property
        def point_load_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6901
            
            return self._parent._cast(_6901.PointLoadHarmonicLoadData)

        @property
        def unbalanced_mass_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6943
            
            return self._parent._cast(_6943.UnbalancedMassHarmonicLoadData)

        @property
        def harmonic_load_data_base(self) -> 'HarmonicLoadDataBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicLoadDataBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def data_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType':
        """enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType: 'DataType' is the original name of this property."""

        temp = self.wrapped.DataType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @data_type.setter
    def data_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DataType = value

    @property
    def excitation_order_as_rotational_order_of_shaft(self) -> 'float':
        """float: 'ExcitationOrderAsRotationalOrderOfShaft' is the original name of this property."""

        temp = self.wrapped.ExcitationOrderAsRotationalOrderOfShaft

        if temp is None:
            return 0.0

        return temp

    @excitation_order_as_rotational_order_of_shaft.setter
    def excitation_order_as_rotational_order_of_shaft(self, value: 'float'):
        self.wrapped.ExcitationOrderAsRotationalOrderOfShaft = float(value) if value else 0.0

    @property
    def number_of_cycles_in_signal(self) -> 'float':
        """float: 'NumberOfCyclesInSignal' is the original name of this property."""

        temp = self.wrapped.NumberOfCyclesInSignal

        if temp is None:
            return 0.0

        return temp

    @number_of_cycles_in_signal.setter
    def number_of_cycles_in_signal(self, value: 'float'):
        self.wrapped.NumberOfCyclesInSignal = float(value) if value else 0.0

    @property
    def number_of_harmonics(self) -> 'int':
        """int: 'NumberOfHarmonics' is the original name of this property."""

        temp = self.wrapped.NumberOfHarmonics

        if temp is None:
            return 0

        return temp

    @number_of_harmonics.setter
    def number_of_harmonics(self, value: 'int'):
        self.wrapped.NumberOfHarmonics = int(value) if value else 0

    @property
    def number_of_values(self) -> 'int':
        """int: 'NumberOfValues' is the original name of this property."""

        temp = self.wrapped.NumberOfValues

        if temp is None:
            return 0

        return temp

    @number_of_values.setter
    def number_of_values(self, value: 'int'):
        self.wrapped.NumberOfValues = int(value) if value else 0

    @property
    def excitations(self) -> 'List[_1501.FourierSeries]':
        """List[FourierSeries]: 'Excitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mean_value(self) -> 'float':
        """float: 'MeanValue' is the original name of this property."""

        temp = self.wrapped.MeanValue

        if temp is None:
            return 0.0

        return temp

    @mean_value.setter
    def mean_value(self, value: 'float'):
        self.wrapped.MeanValue = float(value) if value else 0.0

    @property
    def peak_to_peak(self) -> 'float':
        """float: 'PeakToPeak' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakToPeak

        if temp is None:
            return 0.0

        return temp

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def clear_all_data(self):
        """ 'ClearAllData' is the original name of this method."""

        self.wrapped.ClearAllData()

    def clear_selected_data(self):
        """ 'ClearSelectedData' is the original name of this method."""

        self.wrapped.ClearSelectedData()

    def set_selected_harmonic_load_data_with_fourier_series(self, fourier_series: '_1501.FourierSeries'):
        """ 'SetSelectedHarmonicLoadData' is the original name of this method.

        Args:
            fourier_series (mastapy.math_utility.FourierSeries)
        """

        self.wrapped.SetSelectedHarmonicLoadData.Overloads[_FOURIER_SERIES](fourier_series.wrapped if fourier_series else None)

    def set_selected_harmonic_load_data_extended(self, amplitudes: 'List[float]', phases: 'List[float]', mean_value: 'float', fourier_series_name: 'str', fourier_series_measurement_type: '_7522.MeasurementType'):
        """ 'SetSelectedHarmonicLoadData' is the original name of this method.

        Args:
            amplitudes (List[float])
            phases (List[float])
            mean_value (float)
            fourier_series_name (str)
            fourier_series_measurement_type (mastapy.units_and_measurements.MeasurementType)
        """

        amplitudes = conversion.mp_to_pn_list_float(amplitudes)
        phases = conversion.mp_to_pn_list_float(phases)
        mean_value = float(mean_value)
        fourier_series_name = str(fourier_series_name)
        fourier_series_measurement_type = conversion.mp_to_pn_enum(fourier_series_measurement_type, _7522.MeasurementType.type_())
        self.wrapped.SetSelectedHarmonicLoadData.Overloads[_LIST[_DOUBLE], _LIST[_DOUBLE], _DOUBLE, _STRING, _MEASUREMENT_TYPE](amplitudes, phases, mean_value if mean_value else 0.0, fourier_series_name if fourier_series_name else '', fourier_series_measurement_type)

    def set_selected_harmonic_load_data(self, fourier_series_values: 'List[float]', fourier_series_name: 'str', fourier_series_measurement_type: '_7522.MeasurementType'):
        """ 'SetSelectedHarmonicLoadData' is the original name of this method.

        Args:
            fourier_series_values (List[float])
            fourier_series_name (str)
            fourier_series_measurement_type (mastapy.units_and_measurements.MeasurementType)
        """

        fourier_series_values = conversion.mp_to_pn_array_float(fourier_series_values)
        fourier_series_name = str(fourier_series_name)
        fourier_series_measurement_type = conversion.mp_to_pn_enum(fourier_series_measurement_type, _7522.MeasurementType.type_())
        self.wrapped.SetSelectedHarmonicLoadData.Overloads[_ARRAY[_DOUBLE], _STRING, _MEASUREMENT_TYPE](fourier_series_values, fourier_series_name if fourier_series_name else '', fourier_series_measurement_type)

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'HarmonicLoadDataBase._Cast_HarmonicLoadDataBase':
        return self._Cast_HarmonicLoadDataBase(self)
