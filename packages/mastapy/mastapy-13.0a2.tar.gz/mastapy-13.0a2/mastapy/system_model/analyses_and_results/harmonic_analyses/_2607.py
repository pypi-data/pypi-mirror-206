"""_2607.py

DynamicModelForHarmonicAnalysis
"""
from mastapy.system_model.analyses_and_results.dynamic_analyses import _2605
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_FOR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'DynamicModelForHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicModelForHarmonicAnalysis',)


class DynamicModelForHarmonicAnalysis(_2605.DynamicAnalysis):
    """DynamicModelForHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_FOR_HARMONIC_ANALYSIS

    class _Cast_DynamicModelForHarmonicAnalysis:
        """Special nested class for casting DynamicModelForHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'DynamicModelForHarmonicAnalysis'):
            self._parent = parent

        @property
        def dynamic_analysis(self):
            return self._parent._cast(_2605.DynamicAnalysis)

        @property
        def fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7506
            
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
        def dynamic_model_for_harmonic_analysis(self) -> 'DynamicModelForHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicModelForHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DynamicModelForHarmonicAnalysis._Cast_DynamicModelForHarmonicAnalysis':
        return self._Cast_DynamicModelForHarmonicAnalysis(self)
