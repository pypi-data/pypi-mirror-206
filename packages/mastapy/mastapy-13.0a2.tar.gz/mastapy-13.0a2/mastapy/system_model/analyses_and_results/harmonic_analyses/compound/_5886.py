"""_5886.py

CVTBeltConnectionCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5690
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5855
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'CVTBeltConnectionCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTBeltConnectionCompoundHarmonicAnalysis',)


class CVTBeltConnectionCompoundHarmonicAnalysis(_5855.BeltConnectionCompoundHarmonicAnalysis):
    """CVTBeltConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_CVTBeltConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting CVTBeltConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'CVTBeltConnectionCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def belt_connection_compound_harmonic_analysis(self):
            return self._parent._cast(_5855.BeltConnectionCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5911
            
            return self._parent._cast(_5911.InterMountableComponentConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5881
            
            return self._parent._cast(_5881.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis(self) -> 'CVTBeltConnectionCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTBeltConnectionCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5690.CVTBeltConnectionHarmonicAnalysis]':
        """List[CVTBeltConnectionHarmonicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5690.CVTBeltConnectionHarmonicAnalysis]':
        """List[CVTBeltConnectionHarmonicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTBeltConnectionCompoundHarmonicAnalysis._Cast_CVTBeltConnectionCompoundHarmonicAnalysis':
        return self._Cast_CVTBeltConnectionCompoundHarmonicAnalysis(self)
