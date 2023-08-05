"""_2602.py

AdvancedTimeSteppingAnalysisForModulation
"""
from mastapy.system_model.analyses_and_results.analysis_cases import _7499
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'AdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('AdvancedTimeSteppingAnalysisForModulation',)


class AdvancedTimeSteppingAnalysisForModulation(_7499.CompoundAnalysisCase):
    """AdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_AdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'AdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def compound_analysis_case(self):
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
        def advanced_time_stepping_analysis_for_modulation(self) -> 'AdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AdvancedTimeSteppingAnalysisForModulation._Cast_AdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_AdvancedTimeSteppingAnalysisForModulation(self)
