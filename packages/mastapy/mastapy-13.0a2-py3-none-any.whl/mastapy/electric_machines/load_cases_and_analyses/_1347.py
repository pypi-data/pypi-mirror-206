"""_1347.py

ElectricMachineLoadCaseGroup
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import (
    _1336, _1338, _1363, _1345,
    _1362, _1351, _1346
)
from mastapy.electric_machines import _1259
from mastapy.utility import _1579
from mastapy import _7521, _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineLoadCaseGroup',)


class ElectricMachineLoadCaseGroup(_0.APIBase):
    """ElectricMachineLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_LOAD_CASE_GROUP

    class _Cast_ElectricMachineLoadCaseGroup:
        """Special nested class for casting ElectricMachineLoadCaseGroup to subclasses."""

        def __init__(self, parent: 'ElectricMachineLoadCaseGroup'):
            self._parent = parent

        @property
        def electric_machine_load_case_group(self) -> 'ElectricMachineLoadCaseGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def dynamic_forces_load_cases(self) -> 'List[_1336.DynamicForceLoadCase]':
        """List[DynamicForceLoadCase]: 'DynamicForcesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicForcesLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def efficiency_map_load_cases(self) -> 'List[_1338.EfficiencyMapLoadCase]':
        """List[EfficiencyMapLoadCase]: 'EfficiencyMapLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EfficiencyMapLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def single_operating_point_load_cases_with_non_linear_dq_model(self) -> 'List[_1363.SpeedTorqueLoadCase]':
        """List[SpeedTorqueLoadCase]: 'SingleOperatingPointLoadCasesWithNonLinearDQModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingleOperatingPointLoadCasesWithNonLinearDQModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def single_operating_point_load_cases_without_non_linear_dq_model(self) -> 'List[_1345.ElectricMachineLoadCase]':
        """List[ElectricMachineLoadCase]: 'SingleOperatingPointLoadCasesWithoutNonLinearDQModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingleOperatingPointLoadCasesWithoutNonLinearDQModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def speed_torque_curve_load_cases(self) -> 'List[_1362.SpeedTorqueCurveLoadCase]':
        """List[SpeedTorqueCurveLoadCase]: 'SpeedTorqueCurveLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedTorqueCurveLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

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

    def add_load_case(self, load_case_type: '_1351.LoadCaseType') -> '_1346.ElectricMachineLoadCaseBase':
        """ 'AddLoadCase' is the original name of this method.

        Args:
            load_case_type (mastapy.electric_machines.load_cases_and_analyses.LoadCaseType)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseBase
        """

        load_case_type = conversion.mp_to_pn_enum(load_case_type, _1351.LoadCaseType.type_())
        method_result = self.wrapped.AddLoadCase(load_case_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_load_case_named(self, load_case_type: '_1351.LoadCaseType', name: 'str') -> '_1346.ElectricMachineLoadCaseBase':
        """ 'AddLoadCaseNamed' is the original name of this method.

        Args:
            load_case_type (mastapy.electric_machines.load_cases_and_analyses.LoadCaseType)
            name (str)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseBase
        """

        load_case_type = conversion.mp_to_pn_enum(load_case_type, _1351.LoadCaseType.type_())
        name = str(name)
        method_result = self.wrapped.AddLoadCaseNamed(load_case_type, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def load_case_named(self, load_case_type: '_1351.LoadCaseType', name: 'str') -> '_1346.ElectricMachineLoadCaseBase':
        """ 'LoadCaseNamed' is the original name of this method.

        Args:
            load_case_type (mastapy.electric_machines.load_cases_and_analyses.LoadCaseType)
            name (str)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseBase
        """

        load_case_type = conversion.mp_to_pn_enum(load_case_type, _1351.LoadCaseType.type_())
        name = str(name)
        method_result = self.wrapped.LoadCaseNamed(load_case_type, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def perform_compound_analysis(self, setup: '_1259.ElectricMachineSetup', load_case_type: '_1351.LoadCaseType') -> '_1579.MethodOutcome':
        """ 'PerformCompoundAnalysis' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)
            load_case_type (mastapy.electric_machines.load_cases_and_analyses.LoadCaseType)

        Returns:
            mastapy.utility.MethodOutcome
        """

        load_case_type = conversion.mp_to_pn_enum(load_case_type, _1351.LoadCaseType.type_())
        method_result = self.wrapped.PerformCompoundAnalysis(setup.wrapped if setup else None, load_case_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def perform_compound_analysis_with_progress(self, setup: '_1259.ElectricMachineSetup', load_case_type: '_1351.LoadCaseType', task_progress: '_7521.TaskProgress') -> '_1579.MethodOutcome':
        """ 'PerformCompoundAnalysisWithProgress' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)
            load_case_type (mastapy.electric_machines.load_cases_and_analyses.LoadCaseType)
            task_progress (mastapy.TaskProgress)

        Returns:
            mastapy.utility.MethodOutcome
        """

        load_case_type = conversion.mp_to_pn_enum(load_case_type, _1351.LoadCaseType.type_())
        method_result = self.wrapped.PerformCompoundAnalysisWithProgress(setup.wrapped if setup else None, load_case_type, task_progress.wrapped if task_progress else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def remove_all_electric_machine_load_cases(self):
        """ 'RemoveAllElectricMachineLoadCases' is the original name of this method."""

        self.wrapped.RemoveAllElectricMachineLoadCases()

    def try_remove_load_case(self, load_case: '_1346.ElectricMachineLoadCaseBase') -> 'bool':
        """ 'TryRemoveLoadCase' is the original name of this method.

        Args:
            load_case (mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseBase)

        Returns:
            bool
        """

        method_result = self.wrapped.TryRemoveLoadCase(load_case.wrapped if load_case else None)
        return method_result

    def try_remove_load_case_named(self, load_case_type: '_1351.LoadCaseType', name: 'str') -> 'bool':
        """ 'TryRemoveLoadCaseNamed' is the original name of this method.

        Args:
            load_case_type (mastapy.electric_machines.load_cases_and_analyses.LoadCaseType)
            name (str)

        Returns:
            bool
        """

        load_case_type = conversion.mp_to_pn_enum(load_case_type, _1351.LoadCaseType.type_())
        name = str(name)
        method_result = self.wrapped.TryRemoveLoadCaseNamed(load_case_type, name if name else '')
        return method_result

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
    def cast_to(self) -> 'ElectricMachineLoadCaseGroup._Cast_ElectricMachineLoadCaseGroup':
        return self._Cast_ElectricMachineLoadCaseGroup(self)
