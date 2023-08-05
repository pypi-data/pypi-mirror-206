"""_6394.py

ClutchCompoundDynamicAnalysis
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2557
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6265
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6410
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'ClutchCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchCompoundDynamicAnalysis',)


class ClutchCompoundDynamicAnalysis(_6410.CouplingCompoundDynamicAnalysis):
    """ClutchCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_ClutchCompoundDynamicAnalysis:
        """Special nested class for casting ClutchCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'ClutchCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def coupling_compound_dynamic_analysis(self):
            return self._parent._cast(_6410.CouplingCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6471
            
            return self._parent._cast(_6471.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6373
            
            return self._parent._cast(_6373.AbstractAssemblyCompoundDynamicAnalysis)

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
        def clutch_compound_dynamic_analysis(self) -> 'ClutchCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2557.Clutch':
        """Clutch: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2557.Clutch':
        """Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6265.ClutchDynamicAnalysis]':
        """List[ClutchDynamicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6265.ClutchDynamicAnalysis]':
        """List[ClutchDynamicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ClutchCompoundDynamicAnalysis._Cast_ClutchCompoundDynamicAnalysis':
        return self._Cast_ClutchCompoundDynamicAnalysis(self)
