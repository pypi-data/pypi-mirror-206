"""_7236.py

AdvancedSystemDeflection
"""
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7237
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'AdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('AdvancedSystemDeflection',)


class AdvancedSystemDeflection(_7512.StaticLoadAnalysisCase):
    """AdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ADVANCED_SYSTEM_DEFLECTION

    class _Cast_AdvancedSystemDeflection:
        """Special nested class for casting AdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'AdvancedSystemDeflection'):
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
        def advanced_system_deflection(self) -> 'AdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_system_deflection_options(self) -> '_7237.AdvancedSystemDeflectionOptions':
        """AdvancedSystemDeflectionOptions: 'AdvancedSystemDeflectionOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedSystemDeflectionOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AdvancedSystemDeflection._Cast_AdvancedSystemDeflection':
        return self._Cast_AdvancedSystemDeflection(self)
