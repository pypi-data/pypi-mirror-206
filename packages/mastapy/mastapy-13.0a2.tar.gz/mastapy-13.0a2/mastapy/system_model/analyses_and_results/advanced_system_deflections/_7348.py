"""_7348.py

StraightBevelGearSetAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model.gears import _2527
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6928
from mastapy.gears.rating.straight_bevel import _393
from mastapy.system_model.analyses_and_results.system_deflections import _2796
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7346, _7347, _7253
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'StraightBevelGearSetAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetAdvancedSystemDeflection',)


class StraightBevelGearSetAdvancedSystemDeflection(_7253.BevelGearSetAdvancedSystemDeflection):
    """StraightBevelGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_StraightBevelGearSetAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'StraightBevelGearSetAdvancedSystemDeflection'):
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
        def straight_bevel_gear_set_advanced_system_deflection(self) -> 'StraightBevelGearSetAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2527.StraightBevelGearSet':
        """StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6928.StraightBevelGearSetLoadCase':
        """StraightBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_393.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_393.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2796.StraightBevelGearSetSystemDeflection]':
        """List[StraightBevelGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gears_advanced_system_deflection(self) -> 'List[_7346.StraightBevelGearAdvancedSystemDeflection]':
        """List[StraightBevelGearAdvancedSystemDeflection]: 'StraightBevelGearsAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_advanced_system_deflection(self) -> 'List[_7347.StraightBevelGearMeshAdvancedSystemDeflection]':
        """List[StraightBevelGearMeshAdvancedSystemDeflection]: 'StraightBevelMeshesAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection':
        return self._Cast_StraightBevelGearSetAdvancedSystemDeflection(self)
