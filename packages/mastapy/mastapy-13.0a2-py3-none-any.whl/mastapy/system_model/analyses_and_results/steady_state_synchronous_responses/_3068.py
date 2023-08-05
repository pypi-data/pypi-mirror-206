"""_3068.py

SteadyStateSynchronousResponse
"""
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3070
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7499
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'SteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('SteadyStateSynchronousResponse',)


class SteadyStateSynchronousResponse(_7499.CompoundAnalysisCase):
    """SteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_SteadyStateSynchronousResponse:
        """Special nested class for casting SteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'SteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def compound_analysis_case(self):
            return self._parent._cast(_7499.CompoundAnalysisCase)

        @property
        def static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
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
        def steady_state_synchronous_response(self) -> 'SteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def steady_state_analysis_options(self) -> '_3070.SteadyStateSynchronousResponseOptions':
        """SteadyStateSynchronousResponseOptions: 'SteadyStateAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SteadyStateSynchronousResponse._Cast_SteadyStateSynchronousResponse':
        return self._Cast_SteadyStateSynchronousResponse(self)
