"""_2638.py

CompoundAdvancedSystemDeflectionSubAnalysis
"""
from mastapy.system_model.analyses_and_results import _2598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundAdvancedSystemDeflectionSubAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundAdvancedSystemDeflectionSubAnalysis',)


class CompoundAdvancedSystemDeflectionSubAnalysis(_2598.CompoundAnalysis):
    """CompoundAdvancedSystemDeflectionSubAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS

    class _Cast_CompoundAdvancedSystemDeflectionSubAnalysis:
        """Special nested class for casting CompoundAdvancedSystemDeflectionSubAnalysis to subclasses."""

        def __init__(self, parent: 'CompoundAdvancedSystemDeflectionSubAnalysis'):
            self._parent = parent

        @property
        def compound_analysis(self):
            return self._parent._cast(_2598.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7515
            
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def compound_advanced_system_deflection_sub_analysis(self) -> 'CompoundAdvancedSystemDeflectionSubAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CompoundAdvancedSystemDeflectionSubAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CompoundAdvancedSystemDeflectionSubAnalysis._Cast_CompoundAdvancedSystemDeflectionSubAnalysis':
        return self._Cast_CompoundAdvancedSystemDeflectionSubAnalysis(self)
