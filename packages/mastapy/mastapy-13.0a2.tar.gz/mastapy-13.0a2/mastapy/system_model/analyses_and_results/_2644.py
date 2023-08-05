"""_2644.py

CompoundDynamicModelForModalAnalysis
"""
from mastapy.system_model.analyses_and_results import _2598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_DYNAMIC_MODEL_FOR_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundDynamicModelForModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundDynamicModelForModalAnalysis',)


class CompoundDynamicModelForModalAnalysis(_2598.CompoundAnalysis):
    """CompoundDynamicModelForModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_DYNAMIC_MODEL_FOR_MODAL_ANALYSIS

    class _Cast_CompoundDynamicModelForModalAnalysis:
        """Special nested class for casting CompoundDynamicModelForModalAnalysis to subclasses."""

        def __init__(self, parent: 'CompoundDynamicModelForModalAnalysis'):
            self._parent = parent

        @property
        def compound_analysis(self):
            return self._parent._cast(_2598.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def compound_dynamic_model_for_modal_analysis(self) -> 'CompoundDynamicModelForModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CompoundDynamicModelForModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CompoundDynamicModelForModalAnalysis._Cast_CompoundDynamicModelForModalAnalysis':
        return self._Cast_CompoundDynamicModelForModalAnalysis(self)
