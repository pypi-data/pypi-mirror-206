"""_2648.py

CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
"""
from mastapy.system_model.analyses_and_results import _2598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation',)


class CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(_2598.CompoundAnalysis):
    """CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COMPOUND_HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def compound_analysis(self):
            return self._parent._cast(_2598.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def compound_harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(self) -> 'CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(self)
