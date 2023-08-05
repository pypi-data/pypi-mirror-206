"""_5884.py

CouplingConnectionCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5687
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'CouplingConnectionCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundHarmonicAnalysis',)


class CouplingConnectionCompoundHarmonicAnalysis(_5911.InterMountableComponentConnectionCompoundHarmonicAnalysis):
    """CouplingConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_CouplingConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting CouplingConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingConnectionCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(self):
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
        def clutch_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5868
            
            return self._parent._cast(_5868.ClutchConnectionCompoundHarmonicAnalysis)

        @property
        def concept_coupling_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5873
            
            return self._parent._cast(_5873.ConceptCouplingConnectionCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5927
            
            return self._parent._cast(_5927.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis)

        @property
        def spring_damper_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5949
            
            return self._parent._cast(_5949.SpringDamperConnectionCompoundHarmonicAnalysis)

        @property
        def torque_converter_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5964
            
            return self._parent._cast(_5964.TorqueConverterConnectionCompoundHarmonicAnalysis)

        @property
        def coupling_connection_compound_harmonic_analysis(self) -> 'CouplingConnectionCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_5687.CouplingConnectionHarmonicAnalysis]':
        """List[CouplingConnectionHarmonicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5687.CouplingConnectionHarmonicAnalysis]':
        """List[CouplingConnectionHarmonicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingConnectionCompoundHarmonicAnalysis._Cast_CouplingConnectionCompoundHarmonicAnalysis':
        return self._Cast_CouplingConnectionCompoundHarmonicAnalysis(self)
