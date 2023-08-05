"""_2612.py

HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
"""
from mastapy.system_model.analyses_and_results import _2599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation',)


class HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(_2599.SingleAnalysis):
    """HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def single_analysis(self):
            return self._parent._cast(_2599.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

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
