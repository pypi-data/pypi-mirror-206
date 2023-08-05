"""_2606.py

DynamicModelAtAStiffnessAnalysis
"""
from mastapy.system_model.analyses_and_results import _2599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_AT_A_STIFFNESS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'DynamicModelAtAStiffnessAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicModelAtAStiffnessAnalysis',)


class DynamicModelAtAStiffnessAnalysis(_2599.SingleAnalysis):
    """DynamicModelAtAStiffnessAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_AT_A_STIFFNESS_ANALYSIS

    class _Cast_DynamicModelAtAStiffnessAnalysis:
        """Special nested class for casting DynamicModelAtAStiffnessAnalysis to subclasses."""

        def __init__(self, parent: 'DynamicModelAtAStiffnessAnalysis'):
            self._parent = parent

        @property
        def single_analysis(self):
            return self._parent._cast(_2599.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def dynamic_model_at_a_stiffness_analysis(self) -> 'DynamicModelAtAStiffnessAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicModelAtAStiffnessAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DynamicModelAtAStiffnessAnalysis._Cast_DynamicModelAtAStiffnessAnalysis':
        return self._Cast_DynamicModelAtAStiffnessAnalysis(self)
