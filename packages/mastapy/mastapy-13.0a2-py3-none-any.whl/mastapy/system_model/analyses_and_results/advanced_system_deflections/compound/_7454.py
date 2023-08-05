"""_7454.py

PointLoadCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model import _2451
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7324
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7490
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'PointLoadCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadCompoundAdvancedSystemDeflection',)


class PointLoadCompoundAdvancedSystemDeflection(_7490.VirtualComponentCompoundAdvancedSystemDeflection):
    """PointLoadCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_PointLoadCompoundAdvancedSystemDeflection:
        """Special nested class for casting PointLoadCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'PointLoadCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def virtual_component_compound_advanced_system_deflection(self):
            return self._parent._cast(_7490.VirtualComponentCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7445
            
            return self._parent._cast(_7445.MountableComponentCompoundAdvancedSystemDeflection)

        @property
        def component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7393
            
            return self._parent._cast(_7393.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7447
            
            return self._parent._cast(_7447.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def point_load_compound_advanced_system_deflection(self) -> 'PointLoadCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PointLoadCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2451.PointLoad':
        """PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_7324.PointLoadAdvancedSystemDeflection]':
        """List[PointLoadAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_7324.PointLoadAdvancedSystemDeflection]':
        """List[PointLoadAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PointLoadCompoundAdvancedSystemDeflection._Cast_PointLoadCompoundAdvancedSystemDeflection':
        return self._Cast_PointLoadCompoundAdvancedSystemDeflection(self)
