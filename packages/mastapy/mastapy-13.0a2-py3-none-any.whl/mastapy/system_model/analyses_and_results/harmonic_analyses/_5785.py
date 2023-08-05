"""_5785.py

StiffnessOptionsForHarmonicAnalysis
"""
from typing import List

from mastapy.utility_gui.charts import _1852
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5736
from mastapy.math_utility import _1523
from mastapy.system_model.analyses_and_results.analysis_cases import _7498
from mastapy.system_model.analyses_and_results.static_loads import _6769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STIFFNESS_OPTIONS_FOR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'StiffnessOptionsForHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StiffnessOptionsForHarmonicAnalysis',)


class StiffnessOptionsForHarmonicAnalysis(_7498.AbstractAnalysisOptions['_6769.StaticLoadCase']):
    """StiffnessOptionsForHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STIFFNESS_OPTIONS_FOR_HARMONIC_ANALYSIS

    class _Cast_StiffnessOptionsForHarmonicAnalysis:
        """Special nested class for casting StiffnessOptionsForHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'StiffnessOptionsForHarmonicAnalysis'):
            self._parent = parent

        @property
        def abstract_analysis_options(self):
            return self._parent._cast(_7498.AbstractAnalysisOptions)

        @property
        def stiffness_options_for_harmonic_analysis(self) -> 'StiffnessOptionsForHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StiffnessOptionsForHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def curve_with_stiffness_steps(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'CurveWithStiffnessSteps' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurveWithStiffnessSteps

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def number_of_stiffness_steps(self) -> 'int':
        """int: 'NumberOfStiffnessSteps' is the original name of this property."""

        temp = self.wrapped.NumberOfStiffnessSteps

        if temp is None:
            return 0

        return temp

    @number_of_stiffness_steps.setter
    def number_of_stiffness_steps(self, value: 'int'):
        self.wrapped.NumberOfStiffnessSteps = int(value) if value else 0

    @property
    def step_creation_option(self) -> 'enum_with_selected_value.EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation':
        """enum_with_selected_value.EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation: 'StepCreationOption' is the original name of this property."""

        temp = self.wrapped.StepCreationOption

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @step_creation_option.setter
    def step_creation_option(self, value: 'enum_with_selected_value.EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.StepCreationOption = value

    @property
    def torque_input_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_HarmonicAnalysisTorqueInputType':
        """enum_with_selected_value.EnumWithSelectedValue_HarmonicAnalysisTorqueInputType: 'TorqueInputType' is the original name of this property."""

        temp = self.wrapped.TorqueInputType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_HarmonicAnalysisTorqueInputType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @torque_input_type.setter
    def torque_input_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_HarmonicAnalysisTorqueInputType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_HarmonicAnalysisTorqueInputType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.TorqueInputType = value

    @property
    def torque_speed_curve(self) -> '_1523.Vector2DListAccessor':
        """Vector2DListAccessor: 'TorqueSpeedCurve' is the original name of this property."""

        temp = self.wrapped.TorqueSpeedCurve

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @torque_speed_curve.setter
    def torque_speed_curve(self, value: '_1523.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.TorqueSpeedCurve = value

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

    def create_load_cases_from_steps(self):
        """ 'CreateLoadCasesFromSteps' is the original name of this method."""

        self.wrapped.CreateLoadCasesFromSteps()

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
    def cast_to(self) -> 'StiffnessOptionsForHarmonicAnalysis._Cast_StiffnessOptionsForHarmonicAnalysis':
        return self._Cast_StiffnessOptionsForHarmonicAnalysis(self)
