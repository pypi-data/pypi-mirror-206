"""_3329.py

SteadyStateSynchronousResponseOnAShaft
"""
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3070
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'SteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('SteadyStateSynchronousResponseOnAShaft',)


class SteadyStateSynchronousResponseOnAShaft(_7512.StaticLoadAnalysisCase):
    """SteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_SteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'SteadyStateSynchronousResponseOnAShaft'):
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
        def steady_state_synchronous_response_on_a_shaft(self) -> 'SteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def options(self) -> '_3070.SteadyStateSynchronousResponseOptions':
        """SteadyStateSynchronousResponseOptions: 'Options' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Options

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SteadyStateSynchronousResponseOnAShaft._Cast_SteadyStateSynchronousResponseOnAShaft':
        return self._Cast_SteadyStateSynchronousResponseOnAShaft(self)
