"""_2604.py

CriticalSpeedAnalysis
"""
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6549
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'CriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CriticalSpeedAnalysis',)


class CriticalSpeedAnalysis(_7512.StaticLoadAnalysisCase):
    """CriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CRITICAL_SPEED_ANALYSIS

    class _Cast_CriticalSpeedAnalysis:
        """Special nested class for casting CriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'CriticalSpeedAnalysis'):
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
        def critical_speed_analysis(self) -> 'CriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def critical_speed_analysis_options(self) -> '_6549.CriticalSpeedAnalysisOptions':
        """CriticalSpeedAnalysisOptions: 'CriticalSpeedAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalSpeedAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis':
        return self._Cast_CriticalSpeedAnalysis(self)
