"""_2605.py

DynamicAnalysis
"""
from mastapy.system_model.analyses_and_results.analysis_cases import _7506
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'DynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicAnalysis',)


class DynamicAnalysis(_7506.FEAnalysis):
    """DynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_ANALYSIS

    class _Cast_DynamicAnalysis:
        """Special nested class for casting DynamicAnalysis to subclasses."""

        def __init__(self, parent: 'DynamicAnalysis'):
            self._parent = parent

        @property
        def fe_analysis(self):
            return self._parent._cast(_7506.FEAnalysis)

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
        def dynamic_model_for_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3014
            
            return self._parent._cast(_3014.DynamicModelForSteadyStateSynchronousResponse)

        @property
        def dynamic_model_for_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _2609
            
            return self._parent._cast(_2609.DynamicModelForStabilityAnalysis)

        @property
        def dynamic_model_for_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _2608
            
            return self._parent._cast(_2608.DynamicModelForModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4882
            
            return self._parent._cast(_4882.DynamicModelAtAStiffness)

        @property
        def dynamic_model_for_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _2607
            
            return self._parent._cast(_2607.DynamicModelForHarmonicAnalysis)

        @property
        def dynamic_analysis(self) -> 'DynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DynamicAnalysis._Cast_DynamicAnalysis':
        return self._Cast_DynamicAnalysis(self)
