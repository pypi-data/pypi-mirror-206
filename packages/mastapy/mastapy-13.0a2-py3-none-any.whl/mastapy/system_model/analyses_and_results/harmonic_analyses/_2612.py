"""_2612.py

HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
"""
from mastapy.system_model.analyses_and_results.harmonic_analyses import _2611
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation',)


class HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(_2611.HarmonicAnalysis):
    """HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def harmonic_analysis(self):
            return self._parent._cast(_2611.HarmonicAnalysis)

        @property
        def compound_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7499
            
            return self._parent._cast(_7499.CompoundAnalysisCase)

        @property
        def static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.StaticLoadAnalysisCase)

        @property
        def analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7497
            
            return self._parent._cast(_7497.AnalysisCase)

        @property
        def context(self):
            from mastapy.system_model.analyses_and_results import _2629
            
            return self._parent._cast(_2629.Context)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(self) -> 'HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(self)
