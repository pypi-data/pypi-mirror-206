"""_2615.py

ModalAnalysisAtASpeed
"""
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'ModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ModalAnalysisAtASpeed',)


class ModalAnalysisAtASpeed(_7512.StaticLoadAnalysisCase):
    """ModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_ModalAnalysisAtASpeed:
        """Special nested class for casting ModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'ModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def static_load_analysis_case(self):
            return self._parent._cast(_7512.StaticLoadAnalysisCase)

        @property
        def analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7497
            
            return self._parent._cast(_7497.AnalysisCase)

        @property
        def context(self):
            from mastapy.system_model.analyses_and_results import _2629
            
            return self._parent._cast(_2629.Context)

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
