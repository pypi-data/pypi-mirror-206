"""_2099.py

DynamicBearingAnalysisOptions
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_BEARING_ANALYSIS_OPTIONS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.Dysla', 'DynamicBearingAnalysisOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicBearingAnalysisOptions',)


class DynamicBearingAnalysisOptions(_0.APIBase):
    """DynamicBearingAnalysisOptions

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_BEARING_ANALYSIS_OPTIONS

    class _Cast_DynamicBearingAnalysisOptions:
        """Special nested class for casting DynamicBearingAnalysisOptions to subclasses."""

        def __init__(self, parent: 'DynamicBearingAnalysisOptions'):
            self._parent = parent

        @property
        def dynamic_bearing_analysis_options(self) -> 'DynamicBearingAnalysisOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicBearingAnalysisOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_displacement_damping(self) -> 'float':
        """float: 'ElementDisplacementDamping' is the original name of this property."""

        temp = self.wrapped.ElementDisplacementDamping

        if temp is None:
            return 0.0

        return temp

    @element_displacement_damping.setter
    def element_displacement_damping(self, value: 'float'):
        self.wrapped.ElementDisplacementDamping = float(value) if value else 0.0

    @property
    def end_time(self) -> 'float':
        """float: 'EndTime' is the original name of this property."""

        temp = self.wrapped.EndTime

        if temp is None:
            return 0.0

        return temp

    @end_time.setter
    def end_time(self, value: 'float'):
        self.wrapped.EndTime = float(value) if value else 0.0

    @property
    def include_cage(self) -> 'bool':
        """bool: 'IncludeCage' is the original name of this property."""

        temp = self.wrapped.IncludeCage

        if temp is None:
            return False

        return temp

    @include_cage.setter
    def include_cage(self, value: 'bool'):
        self.wrapped.IncludeCage = bool(value) if value else False

    @property
    def include_torsional_vibration_on_inner(self) -> 'bool':
        """bool: 'IncludeTorsionalVibrationOnInner' is the original name of this property."""

        temp = self.wrapped.IncludeTorsionalVibrationOnInner

        if temp is None:
            return False

        return temp

    @include_torsional_vibration_on_inner.setter
    def include_torsional_vibration_on_inner(self, value: 'bool'):
        self.wrapped.IncludeTorsionalVibrationOnInner = bool(value) if value else False

    @property
    def include_torsional_vibration_on_outer(self) -> 'bool':
        """bool: 'IncludeTorsionalVibrationOnOuter' is the original name of this property."""

        temp = self.wrapped.IncludeTorsionalVibrationOnOuter

        if temp is None:
            return False

        return temp

    @include_torsional_vibration_on_outer.setter
    def include_torsional_vibration_on_outer(self, value: 'bool'):
        self.wrapped.IncludeTorsionalVibrationOnOuter = bool(value) if value else False

    @property
    def log_all_points_during_cage_impacts(self) -> 'bool':
        """bool: 'LogAllPointsDuringCageImpacts' is the original name of this property."""

        temp = self.wrapped.LogAllPointsDuringCageImpacts

        if temp is None:
            return False

        return temp

    @log_all_points_during_cage_impacts.setter
    def log_all_points_during_cage_impacts(self, value: 'bool'):
        self.wrapped.LogAllPointsDuringCageImpacts = bool(value) if value else False

    @property
    def log_all_points(self) -> 'bool':
        """bool: 'LogAllPoints' is the original name of this property."""

        temp = self.wrapped.LogAllPoints

        if temp is None:
            return False

        return temp

    @log_all_points.setter
    def log_all_points(self, value: 'bool'):
        self.wrapped.LogAllPoints = bool(value) if value else False

    @property
    def logging_frequency(self) -> 'float':
        """float: 'LoggingFrequency' is the original name of this property."""

        temp = self.wrapped.LoggingFrequency

        if temp is None:
            return 0.0

        return temp

    @logging_frequency.setter
    def logging_frequency(self, value: 'float'):
        self.wrapped.LoggingFrequency = float(value) if value else 0.0

    @property
    def maximum_number_of_time_steps(self) -> 'int':
        """int: 'MaximumNumberOfTimeSteps' is the original name of this property."""

        temp = self.wrapped.MaximumNumberOfTimeSteps

        if temp is None:
            return 0

        return temp

    @maximum_number_of_time_steps.setter
    def maximum_number_of_time_steps(self, value: 'int'):
        self.wrapped.MaximumNumberOfTimeSteps = int(value) if value else 0

    @property
    def order_of_inner_torsional_vibrations(self) -> 'float':
        """float: 'OrderOfInnerTorsionalVibrations' is the original name of this property."""

        temp = self.wrapped.OrderOfInnerTorsionalVibrations

        if temp is None:
            return 0.0

        return temp

    @order_of_inner_torsional_vibrations.setter
    def order_of_inner_torsional_vibrations(self, value: 'float'):
        self.wrapped.OrderOfInnerTorsionalVibrations = float(value) if value else 0.0

    @property
    def order_of_outer_torsional_vibrations(self) -> 'float':
        """float: 'OrderOfOuterTorsionalVibrations' is the original name of this property."""

        temp = self.wrapped.OrderOfOuterTorsionalVibrations

        if temp is None:
            return 0.0

        return temp

    @order_of_outer_torsional_vibrations.setter
    def order_of_outer_torsional_vibrations(self, value: 'float'):
        self.wrapped.OrderOfOuterTorsionalVibrations = float(value) if value else 0.0

    @property
    def percentage_amplitude_inner_torsional_vibration(self) -> 'float':
        """float: 'PercentageAmplitudeInnerTorsionalVibration' is the original name of this property."""

        temp = self.wrapped.PercentageAmplitudeInnerTorsionalVibration

        if temp is None:
            return 0.0

        return temp

    @percentage_amplitude_inner_torsional_vibration.setter
    def percentage_amplitude_inner_torsional_vibration(self, value: 'float'):
        self.wrapped.PercentageAmplitudeInnerTorsionalVibration = float(value) if value else 0.0

    @property
    def percentage_amplitude_outer_torsional_vibration(self) -> 'float':
        """float: 'PercentageAmplitudeOuterTorsionalVibration' is the original name of this property."""

        temp = self.wrapped.PercentageAmplitudeOuterTorsionalVibration

        if temp is None:
            return 0.0

        return temp

    @percentage_amplitude_outer_torsional_vibration.setter
    def percentage_amplitude_outer_torsional_vibration(self, value: 'float'):
        self.wrapped.PercentageAmplitudeOuterTorsionalVibration = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'DynamicBearingAnalysisOptions._Cast_DynamicBearingAnalysisOptions':
        return self._Cast_DynamicBearingAnalysisOptions(self)
