"""_6461.py

PulleyCompoundDynamicAnalysis
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2569
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6412
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'PulleyCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyCompoundDynamicAnalysis',)


class PulleyCompoundDynamicAnalysis(_6412.CouplingHalfCompoundDynamicAnalysis):
    """PulleyCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_PulleyCompoundDynamicAnalysis:
        """Special nested class for casting PulleyCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'PulleyCompoundDynamicAnalysis'):
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
        def cvt_pulley_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6415
            
            return self._parent._cast(_6415.CVTPulleyCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(self) -> 'PulleyCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PulleyCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2569.Pulley':
        """Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6332.PulleyDynamicAnalysis]':
        """List[PulleyDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6332.PulleyDynamicAnalysis]':
        """List[PulleyDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis':
        return self._Cast_PulleyCompoundDynamicAnalysis(self)
