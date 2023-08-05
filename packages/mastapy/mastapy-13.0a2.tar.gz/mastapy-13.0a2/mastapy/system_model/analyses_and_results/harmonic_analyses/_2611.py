"""_2611.py

HarmonicAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6037
from mastapy.system_model.analyses_and_results.analysis_cases import _7499
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'HarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysis',)


class HarmonicAnalysis(_7499.CompoundAnalysisCase):
    """HarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS

    class _Cast_HarmonicAnalysis:
        """Special nested class for casting HarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysis'):
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
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _2612
            
            return self._parent._cast(_2612.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation)

        @property
        def harmonic_analysis(self) -> 'HarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def time_for_modal_analysis(self) -> 'float':
        """float: 'TimeForModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeForModalAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def time_for_single_excitations_post_analysis(self) -> 'float':
        """float: 'TimeForSingleExcitationsPostAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeForSingleExcitationsPostAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_run_single_excitations(self) -> 'float':
        """float: 'TimeToRunSingleExcitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeToRunSingleExcitations

        if temp is None:
            return 0.0

        return temp

    @property
    def harmonic_analyses_of_single_excitations(self) -> 'List[_6037.HarmonicAnalysisOfSingleExcitation]':
        """List[HarmonicAnalysisOfSingleExcitation]: 'HarmonicAnalysesOfSingleExcitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysesOfSingleExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'HarmonicAnalysis._Cast_HarmonicAnalysis':
        return self._Cast_HarmonicAnalysis(self)
