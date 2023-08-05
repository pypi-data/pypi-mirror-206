"""_6396.py

ClutchHalfCompoundDynamicAnalysis
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2558
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6266
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6412
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'ClutchHalfCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfCompoundDynamicAnalysis',)


class ClutchHalfCompoundDynamicAnalysis(_6412.CouplingHalfCompoundDynamicAnalysis):
    """ClutchHalfCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_ClutchHalfCompoundDynamicAnalysis:
        """Special nested class for casting ClutchHalfCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'ClutchHalfCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def coupling_half_compound_dynamic_analysis(self):
            return self._parent._cast(_6412.CouplingHalfCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6450
            
            return self._parent._cast(_6450.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6398
            
            return self._parent._cast(_6398.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6452
            
            return self._parent._cast(_6452.PartCompoundDynamicAnalysis)

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
        def clutch_half_compound_dynamic_analysis(self) -> 'ClutchHalfCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchHalfCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2558.ClutchHalf':
        """ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6266.ClutchHalfDynamicAnalysis]':
        """List[ClutchHalfDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6266.ClutchHalfDynamicAnalysis]':
        """List[ClutchHalfDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ClutchHalfCompoundDynamicAnalysis._Cast_ClutchHalfCompoundDynamicAnalysis':
        return self._Cast_ClutchHalfCompoundDynamicAnalysis(self)
