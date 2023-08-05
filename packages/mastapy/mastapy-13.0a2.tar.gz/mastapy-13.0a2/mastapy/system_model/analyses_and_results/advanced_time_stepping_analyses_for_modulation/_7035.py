"""_7035.py

HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5733
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_OPTIONS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation',)


class HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation(_5733.HarmonicAnalysisOptions):
    """HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_OPTIONS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def harmonic_analysis_options(self):
            return self._parent._cast(_5733.HarmonicAnalysisOptions)

        @property
        def harmonic_analysis_options_for_advanced_time_stepping_analysis_for_modulation(self) -> 'HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculate_uncoupled_modes_during_analysis(self) -> 'bool':
        """bool: 'CalculateUncoupledModesDuringAnalysis' is the original name of this property."""

        temp = self.wrapped.CalculateUncoupledModesDuringAnalysis

        if temp is None:
            return False

        return temp

    @calculate_uncoupled_modes_during_analysis.setter
    def calculate_uncoupled_modes_during_analysis(self, value: 'bool'):
        self.wrapped.CalculateUncoupledModesDuringAnalysis = bool(value) if value else False

    @property
    def crop_to_speed_range_for_export_and_reports(self) -> 'bool':
        """bool: 'CropToSpeedRangeForExportAndReports' is the original name of this property."""

        temp = self.wrapped.CropToSpeedRangeForExportAndReports

        if temp is None:
            return False

        return temp

    @crop_to_speed_range_for_export_and_reports.setter
    def crop_to_speed_range_for_export_and_reports(self, value: 'bool'):
        self.wrapped.CropToSpeedRangeForExportAndReports = bool(value) if value else False

    @property
    def cast_to(self) -> 'HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation(self)
