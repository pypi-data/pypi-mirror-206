"""_2661.py

CompoundTorsionalSystemDeflectionAnalysis
"""
from mastapy.system_model.analyses_and_results import _2598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_TORSIONAL_SYSTEM_DEFLECTION_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundTorsionalSystemDeflectionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundTorsionalSystemDeflectionAnalysis',)


class CompoundTorsionalSystemDeflectionAnalysis(_2598.CompoundAnalysis):
    """CompoundTorsionalSystemDeflectionAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_TORSIONAL_SYSTEM_DEFLECTION_ANALYSIS

    class _Cast_CompoundTorsionalSystemDeflectionAnalysis:
        """Special nested class for casting CompoundTorsionalSystemDeflectionAnalysis to subclasses."""

        def __init__(self, parent: 'CompoundTorsionalSystemDeflectionAnalysis'):
            self._parent = parent

        @property
        def compound_analysis(self):
            return self._parent._cast(_2598.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def compound_torsional_system_deflection_analysis(self) -> 'CompoundTorsionalSystemDeflectionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CompoundTorsionalSystemDeflectionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CompoundTorsionalSystemDeflectionAnalysis._Cast_CompoundTorsionalSystemDeflectionAnalysis':
        return self._Cast_CompoundTorsionalSystemDeflectionAnalysis(self)
