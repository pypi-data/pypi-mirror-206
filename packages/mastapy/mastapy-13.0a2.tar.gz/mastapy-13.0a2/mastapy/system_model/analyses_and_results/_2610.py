"""_2610.py

DynamicModelForSteadyStateSynchronousResponseAnalysis
"""
from mastapy.system_model.analyses_and_results import _2599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_FOR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'DynamicModelForSteadyStateSynchronousResponseAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicModelForSteadyStateSynchronousResponseAnalysis',)


class DynamicModelForSteadyStateSynchronousResponseAnalysis(_2599.SingleAnalysis):
    """DynamicModelForSteadyStateSynchronousResponseAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_FOR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS

    class _Cast_DynamicModelForSteadyStateSynchronousResponseAnalysis:
        """Special nested class for casting DynamicModelForSteadyStateSynchronousResponseAnalysis to subclasses."""

        def __init__(self, parent: 'DynamicModelForSteadyStateSynchronousResponseAnalysis'):
            self._parent = parent

        @property
        def single_analysis(self):
            return self._parent._cast(_2599.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def dynamic_model_for_steady_state_synchronous_response_analysis(self) -> 'DynamicModelForSteadyStateSynchronousResponseAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicModelForSteadyStateSynchronousResponseAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_DynamicModelForSteadyStateSynchronousResponseAnalysis':
        return self._Cast_DynamicModelForSteadyStateSynchronousResponseAnalysis(self)
