"""_7367.py

ZerolBevelGearSetAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model.gears import _2533
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6951
from mastapy.gears.rating.zerol_bevel import _367
from mastapy.system_model.analyses_and_results.system_deflections import _2819
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7365, _7366, _7253
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ZerolBevelGearSetAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetAdvancedSystemDeflection',)


class ZerolBevelGearSetAdvancedSystemDeflection(_7253.BevelGearSetAdvancedSystemDeflection):
    """ZerolBevelGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_ZerolBevelGearSetAdvancedSystemDeflection:
        """Special nested class for casting ZerolBevelGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearSetAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def bevel_gear_set_advanced_system_deflection(self):
            return self._parent._cast(_7253.BevelGearSetAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7241
            
            return self._parent._cast(_7241.AGMAGleasonConicalGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7269
            
            return self._parent._cast(_7269.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7297
            
            return self._parent._cast(_7297.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7336
            
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
        def zerol_bevel_gear_set_advanced_system_deflection(self) -> 'ZerolBevelGearSetAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2533.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6951.ZerolBevelGearSetLoadCase':
        """ZerolBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_367.ZerolBevelGearSetRating':
        """ZerolBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_367.ZerolBevelGearSetRating':
        """ZerolBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2819.ZerolBevelGearSetSystemDeflection]':
        """List[ZerolBevelGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gears_advanced_system_deflection(self) -> 'List[_7365.ZerolBevelGearAdvancedSystemDeflection]':
        """List[ZerolBevelGearAdvancedSystemDeflection]: 'ZerolBevelGearsAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes_advanced_system_deflection(self) -> 'List[_7366.ZerolBevelGearMeshAdvancedSystemDeflection]':
        """List[ZerolBevelGearMeshAdvancedSystemDeflection]: 'ZerolBevelMeshesAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection':
        return self._Cast_ZerolBevelGearSetAdvancedSystemDeflection(self)
