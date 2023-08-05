"""_655.py

CalculateLeadDeviationAccuracy
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _673
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CALCULATE_LEAD_DEVIATION_ACCURACY = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'CalculateLeadDeviationAccuracy')


__docformat__ = 'restructuredtext en'
__all__ = ('CalculateLeadDeviationAccuracy',)


class CalculateLeadDeviationAccuracy(_0.APIBase):
    """CalculateLeadDeviationAccuracy

    This is a mastapy class.
    """

    TYPE = _CALCULATE_LEAD_DEVIATION_ACCURACY

    class _Cast_CalculateLeadDeviationAccuracy:
        """Special nested class for casting CalculateLeadDeviationAccuracy to subclasses."""

        def __init__(self, parent: 'CalculateLeadDeviationAccuracy'):
            self._parent = parent

        @property
        def calculate_lead_deviation_accuracy(self) -> 'CalculateLeadDeviationAccuracy':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CalculateLeadDeviationAccuracy.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def achieved_lead_agma20151a01_quality_grade(self) -> 'float':
        """float: 'AchievedLeadAGMA20151A01QualityGrade' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AchievedLeadAGMA20151A01QualityGrade

        if temp is None:
            return 0.0

        return temp

    @property
    def achieved_lead_iso132811995e_quality_grade(self) -> 'float':
        """float: 'AchievedLeadISO132811995EQualityGrade' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AchievedLeadISO132811995EQualityGrade

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_name(self) -> 'str':
        """str: 'FlankName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankName

        if temp is None:
            return ''

        return temp

    @property
    def helix_deviation_agma20151a01_quality_grade_designed(self) -> 'float':
        """float: 'HelixDeviationAGMA20151A01QualityGradeDesigned' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixDeviationAGMA20151A01QualityGradeDesigned

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_deviation_iso132811995e_quality_grade_designed(self) -> 'float':
        """float: 'HelixDeviationISO132811995EQualityGradeDesigned' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixDeviationISO132811995EQualityGradeDesigned

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_form_deviation(self) -> 'float':
        """float: 'HelixFormDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixFormDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_form_deviation_agma20151a01_quality_grade_obtained(self) -> 'float':
        """float: 'HelixFormDeviationAGMA20151A01QualityGradeObtained' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixFormDeviationAGMA20151A01QualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_form_deviation_iso132811995e_quality_grade_obtained(self) -> 'float':
        """float: 'HelixFormDeviationISO132811995EQualityGradeObtained' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixFormDeviationISO132811995EQualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_slope_deviation(self) -> 'float':
        """float: 'HelixSlopeDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixSlopeDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_slope_deviation_agma20151a01_quality_grade_obtained(self) -> 'float':
        """float: 'HelixSlopeDeviationAGMA20151A01QualityGradeObtained' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixSlopeDeviationAGMA20151A01QualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_slope_deviation_iso132811995e_quality_grade_obtained(self) -> 'float':
        """float: 'HelixSlopeDeviationISO132811995EQualityGradeObtained' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixSlopeDeviationISO132811995EQualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def total_helix_deviation(self) -> 'float':
        """float: 'TotalHelixDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalHelixDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def total_helix_deviation_agma20151a01_quality_grade_obtained(self) -> 'float':
        """float: 'TotalHelixDeviationAGMA20151A01QualityGradeObtained' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalHelixDeviationAGMA20151A01QualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def total_helix_deviation_iso132811995e_quality_grade_obtained(self) -> 'float':
        """float: 'TotalHelixDeviationISO132811995EQualityGradeObtained' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalHelixDeviationISO132811995EQualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def manufactured_agma20151a01_quality_grades(self) -> 'List[_673.ManufacturedQualityGrade]':
        """List[ManufacturedQualityGrade]: 'ManufacturedAGMA20151A01QualityGrades' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturedAGMA20151A01QualityGrades

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def manufactured_iso132811995e_quality_grades(self) -> 'List[_673.ManufacturedQualityGrade]':
        """List[ManufacturedQualityGrade]: 'ManufacturedISO132811995EQualityGrades' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturedISO132811995EQualityGrades

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
    def cast_to(self) -> 'CalculateLeadDeviationAccuracy._Cast_CalculateLeadDeviationAccuracy':
        return self._Cast_CalculateLeadDeviationAccuracy(self)
