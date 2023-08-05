"""_657.py

CalculateProfileDeviationAccuracy
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _673
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CALCULATE_PROFILE_DEVIATION_ACCURACY = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'CalculateProfileDeviationAccuracy')


__docformat__ = 'restructuredtext en'
__all__ = ('CalculateProfileDeviationAccuracy',)


class CalculateProfileDeviationAccuracy(_0.APIBase):
    """CalculateProfileDeviationAccuracy

    This is a mastapy class.
    """

    TYPE = _CALCULATE_PROFILE_DEVIATION_ACCURACY

    class _Cast_CalculateProfileDeviationAccuracy:
        """Special nested class for casting CalculateProfileDeviationAccuracy to subclasses."""

        def __init__(self, parent: 'CalculateProfileDeviationAccuracy'):
            self._parent = parent

        @property
        def calculate_profile_deviation_accuracy(self) -> 'CalculateProfileDeviationAccuracy':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CalculateProfileDeviationAccuracy.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def achieved_profile_agma20151a01_quality_grade(self) -> 'float':
        """float: 'AchievedProfileAGMA20151A01QualityGrade' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AchievedProfileAGMA20151A01QualityGrade

        if temp is None:
            return 0.0

        return temp

    @property
    def achieved_profile_iso132811995e_quality_grade(self) -> 'float':
        """float: 'AchievedProfileISO132811995EQualityGrade' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AchievedProfileISO132811995EQualityGrade

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
    def profile_deviation_agma20151a01_quality_grade_designed(self) -> 'float':
        """float: 'ProfileDeviationAGMA20151A01QualityGradeDesigned' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileDeviationAGMA20151A01QualityGradeDesigned

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_deviation_iso132811995e_quality_grade_designed(self) -> 'float':
        """float: 'ProfileDeviationISO132811995EQualityGradeDesigned' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileDeviationISO132811995EQualityGradeDesigned

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_form_deviation(self) -> 'float':
        """float: 'ProfileFormDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_form_deviation_agma20151a01_quality_grade_obtained(self) -> 'float':
        """float: 'ProfileFormDeviationAGMA20151A01QualityGradeObtained' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormDeviationAGMA20151A01QualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_form_deviation_iso132811995e_quality_grade_obtained(self) -> 'float':
        """float: 'ProfileFormDeviationISO132811995EQualityGradeObtained' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormDeviationISO132811995EQualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_slope_deviation(self) -> 'float':
        """float: 'ProfileSlopeDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_slope_deviation_agma20151a01_quality_grade_obtained(self) -> 'float':
        """float: 'ProfileSlopeDeviationAGMA20151A01QualityGradeObtained' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeDeviationAGMA20151A01QualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_slope_deviation_iso132811995e_quality_grade_obtained(self) -> 'float':
        """float: 'ProfileSlopeDeviationISO132811995EQualityGradeObtained' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeDeviationISO132811995EQualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def total_profile_deviation(self) -> 'float':
        """float: 'TotalProfileDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalProfileDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def total_profile_deviation_agma20151a01_quality_grade_obtained(self) -> 'float':
        """float: 'TotalProfileDeviationAGMA20151A01QualityGradeObtained' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalProfileDeviationAGMA20151A01QualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def total_profile_deviation_iso132811995e_quality_grade_obtained(self) -> 'float':
        """float: 'TotalProfileDeviationISO132811995EQualityGradeObtained' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalProfileDeviationISO132811995EQualityGradeObtained

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
    def cast_to(self) -> 'CalculateProfileDeviationAccuracy._Cast_CalculateProfileDeviationAccuracy':
        return self._Cast_CalculateProfileDeviationAccuracy(self)
