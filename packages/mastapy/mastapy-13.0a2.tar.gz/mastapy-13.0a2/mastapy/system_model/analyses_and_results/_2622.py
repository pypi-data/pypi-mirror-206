"""_2622.py

SteadyStateSynchronousResponseAnalysis
"""
from mastapy.system_model.analyses_and_results import _2599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'SteadyStateSynchronousResponseAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SteadyStateSynchronousResponseAnalysis',)


class SteadyStateSynchronousResponseAnalysis(_2599.SingleAnalysis):
    """SteadyStateSynchronousResponseAnalysis

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS

    class _Cast_SteadyStateSynchronousResponseAnalysis:
        """Special nested class for casting SteadyStateSynchronousResponseAnalysis to subclasses."""

        def __init__(self, parent: 'SteadyStateSynchronousResponseAnalysis'):
            self._parent = parent

        @property
        def single_analysis(self):
            return self._parent._cast(_2599.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def steady_state_synchronous_response_analysis(self) -> 'SteadyStateSynchronousResponseAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SteadyStateSynchronousResponseAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SteadyStateSynchronousResponseAnalysis._Cast_SteadyStateSynchronousResponseAnalysis':
        return self._Cast_SteadyStateSynchronousResponseAnalysis(self)
