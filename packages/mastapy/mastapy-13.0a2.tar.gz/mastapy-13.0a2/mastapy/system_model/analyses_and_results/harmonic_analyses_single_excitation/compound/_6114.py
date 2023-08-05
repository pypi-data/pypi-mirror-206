"""_6114.py

BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.connections_and_sockets import _2249
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5984
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6170
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation',)


class BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation(_6170.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation):
    """BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6170.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6140
            
            return self._parent._cast(_6140.ConnectionCompoundHarmonicAnalysisOfSingleExcitation)

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
        def cvt_belt_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6145
            
            return self._parent._cast(_6145.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_connection_compound_harmonic_analysis_of_single_excitation(self) -> 'BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2249.BeltConnection':
        """BeltConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2249.BeltConnection':
        """BeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5984.BeltConnectionHarmonicAnalysisOfSingleExcitation]':
        """List[BeltConnectionHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5984.BeltConnectionHarmonicAnalysisOfSingleExcitation]':
        """List[BeltConnectionHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation(self)
