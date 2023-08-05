"""_7499.py

CompoundAnalysisCase
"""
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_ANALYSIS_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'CompoundAnalysisCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundAnalysisCase',)


class CompoundAnalysisCase(_7512.StaticLoadAnalysisCase):
    """CompoundAnalysisCase

    This is a mastapy class.
    """

    TYPE = _COMPOUND_ANALYSIS_CASE

    class _Cast_CompoundAnalysisCase:
        """Special nested class for casting CompoundAnalysisCase to subclasses."""

        def __init__(self, parent: 'CompoundAnalysisCase'):
            self._parent = parent

        @property
        def static_load_analysis_case(self):
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
        def steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3068
            
            return self._parent._cast(_3068.SteadyStateSynchronousResponse)

        @property
        def harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _2611
            
            return self._parent._cast(_2611.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _2612
            
            return self._parent._cast(_2612.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _2602
            
            return self._parent._cast(_2602.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def compound_analysis_case(self) -> 'CompoundAnalysisCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CompoundAnalysisCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CompoundAnalysisCase._Cast_CompoundAnalysisCase':
        return self._Cast_CompoundAnalysisCase(self)
