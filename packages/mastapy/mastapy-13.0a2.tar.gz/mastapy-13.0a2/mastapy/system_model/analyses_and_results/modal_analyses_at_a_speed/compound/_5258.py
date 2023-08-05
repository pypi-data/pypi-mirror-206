"""_5258.py

CVTBeltConnectionCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5129
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'CVTBeltConnectionCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTBeltConnectionCompoundModalAnalysisAtASpeed',)


class CVTBeltConnectionCompoundModalAnalysisAtASpeed(_5227.BeltConnectionCompoundModalAnalysisAtASpeed):
    """CVTBeltConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CVTBeltConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'CVTBeltConnectionCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def belt_connection_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5227.BeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5283
            
            return self._parent._cast(_5283.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5253
            
            return self._parent._cast(_5253.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_speed(self) -> 'CVTBeltConnectionCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTBeltConnectionCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5129.CVTBeltConnectionModalAnalysisAtASpeed]':
        """List[CVTBeltConnectionModalAnalysisAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5129.CVTBeltConnectionModalAnalysisAtASpeed]':
        """List[CVTBeltConnectionModalAnalysisAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTBeltConnectionCompoundModalAnalysisAtASpeed._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed':
        return self._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed(self)
