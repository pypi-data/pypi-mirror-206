"""_7294.py

FlexiblePinAssemblyAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model import _2434
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6852
from mastapy.system_model.analyses_and_results.system_deflections import _2737, _2757, _2780
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7333, _7283, _7336
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'FlexiblePinAssemblyAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblyAdvancedSystemDeflection',)


class FlexiblePinAssemblyAdvancedSystemDeflection(_7336.SpecialisedAssemblyAdvancedSystemDeflection):
    """FlexiblePinAssemblyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_FlexiblePinAssemblyAdvancedSystemDeflection:
        """Special nested class for casting FlexiblePinAssemblyAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'FlexiblePinAssemblyAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(self):
            return self._parent._cast(_7336.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7232
            
            return self._parent._cast(_7232.AbstractAssemblyAdvancedSystemDeflection)

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
        def flexible_pin_assembly_advanced_system_deflection(self) -> 'FlexiblePinAssemblyAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblyAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2434.FlexiblePinAssembly':
        """FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6852.FlexiblePinAssemblyLoadCase':
        """FlexiblePinAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2737.FlexiblePinAssemblySystemDeflection]':
        """List[FlexiblePinAssemblySystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def load_sharing_factor_reporters(self) -> 'List[_2757.LoadSharingFactorReporter]':
        """List[LoadSharingFactorReporter]: 'LoadSharingFactorReporters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadSharingFactorReporters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def pin_advanced_analyses(self) -> 'List[_7333.ShaftAdvancedSystemDeflection]':
        """List[ShaftAdvancedSystemDeflection]: 'PinAdvancedAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinAdvancedAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def pin_spindle_fit_advanced_analyses(self) -> 'List[_2780.ShaftHubConnectionSystemDeflection]':
        """List[ShaftHubConnectionSystemDeflection]: 'PinSpindleFitAdvancedAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinSpindleFitAdvancedAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planet_gear_analyses(self) -> 'List[_7283.CylindricalGearAdvancedSystemDeflection]':
        """List[CylindricalGearAdvancedSystemDeflection]: 'PlanetGearAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetGearAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spindle_advanced_analyses(self) -> 'List[_7333.ShaftAdvancedSystemDeflection]':
        """List[ShaftAdvancedSystemDeflection]: 'SpindleAdvancedAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpindleAdvancedAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FlexiblePinAssemblyAdvancedSystemDeflection._Cast_FlexiblePinAssemblyAdvancedSystemDeflection':
        return self._Cast_FlexiblePinAssemblyAdvancedSystemDeflection(self)
