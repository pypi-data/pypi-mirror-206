"""_5269.py

DatumCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.part_model import _2428
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5140
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5243
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'DatumCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumCompoundModalAnalysisAtASpeed',)


class DatumCompoundModalAnalysisAtASpeed(_5243.ComponentCompoundModalAnalysisAtASpeed):
    """DatumCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_DatumCompoundModalAnalysisAtASpeed:
        """Special nested class for casting DatumCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'DatumCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def component_compound_modal_analysis_at_a_speed(self):
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
        def datum_compound_modal_analysis_at_a_speed(self) -> 'DatumCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DatumCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2428.Datum':
        """Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5140.DatumModalAnalysisAtASpeed]':
        """List[DatumModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5140.DatumModalAnalysisAtASpeed]':
        """List[DatumModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'DatumCompoundModalAnalysisAtASpeed._Cast_DatumCompoundModalAnalysisAtASpeed':
        return self._Cast_DatumCompoundModalAnalysisAtASpeed(self)
