"""_5274.py

FEPartCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.part_model import _2433
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5145
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5220
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'FEPartCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartCompoundModalAnalysisAtASpeed',)


class FEPartCompoundModalAnalysisAtASpeed(_5220.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed):
    """FEPartCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_FEPartCompoundModalAnalysisAtASpeed:
        """Special nested class for casting FEPartCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'FEPartCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5220.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5243
            
            return self._parent._cast(_5243.ComponentCompoundModalAnalysisAtASpeed)

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
        def fe_part_compound_modal_analysis_at_a_speed(self) -> 'FEPartCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEPartCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2433.FEPart':
        """FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5145.FEPartModalAnalysisAtASpeed]':
        """List[FEPartModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[FEPartCompoundModalAnalysisAtASpeed]':
        """List[FEPartCompoundModalAnalysisAtASpeed]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5145.FEPartModalAnalysisAtASpeed]':
        """List[FEPartModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FEPartCompoundModalAnalysisAtASpeed._Cast_FEPartCompoundModalAnalysisAtASpeed':
        return self._Cast_FEPartCompoundModalAnalysisAtASpeed(self)
