"""_6234.py

CombinationAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMBINATION_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses', 'CombinationAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CombinationAnalysis',)


class CombinationAnalysis(_0.APIBase):
    """CombinationAnalysis

    This is a mastapy class.
    """

    TYPE = _COMBINATION_ANALYSIS

    class _Cast_CombinationAnalysis:
        """Special nested class for casting CombinationAnalysis to subclasses."""

        def __init__(self, parent: 'CombinationAnalysis'):
            self._parent = parent

        @property
        def flexible_pin_analysis(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6235
            
            return self._parent._cast(_6235.FlexiblePinAnalysis)

        @property
        def flexible_pin_analysis_concept_level(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6236
            
            return self._parent._cast(_6236.FlexiblePinAnalysisConceptLevel)

        @property
        def flexible_pin_analysis_detail_level_and_pin_fatigue_one_tooth_pass(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6237
            
            return self._parent._cast(_6237.FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass)

        @property
        def flexible_pin_analysis_gear_and_bearing_rating(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6238
            
            return self._parent._cast(_6238.FlexiblePinAnalysisGearAndBearingRating)

        @property
        def flexible_pin_analysis_manufacture_level(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6239
            
            return self._parent._cast(_6239.FlexiblePinAnalysisManufactureLevel)

        @property
        def flexible_pin_analysis_stop_start_analysis(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6241
            
            return self._parent._cast(_6241.FlexiblePinAnalysisStopStartAnalysis)

        @property
        def wind_turbine_certification_report(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6242
            
            return self._parent._cast(_6242.WindTurbineCertificationReport)

        @property
        def combination_analysis(self) -> 'CombinationAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CombinationAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self) -> 'CombinationAnalysis._Cast_CombinationAnalysis':
        return self._Cast_CombinationAnalysis(self)
