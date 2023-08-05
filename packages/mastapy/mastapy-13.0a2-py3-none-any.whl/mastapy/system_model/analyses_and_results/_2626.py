"""_2626.py

TorsionalSystemDeflectionAnalysis
"""
from mastapy.system_model.analyses_and_results import _2599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORSIONAL_SYSTEM_DEFLECTION_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'TorsionalSystemDeflectionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorsionalSystemDeflectionAnalysis',)


class TorsionalSystemDeflectionAnalysis(_2599.SingleAnalysis):
    """TorsionalSystemDeflectionAnalysis

    This is a mastapy class.
    """

    TYPE = _TORSIONAL_SYSTEM_DEFLECTION_ANALYSIS

    class _Cast_TorsionalSystemDeflectionAnalysis:
        """Special nested class for casting TorsionalSystemDeflectionAnalysis to subclasses."""

        def __init__(self, parent: 'TorsionalSystemDeflectionAnalysis'):
            self._parent = parent

        @property
        def single_analysis(self):
            return self._parent._cast(_2599.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def torsional_system_deflection_analysis(self) -> 'TorsionalSystemDeflectionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorsionalSystemDeflectionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TorsionalSystemDeflectionAnalysis._Cast_TorsionalSystemDeflectionAnalysis':
        return self._Cast_TorsionalSystemDeflectionAnalysis(self)
