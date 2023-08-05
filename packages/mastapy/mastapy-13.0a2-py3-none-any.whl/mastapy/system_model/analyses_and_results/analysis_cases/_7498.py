"""_7498.py

AbstractAnalysisOptions
"""
from typing import TypeVar, Generic

from mastapy import _0
from mastapy.system_model.analyses_and_results.static_loads import _6768
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ANALYSIS_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'AbstractAnalysisOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAnalysisOptions',)


T = TypeVar('T', bound='_6768.LoadCase')


class AbstractAnalysisOptions(_0.APIBase, Generic[T]):
    """AbstractAnalysisOptions

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _ABSTRACT_ANALYSIS_OPTIONS

    class _Cast_AbstractAnalysisOptions:
        """Special nested class for casting AbstractAnalysisOptions to subclasses."""

        def __init__(self, parent: 'AbstractAnalysisOptions'):
            self._parent = parent

        @property
        def system_deflection_options(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2806
            
            return self._parent._cast(_2806.SystemDeflectionOptions)

        @property
        def frequency_response_analysis_options(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608
            
            return self._parent._cast(_4608.FrequencyResponseAnalysisOptions)

        @property
        def mbd_run_up_analysis_options(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433
            
            return self._parent._cast(_5433.MBDRunUpAnalysisOptions)

        @property
        def frequency_options_for_harmonic_analysis_results(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5721
            
            return self._parent._cast(_5721.FrequencyOptionsForHarmonicAnalysisResults)

        @property
        def speed_options_for_harmonic_analysis_results(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5778
            
            return self._parent._cast(_5778.SpeedOptionsForHarmonicAnalysisResults)

        @property
        def stiffness_options_for_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5785
            
            return self._parent._cast(_5785.StiffnessOptionsForHarmonicAnalysis)

        @property
        def abstract_analysis_options(self) -> 'AbstractAnalysisOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAnalysisOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AbstractAnalysisOptions._Cast_AbstractAnalysisOptions':
        return self._Cast_AbstractAnalysisOptions(self)
