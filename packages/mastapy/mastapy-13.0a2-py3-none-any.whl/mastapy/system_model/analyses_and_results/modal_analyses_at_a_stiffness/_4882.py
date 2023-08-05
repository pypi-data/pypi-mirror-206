"""_4882.py

DynamicModelAtAStiffness
"""
from mastapy.system_model.analyses_and_results.dynamic_analyses import _2605
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'DynamicModelAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicModelAtAStiffness',)


class DynamicModelAtAStiffness(_2605.DynamicAnalysis):
    """DynamicModelAtAStiffness

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_AT_A_STIFFNESS

    class _Cast_DynamicModelAtAStiffness:
        """Special nested class for casting DynamicModelAtAStiffness to subclasses."""

        def __init__(self, parent: 'DynamicModelAtAStiffness'):
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
        def dynamic_model_at_a_stiffness(self) -> 'DynamicModelAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicModelAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness':
        return self._Cast_DynamicModelAtAStiffness(self)
