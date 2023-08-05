"""_2642.py

CompoundDynamicModelAtAStiffnessAnalysis
"""
from mastapy.system_model.analyses_and_results import _2598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_DYNAMIC_MODEL_AT_A_STIFFNESS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundDynamicModelAtAStiffnessAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundDynamicModelAtAStiffnessAnalysis',)


class CompoundDynamicModelAtAStiffnessAnalysis(_2598.CompoundAnalysis):
    """CompoundDynamicModelAtAStiffnessAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_DYNAMIC_MODEL_AT_A_STIFFNESS_ANALYSIS

    class _Cast_CompoundDynamicModelAtAStiffnessAnalysis:
        """Special nested class for casting CompoundDynamicModelAtAStiffnessAnalysis to subclasses."""

        def __init__(self, parent: 'CompoundDynamicModelAtAStiffnessAnalysis'):
            self._parent = parent

        @property
        def compound_analysis(self):
            return self._parent._cast(_2598.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def compound_dynamic_model_at_a_stiffness_analysis(self) -> 'CompoundDynamicModelAtAStiffnessAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CompoundDynamicModelAtAStiffnessAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CompoundDynamicModelAtAStiffnessAnalysis._Cast_CompoundDynamicModelAtAStiffnessAnalysis':
        return self._Cast_CompoundDynamicModelAtAStiffnessAnalysis(self)
