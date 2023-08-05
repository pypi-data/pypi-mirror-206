"""_7316.py

OilSealAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model import _2446
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6890
from mastapy.system_model.analyses_and_results.system_deflections import _2763
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7271
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'OilSealAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('OilSealAdvancedSystemDeflection',)


class OilSealAdvancedSystemDeflection(_7271.ConnectorAdvancedSystemDeflection):
    """OilSealAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_OilSealAdvancedSystemDeflection:
        """Special nested class for casting OilSealAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'OilSealAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def connector_advanced_system_deflection(self):
            return self._parent._cast(_7271.ConnectorAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7315
            
            return self._parent._cast(_7315.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7260
            
            return self._parent._cast(_7260.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7317
            
            return self._parent._cast(_7317.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def oil_seal_advanced_system_deflection(self) -> 'OilSealAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OilSealAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2446.OilSeal':
        """OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6890.OilSealLoadCase':
        """OilSealLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2763.OilSealSystemDeflection]':
        """List[OilSealSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection':
        return self._Cast_OilSealAdvancedSystemDeflection(self)
