"""_3902.py

ConceptCouplingHalfCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2561
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3769
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3913
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'ConceptCouplingHalfCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalfCompoundStabilityAnalysis',)


class ConceptCouplingHalfCompoundStabilityAnalysis(_3913.CouplingHalfCompoundStabilityAnalysis):
    """ConceptCouplingHalfCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS

    class _Cast_ConceptCouplingHalfCompoundStabilityAnalysis:
        """Special nested class for casting ConceptCouplingHalfCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'ConceptCouplingHalfCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def coupling_half_compound_stability_analysis(self):
            return self._parent._cast(_3913.CouplingHalfCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3951
            
            return self._parent._cast(_3951.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3899
            
            return self._parent._cast(_3899.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3953
            
            return self._parent._cast(_3953.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(self) -> 'ConceptCouplingHalfCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalfCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2561.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3769.ConceptCouplingHalfStabilityAnalysis]':
        """List[ConceptCouplingHalfStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3769.ConceptCouplingHalfStabilityAnalysis]':
        """List[ConceptCouplingHalfStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptCouplingHalfCompoundStabilityAnalysis._Cast_ConceptCouplingHalfCompoundStabilityAnalysis':
        return self._Cast_ConceptCouplingHalfCompoundStabilityAnalysis(self)
