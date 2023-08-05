"""_5261.py

CycloidalAssemblyCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.part_model.cycloidal import _2547
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5132
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5316
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'CycloidalAssemblyCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalAssemblyCompoundModalAnalysisAtASpeed',)


class CycloidalAssemblyCompoundModalAnalysisAtASpeed(_5316.SpecialisedAssemblyCompoundModalAnalysisAtASpeed):
    """CycloidalAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CycloidalAssemblyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'CycloidalAssemblyCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5316.SpecialisedAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5218
            
            return self._parent._cast(_5218.AbstractAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5297
            
            return self._parent._cast(_5297.PartCompoundModalAnalysisAtASpeed)

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
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(self) -> 'CycloidalAssemblyCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalAssemblyCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2547.CycloidalAssembly':
        """CycloidalAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2547.CycloidalAssembly':
        """CycloidalAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5132.CycloidalAssemblyModalAnalysisAtASpeed]':
        """List[CycloidalAssemblyModalAnalysisAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5132.CycloidalAssemblyModalAnalysisAtASpeed]':
        """List[CycloidalAssemblyModalAnalysisAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalAssemblyCompoundModalAnalysisAtASpeed._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed':
        return self._Cast_CycloidalAssemblyCompoundModalAnalysisAtASpeed(self)
