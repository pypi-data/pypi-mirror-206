"""_2646.py

CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis
"""
from mastapy.system_model.analyses_and_results import _2598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_DYNAMIC_MODEL_FOR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis',)


class CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis(_2598.CompoundAnalysis):
    """CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_DYNAMIC_MODEL_FOR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS

    class _Cast_CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis:
        """Special nested class for casting CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis to subclasses."""

        def __init__(self, parent: 'CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis'):
            self._parent = parent

        @property
        def compound_analysis(self):
            return self._parent._cast(_2598.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def compound_dynamic_model_for_steady_state_synchronous_response_analysis(self) -> 'CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis':
        return self._Cast_CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis(self)
