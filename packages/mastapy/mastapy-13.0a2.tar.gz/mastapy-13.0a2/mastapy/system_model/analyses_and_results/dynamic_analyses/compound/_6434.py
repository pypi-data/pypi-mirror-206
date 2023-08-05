"""_6434.py

GuideDxfModelCompoundDynamicAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2435
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6398
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'GuideDxfModelCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelCompoundDynamicAnalysis',)


class GuideDxfModelCompoundDynamicAnalysis(_6398.ComponentCompoundDynamicAnalysis):
    """GuideDxfModelCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_GuideDxfModelCompoundDynamicAnalysis:
        """Special nested class for casting GuideDxfModelCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'GuideDxfModelCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def component_compound_dynamic_analysis(self):
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
        def guide_dxf_model_compound_dynamic_analysis(self) -> 'GuideDxfModelCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GuideDxfModelCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2435.GuideDxfModel':
        """GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6305.GuideDxfModelDynamicAnalysis]':
        """List[GuideDxfModelDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6305.GuideDxfModelDynamicAnalysis]':
        """List[GuideDxfModelDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GuideDxfModelCompoundDynamicAnalysis._Cast_GuideDxfModelCompoundDynamicAnalysis':
        return self._Cast_GuideDxfModelCompoundDynamicAnalysis(self)
