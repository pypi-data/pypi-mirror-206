"""_3912.py

CouplingConnectionCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3779
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3939
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'CouplingConnectionCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundStabilityAnalysis',)


class CouplingConnectionCompoundStabilityAnalysis(_3939.InterMountableComponentConnectionCompoundStabilityAnalysis):
    """CouplingConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_STABILITY_ANALYSIS

    class _Cast_CouplingConnectionCompoundStabilityAnalysis:
        """Special nested class for casting CouplingConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingConnectionCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_stability_analysis(self):
            return self._parent._cast(_3939.InterMountableComponentConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3909
            
            return self._parent._cast(_3909.ConnectionCompoundStabilityAnalysis)

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
        def clutch_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3896
            
            return self._parent._cast(_3896.ClutchConnectionCompoundStabilityAnalysis)

        @property
        def concept_coupling_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3901
            
            return self._parent._cast(_3901.ConceptCouplingConnectionCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3955
            
            return self._parent._cast(_3955.PartToPartShearCouplingConnectionCompoundStabilityAnalysis)

        @property
        def spring_damper_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3977
            
            return self._parent._cast(_3977.SpringDamperConnectionCompoundStabilityAnalysis)

        @property
        def torque_converter_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3992
            
            return self._parent._cast(_3992.TorqueConverterConnectionCompoundStabilityAnalysis)

        @property
        def coupling_connection_compound_stability_analysis(self) -> 'CouplingConnectionCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_3779.CouplingConnectionStabilityAnalysis]':
        """List[CouplingConnectionStabilityAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3779.CouplingConnectionStabilityAnalysis]':
        """List[CouplingConnectionStabilityAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingConnectionCompoundStabilityAnalysis._Cast_CouplingConnectionCompoundStabilityAnalysis':
        return self._Cast_CouplingConnectionCompoundStabilityAnalysis(self)
