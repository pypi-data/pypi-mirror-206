"""_6975.py

AdvancedTimeSteppingAnalysisForModulationOptions
"""
from mastapy.system_model.analyses_and_results.static_loads import _6777, _6769, _6859
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.analyses_and_results import _2663
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'AdvancedTimeSteppingAnalysisForModulationOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('AdvancedTimeSteppingAnalysisForModulationOptions',)


class AdvancedTimeSteppingAnalysisForModulationOptions(_0.APIBase):
    """AdvancedTimeSteppingAnalysisForModulationOptions

    This is a mastapy class.
    """

    TYPE = _ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION_OPTIONS

    class _Cast_AdvancedTimeSteppingAnalysisForModulationOptions:
        """Special nested class for casting AdvancedTimeSteppingAnalysisForModulationOptions to subclasses."""

        def __init__(self, parent: 'AdvancedTimeSteppingAnalysisForModulationOptions'):
            self._parent = parent

        @property
        def advanced_time_stepping_analysis_for_modulation_options(self) -> 'AdvancedTimeSteppingAnalysisForModulationOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AdvancedTimeSteppingAnalysisForModulationOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_time_stepping_analysis_method(self) -> '_6777.AdvancedTimeSteppingAnalysisForModulationType':
        """AdvancedTimeSteppingAnalysisForModulationType: 'AdvancedTimeSteppingAnalysisMethod' is the original name of this property."""

        temp = self.wrapped.AdvancedTimeSteppingAnalysisMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _6777.AdvancedTimeSteppingAnalysisForModulationType)
        return constructor.new_from_mastapy_type(_6777.AdvancedTimeSteppingAnalysisForModulationType)(value) if value is not None else None

    @advanced_time_stepping_analysis_method.setter
    def advanced_time_stepping_analysis_method(self, value: '_6777.AdvancedTimeSteppingAnalysisForModulationType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _6777.AdvancedTimeSteppingAnalysisForModulationType.type_())
        self.wrapped.AdvancedTimeSteppingAnalysisMethod = value

    @property
    def include_time_offset_for_steady_state(self) -> 'bool':
        """bool: 'IncludeTimeOffsetForSteadyState' is the original name of this property."""

        temp = self.wrapped.IncludeTimeOffsetForSteadyState

        if temp is None:
            return False

        return temp

    @include_time_offset_for_steady_state.setter
    def include_time_offset_for_steady_state(self, value: 'bool'):
        self.wrapped.IncludeTimeOffsetForSteadyState = bool(value) if value else False

    @property
    def load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts(self) -> 'list_with_selected_item.ListWithSelectedItem_StaticLoadCase':
        """list_with_selected_item.ListWithSelectedItem_StaticLoadCase: 'LoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts' is the original name of this property."""

        temp = self.wrapped.LoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_StaticLoadCase)(temp) if temp is not None else None

    @load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts.setter
    def load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts(self, value: 'list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.LoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts = value

    @property
    def number_of_periods_for_advanced_time_stepping_analysis(self) -> 'float':
        """float: 'NumberOfPeriodsForAdvancedTimeSteppingAnalysis' is the original name of this property."""

        temp = self.wrapped.NumberOfPeriodsForAdvancedTimeSteppingAnalysis

        if temp is None:
            return 0.0

        return temp

    @number_of_periods_for_advanced_time_stepping_analysis.setter
    def number_of_periods_for_advanced_time_stepping_analysis(self, value: 'float'):
        self.wrapped.NumberOfPeriodsForAdvancedTimeSteppingAnalysis = float(value) if value else 0.0

    @property
    def number_of_steps_for_advanced_time_stepping_analysis(self) -> 'int':
        """int: 'NumberOfStepsForAdvancedTimeSteppingAnalysis' is the original name of this property."""

        temp = self.wrapped.NumberOfStepsForAdvancedTimeSteppingAnalysis

        if temp is None:
            return 0

        return temp

    @number_of_steps_for_advanced_time_stepping_analysis.setter
    def number_of_steps_for_advanced_time_stepping_analysis(self, value: 'int'):
        self.wrapped.NumberOfStepsForAdvancedTimeSteppingAnalysis = int(value) if value else 0

    @property
    def number_of_times_per_quasi_step(self) -> 'int':
        """int: 'NumberOfTimesPerQuasiStep' is the original name of this property."""

        temp = self.wrapped.NumberOfTimesPerQuasiStep

        if temp is None:
            return 0

        return temp

    @number_of_times_per_quasi_step.setter
    def number_of_times_per_quasi_step(self, value: 'int'):
        self.wrapped.NumberOfTimesPerQuasiStep = int(value) if value else 0

    @property
    def tolerance_for_compatibility_of_atsam_and_te_periods_check(self) -> 'float':
        """float: 'ToleranceForCompatibilityOfATSAMAndTEPeriodsCheck' is the original name of this property."""

        temp = self.wrapped.ToleranceForCompatibilityOfATSAMAndTEPeriodsCheck

        if temp is None:
            return 0.0

        return temp

    @tolerance_for_compatibility_of_atsam_and_te_periods_check.setter
    def tolerance_for_compatibility_of_atsam_and_te_periods_check(self, value: 'float'):
        self.wrapped.ToleranceForCompatibilityOfATSAMAndTEPeriodsCheck = float(value) if value else 0.0

    @property
    def use_this_load_case_for_load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts(self) -> 'bool':
        """bool: 'UseThisLoadCaseForLoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts' is the original name of this property."""

        temp = self.wrapped.UseThisLoadCaseForLoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts

        if temp is None:
            return False

        return temp

    @use_this_load_case_for_load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts.setter
    def use_this_load_case_for_load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts(self, value: 'bool'):
        self.wrapped.UseThisLoadCaseForLoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts = bool(value) if value else False

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation(self) -> '_6859.GearSetLoadCase':
        """GearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def time_options(self) -> '_2663.TimeOptions':
        """TimeOptions: 'TimeOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AdvancedTimeSteppingAnalysisForModulationOptions._Cast_AdvancedTimeSteppingAnalysisForModulationOptions':
        return self._Cast_AdvancedTimeSteppingAnalysisForModulationOptions(self)
