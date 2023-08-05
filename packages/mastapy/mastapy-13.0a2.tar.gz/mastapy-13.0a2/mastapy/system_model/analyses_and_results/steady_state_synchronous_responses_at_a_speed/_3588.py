"""_3588.py

SteadyStateSynchronousResponseAtASpeed
"""
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'SteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SteadyStateSynchronousResponseAtASpeed',)


class SteadyStateSynchronousResponseAtASpeed(_7512.StaticLoadAnalysisCase):
    """SteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_SteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'SteadyStateSynchronousResponseAtASpeed'):
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
        def steady_state_synchronous_response_at_a_speed(self) -> 'SteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SteadyStateSynchronousResponseAtASpeed._Cast_SteadyStateSynchronousResponseAtASpeed':
        return self._Cast_SteadyStateSynchronousResponseAtASpeed(self)
