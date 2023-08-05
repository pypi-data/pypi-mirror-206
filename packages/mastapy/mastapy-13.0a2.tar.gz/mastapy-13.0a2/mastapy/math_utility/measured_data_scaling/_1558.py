"""_1558.py

DataScalingOptions
"""
from typing import List

from mastapy._internal.implicit import enum_with_selected_value
from mastapy.math_utility import _1494, _1478
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.math_utility.measured_data_scaling import _1559
from mastapy.utility.units_and_measurements.measurements import (
    _1601, _1602, _1606, _1610,
    _1618, _1625, _1631, _1637,
    _1665, _1673, _1654, _1678,
    _1679, _1683, _1682, _1688,
    _1698, _1656, _1712, _1604,
    _1628, _1721, _1703, _1704,
    _1715, _1716, _1714, _1677,
    _1720, _1659, _1713, _1605
)
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_SCALING_OPTIONS = python_net_import('SMT.MastaAPI.MathUtility.MeasuredDataScaling', 'DataScalingOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('DataScalingOptions',)


class DataScalingOptions(_0.APIBase):
    """DataScalingOptions

    This is a mastapy class.
    """

    TYPE = _DATA_SCALING_OPTIONS

    class _Cast_DataScalingOptions:
        """Special nested class for casting DataScalingOptions to subclasses."""

        def __init__(self, parent: 'DataScalingOptions'):
            self._parent = parent

        @property
        def data_scaling_options(self) -> 'DataScalingOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DataScalingOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_scaling(self) -> 'enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling':
        """enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling: 'DynamicScaling' is the original name of this property."""

        temp = self.wrapped.DynamicScaling

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @dynamic_scaling.setter
    def dynamic_scaling(self, value: 'enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DynamicScaling = value

    @property
    def weighting(self) -> '_1478.AcousticWeighting':
        """AcousticWeighting: 'Weighting' is the original name of this property."""

        temp = self.wrapped.Weighting

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1478.AcousticWeighting)
        return constructor.new_from_mastapy_type(_1478.AcousticWeighting)(value) if value is not None else None

    @weighting.setter
    def weighting(self, value: '_1478.AcousticWeighting'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1478.AcousticWeighting.type_())
        self.wrapped.Weighting = value

    @property
    def acceleration_reference_values(self) -> '_1559.DataScalingReferenceValues[_1601.Acceleration]':
        """DataScalingReferenceValues[Acceleration]: 'AccelerationReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccelerationReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1601.Acceleration](temp) if temp is not None else None

    @property
    def angle_reference_values(self) -> '_1559.DataScalingReferenceValues[_1602.Angle]':
        """DataScalingReferenceValues[Angle]: 'AngleReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngleReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1602.Angle](temp) if temp is not None else None

    @property
    def angular_acceleration_reference_values(self) -> '_1559.DataScalingReferenceValues[_1606.AngularAcceleration]':
        """DataScalingReferenceValues[AngularAcceleration]: 'AngularAccelerationReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularAccelerationReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1606.AngularAcceleration](temp) if temp is not None else None

    @property
    def angular_velocity_reference_values(self) -> '_1559.DataScalingReferenceValues[_1610.AngularVelocity]':
        """DataScalingReferenceValues[AngularVelocity]: 'AngularVelocityReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularVelocityReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1610.AngularVelocity](temp) if temp is not None else None

    @property
    def damage_rate(self) -> '_1559.DataScalingReferenceValues[_1618.DamageRate]':
        """DataScalingReferenceValues[DamageRate]: 'DamageRate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageRate

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1618.DamageRate](temp) if temp is not None else None

    @property
    def energy_reference_values(self) -> '_1559.DataScalingReferenceValues[_1625.Energy]':
        """DataScalingReferenceValues[Energy]: 'EnergyReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EnergyReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1625.Energy](temp) if temp is not None else None

    @property
    def force_reference_values(self) -> '_1559.DataScalingReferenceValues[_1631.Force]':
        """DataScalingReferenceValues[Force]: 'ForceReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1631.Force](temp) if temp is not None else None

    @property
    def frequency_reference_values(self) -> '_1559.DataScalingReferenceValues[_1637.Frequency]':
        """DataScalingReferenceValues[Frequency]: 'FrequencyReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrequencyReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1637.Frequency](temp) if temp is not None else None

    @property
    def linear_stiffness_reference_values(self) -> '_1559.DataScalingReferenceValues[_1665.LinearStiffness]':
        """DataScalingReferenceValues[LinearStiffness]: 'LinearStiffnessReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearStiffnessReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1665.LinearStiffness](temp) if temp is not None else None

    @property
    def mass_per_unit_time_reference_values(self) -> '_1559.DataScalingReferenceValues[_1673.MassPerUnitTime]':
        """DataScalingReferenceValues[MassPerUnitTime]: 'MassPerUnitTimeReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassPerUnitTimeReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1673.MassPerUnitTime](temp) if temp is not None else None

    @property
    def medium_length_reference_values(self) -> '_1559.DataScalingReferenceValues[_1654.LengthMedium]':
        """DataScalingReferenceValues[LengthMedium]: 'MediumLengthReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MediumLengthReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1654.LengthMedium](temp) if temp is not None else None

    @property
    def percentage(self) -> '_1559.DataScalingReferenceValues[_1678.Percentage]':
        """DataScalingReferenceValues[Percentage]: 'Percentage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Percentage

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1678.Percentage](temp) if temp is not None else None

    @property
    def power_reference_values(self) -> '_1559.DataScalingReferenceValues[_1679.Power]':
        """DataScalingReferenceValues[Power]: 'PowerReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1679.Power](temp) if temp is not None else None

    @property
    def power_small_per_unit_area_reference_values(self) -> '_1559.DataScalingReferenceValues[_1683.PowerSmallPerArea]':
        """DataScalingReferenceValues[PowerSmallPerArea]: 'PowerSmallPerUnitAreaReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerSmallPerUnitAreaReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1683.PowerSmallPerArea](temp) if temp is not None else None

    @property
    def power_small_reference_values(self) -> '_1559.DataScalingReferenceValues[_1682.PowerSmall]':
        """DataScalingReferenceValues[PowerSmall]: 'PowerSmallReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerSmallReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1682.PowerSmall](temp) if temp is not None else None

    @property
    def pressure_reference_values(self) -> '_1559.DataScalingReferenceValues[_1688.Pressure]':
        """DataScalingReferenceValues[Pressure]: 'PressureReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PressureReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1688.Pressure](temp) if temp is not None else None

    @property
    def safety_factor(self) -> '_1559.DataScalingReferenceValues[_1698.SafetyFactor]':
        """DataScalingReferenceValues[SafetyFactor]: 'SafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1698.SafetyFactor](temp) if temp is not None else None

    @property
    def short_length_reference_values(self) -> '_1559.DataScalingReferenceValues[_1656.LengthShort]':
        """DataScalingReferenceValues[LengthShort]: 'ShortLengthReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShortLengthReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1656.LengthShort](temp) if temp is not None else None

    @property
    def short_time_reference_values(self) -> '_1559.DataScalingReferenceValues[_1712.TimeShort]':
        """DataScalingReferenceValues[TimeShort]: 'ShortTimeReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShortTimeReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1712.TimeShort](temp) if temp is not None else None

    @property
    def small_angle_reference_values(self) -> '_1559.DataScalingReferenceValues[_1604.AngleSmall]':
        """DataScalingReferenceValues[AngleSmall]: 'SmallAngleReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallAngleReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1604.AngleSmall](temp) if temp is not None else None

    @property
    def small_energy_reference_values(self) -> '_1559.DataScalingReferenceValues[_1628.EnergySmall]':
        """DataScalingReferenceValues[EnergySmall]: 'SmallEnergyReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallEnergyReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1628.EnergySmall](temp) if temp is not None else None

    @property
    def small_velocity_reference_values(self) -> '_1559.DataScalingReferenceValues[_1721.VelocitySmall]':
        """DataScalingReferenceValues[VelocitySmall]: 'SmallVelocityReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallVelocityReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1721.VelocitySmall](temp) if temp is not None else None

    @property
    def stress_reference_values(self) -> '_1559.DataScalingReferenceValues[_1703.Stress]':
        """DataScalingReferenceValues[Stress]: 'StressReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1703.Stress](temp) if temp is not None else None

    @property
    def temperature_reference_values(self) -> '_1559.DataScalingReferenceValues[_1704.Temperature]':
        """DataScalingReferenceValues[Temperature]: 'TemperatureReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TemperatureReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1704.Temperature](temp) if temp is not None else None

    @property
    def torque_converter_inverse_k(self) -> '_1559.DataScalingReferenceValues[_1715.TorqueConverterInverseK]':
        """DataScalingReferenceValues[TorqueConverterInverseK]: 'TorqueConverterInverseK' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConverterInverseK

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1715.TorqueConverterInverseK](temp) if temp is not None else None

    @property
    def torque_converter_k(self) -> '_1559.DataScalingReferenceValues[_1716.TorqueConverterK]':
        """DataScalingReferenceValues[TorqueConverterK]: 'TorqueConverterK' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConverterK

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1716.TorqueConverterK](temp) if temp is not None else None

    @property
    def torque_reference_values(self) -> '_1559.DataScalingReferenceValues[_1714.Torque]':
        """DataScalingReferenceValues[Torque]: 'TorqueReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1714.Torque](temp) if temp is not None else None

    @property
    def unmeasureable(self) -> '_1559.DataScalingReferenceValues[_1677.Number]':
        """DataScalingReferenceValues[Number]: 'Unmeasureable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Unmeasureable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1677.Number](temp) if temp is not None else None

    @property
    def velocity_reference_values(self) -> '_1559.DataScalingReferenceValues[_1720.Velocity]':
        """DataScalingReferenceValues[Velocity]: 'VelocityReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VelocityReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1720.Velocity](temp) if temp is not None else None

    @property
    def very_short_length_reference_values(self) -> '_1559.DataScalingReferenceValues[_1659.LengthVeryShort]':
        """DataScalingReferenceValues[LengthVeryShort]: 'VeryShortLengthReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VeryShortLengthReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1659.LengthVeryShort](temp) if temp is not None else None

    @property
    def very_short_time_reference_values(self) -> '_1559.DataScalingReferenceValues[_1713.TimeVeryShort]':
        """DataScalingReferenceValues[TimeVeryShort]: 'VeryShortTimeReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VeryShortTimeReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1713.TimeVeryShort](temp) if temp is not None else None

    @property
    def very_small_angle_reference_values(self) -> '_1559.DataScalingReferenceValues[_1605.AngleVerySmall]':
        """DataScalingReferenceValues[AngleVerySmall]: 'VerySmallAngleReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VerySmallAngleReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1605.AngleVerySmall](temp) if temp is not None else None

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
    def cast_to(self) -> 'DataScalingOptions._Cast_DataScalingOptions':
        return self._Cast_DataScalingOptions(self)
