"""_2615.py

ModalAnalysisAtASpeed
"""
from mastapy.system_model.analyses_and_results import _2599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'ModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ModalAnalysisAtASpeed',)


class ModalAnalysisAtASpeed(_2599.SingleAnalysis):
    """ModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_ModalAnalysisAtASpeed:
        """Special nested class for casting ModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'ModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def single_analysis(self):
            return self._parent._cast(_2599.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def modal_analysis_at_a_speed(self) -> 'ModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ModalAnalysisAtASpeed._Cast_ModalAnalysisAtASpeed':
        return self._Cast_ModalAnalysisAtASpeed(self)
