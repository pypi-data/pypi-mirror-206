"""_7314.py

MeasurementComponentAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model import _2443
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6886
from mastapy.system_model.analyses_and_results.system_deflections import _2759
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'MeasurementComponentAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentAdvancedSystemDeflection',)


class MeasurementComponentAdvancedSystemDeflection(_7361.VirtualComponentAdvancedSystemDeflection):
    """MeasurementComponentAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_MeasurementComponentAdvancedSystemDeflection:
        """Special nested class for casting MeasurementComponentAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'MeasurementComponentAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def virtual_component_advanced_system_deflection(self):
            return self._parent._cast(_7361.VirtualComponentAdvancedSystemDeflection)

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
        def measurement_component_advanced_system_deflection(self) -> 'MeasurementComponentAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeasurementComponentAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2443.MeasurementComponent':
        """MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6886.MeasurementComponentLoadCase':
        """MeasurementComponentLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2759.MeasurementComponentSystemDeflection]':
        """List[MeasurementComponentSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection':
        return self._Cast_MeasurementComponentAdvancedSystemDeflection(self)
