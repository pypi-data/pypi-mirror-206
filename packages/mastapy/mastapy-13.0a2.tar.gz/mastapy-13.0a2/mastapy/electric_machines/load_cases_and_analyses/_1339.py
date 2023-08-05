"""_1339.py

ElectricMachineAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines import _1254, _1259
from mastapy.electric_machines.load_cases_and_analyses import _1346
from mastapy import _7521, _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineAnalysis',)


class ElectricMachineAnalysis(_0.APIBase):
    """ElectricMachineAnalysis

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_ANALYSIS

    class _Cast_ElectricMachineAnalysis:
        """Special nested class for casting ElectricMachineAnalysis to subclasses."""

        def __init__(self, parent: 'ElectricMachineAnalysis'):
            self._parent = parent

        @property
        def dynamic_force_analysis(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1335
            
            return self._parent._cast(_1335.DynamicForceAnalysis)

        @property
        def efficiency_map_analysis(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1337
            
            return self._parent._cast(_1337.EfficiencyMapAnalysis)

        @property
        def electric_machine_fe_analysis(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1343
            
            return self._parent._cast(_1343.ElectricMachineFEAnalysis)

        @property
        def electric_machine_fe_mechanical_analysis(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1344
            
            return self._parent._cast(_1344.ElectricMachineFEMechanicalAnalysis)

        @property
        def single_operating_point_analysis(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1357
            
            return self._parent._cast(_1357.SingleOperatingPointAnalysis)

        @property
        def speed_torque_curve_analysis(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1361
            
            return self._parent._cast(_1361.SpeedTorqueCurveAnalysis)

        @property
        def electric_machine_analysis(self) -> 'ElectricMachineAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_time(self) -> 'float':
        """float: 'AnalysisTime' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisTime

        if temp is None:
            return 0.0

        return temp

    @property
    def magnet_temperature(self) -> 'float':
        """float: 'MagnetTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MagnetTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def windings_temperature(self) -> 'float':
        """float: 'WindingsTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingsTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def electric_machine_detail(self) -> '_1254.ElectricMachineDetail':
        """ElectricMachineDetail: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_case(self) -> '_1346.ElectricMachineLoadCaseBase':
        """ElectricMachineLoadCaseBase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def setup(self) -> '_1259.ElectricMachineSetup':
        """ElectricMachineSetup: 'Setup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Setup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results_ready(self) -> 'bool':
        """bool: 'ResultsReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsReady

        if temp is None:
            return False

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

    def perform_analysis(self):
        """ 'PerformAnalysis' is the original name of this method."""

        self.wrapped.PerformAnalysis()

    def perform_analysis_with_progress(self, token: '_7521.TaskProgress'):
        """ 'PerformAnalysisWithProgress' is the original name of this method.

        Args:
            token (mastapy.TaskProgress)
        """

        self.wrapped.PerformAnalysisWithProgress(token.wrapped if token else None)

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
    def cast_to(self) -> 'ElectricMachineAnalysis._Cast_ElectricMachineAnalysis':
        return self._Cast_ElectricMachineAnalysis(self)
