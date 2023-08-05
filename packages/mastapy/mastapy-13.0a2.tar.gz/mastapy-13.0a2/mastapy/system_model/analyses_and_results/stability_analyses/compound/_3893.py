"""_3893.py

BoltCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2422
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3762
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3899
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'BoltCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltCompoundStabilityAnalysis',)


class BoltCompoundStabilityAnalysis(_3899.ComponentCompoundStabilityAnalysis):
    """BoltCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLT_COMPOUND_STABILITY_ANALYSIS

    class _Cast_BoltCompoundStabilityAnalysis:
        """Special nested class for casting BoltCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'BoltCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def component_compound_stability_analysis(self):
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
        def bolt_compound_stability_analysis(self) -> 'BoltCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoltCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2422.Bolt':
        """Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3762.BoltStabilityAnalysis]':
        """List[BoltStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3762.BoltStabilityAnalysis]':
        """List[BoltStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BoltCompoundStabilityAnalysis._Cast_BoltCompoundStabilityAnalysis':
        return self._Cast_BoltCompoundStabilityAnalysis(self)
