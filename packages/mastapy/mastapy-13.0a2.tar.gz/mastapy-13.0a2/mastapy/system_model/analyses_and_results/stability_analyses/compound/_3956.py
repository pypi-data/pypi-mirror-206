"""_3956.py

PartToPartShearCouplingHalfCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2568
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3824
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3913
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'PartToPartShearCouplingHalfCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalfCompoundStabilityAnalysis',)


class PartToPartShearCouplingHalfCompoundStabilityAnalysis(_3913.CouplingHalfCompoundStabilityAnalysis):
    """PartToPartShearCouplingHalfCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS

    class _Cast_PartToPartShearCouplingHalfCompoundStabilityAnalysis:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'PartToPartShearCouplingHalfCompoundStabilityAnalysis'):
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
        def part_to_part_shear_coupling_half_compound_stability_analysis(self) -> 'PartToPartShearCouplingHalfCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalfCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2568.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3824.PartToPartShearCouplingHalfStabilityAnalysis]':
        """List[PartToPartShearCouplingHalfStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3824.PartToPartShearCouplingHalfStabilityAnalysis]':
        """List[PartToPartShearCouplingHalfStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartToPartShearCouplingHalfCompoundStabilityAnalysis._Cast_PartToPartShearCouplingHalfCompoundStabilityAnalysis':
        return self._Cast_PartToPartShearCouplingHalfCompoundStabilityAnalysis(self)
