"""_2653.py

CompoundModalAnalysisForHarmonicAnalysis
"""
from mastapy.system_model.analyses_and_results import _2598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_MODAL_ANALYSIS_FOR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundModalAnalysisForHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundModalAnalysisForHarmonicAnalysis',)


class CompoundModalAnalysisForHarmonicAnalysis(_2598.CompoundAnalysis):
    """CompoundModalAnalysisForHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_MODAL_ANALYSIS_FOR_HARMONIC_ANALYSIS

    class _Cast_CompoundModalAnalysisForHarmonicAnalysis:
        """Special nested class for casting CompoundModalAnalysisForHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'CompoundModalAnalysisForHarmonicAnalysis'):
            self._parent = parent

        @property
        def compound_analysis(self):
            return self._parent._cast(_2598.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def compound_modal_analysis_for_harmonic_analysis(self) -> 'CompoundModalAnalysisForHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CompoundModalAnalysisForHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CompoundModalAnalysisForHarmonicAnalysis._Cast_CompoundModalAnalysisForHarmonicAnalysis':
        return self._Cast_CompoundModalAnalysisForHarmonicAnalysis(self)
