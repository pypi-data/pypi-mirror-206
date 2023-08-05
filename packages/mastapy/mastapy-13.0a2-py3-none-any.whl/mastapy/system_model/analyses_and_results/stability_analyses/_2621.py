"""_2621.py

StabilityAnalysis
"""
from mastapy.system_model.analyses_and_results.stability_analyses import _3849
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'StabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StabilityAnalysis',)


class StabilityAnalysis(_7512.StaticLoadAnalysisCase):
    """StabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STABILITY_ANALYSIS

    class _Cast_StabilityAnalysis:
        """Special nested class for casting StabilityAnalysis to subclasses."""

        def __init__(self, parent: 'StabilityAnalysis'):
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
        def stability_analysis(self) -> 'StabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stability_analysis_options(self) -> '_3849.StabilityAnalysisOptions':
        """StabilityAnalysisOptions: 'StabilityAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StabilityAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StabilityAnalysis._Cast_StabilityAnalysis':
        return self._Cast_StabilityAnalysis(self)
