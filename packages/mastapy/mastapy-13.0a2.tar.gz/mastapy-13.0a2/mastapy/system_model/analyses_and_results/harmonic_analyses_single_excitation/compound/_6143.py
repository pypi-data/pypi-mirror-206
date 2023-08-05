"""_6143.py

CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6012
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6170
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation',)


class CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation(_6170.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation):
    """CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation'):
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
        def clutch_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6127
            
            return self._parent._cast(_6127.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6132
            
            return self._parent._cast(_6132.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6186
            
            return self._parent._cast(_6186.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6208
            
            return self._parent._cast(_6208.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6223
            
            return self._parent._cast(_6223.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_connection_compound_harmonic_analysis_of_single_excitation(self) -> 'CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6012.CouplingConnectionHarmonicAnalysisOfSingleExcitation]':
        """List[CouplingConnectionHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6012.CouplingConnectionHarmonicAnalysisOfSingleExcitation]':
        """List[CouplingConnectionHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation(self)
