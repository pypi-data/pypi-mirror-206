"""_7099.py

WormGearSetAdvancedTimeSteppingAnalysisForModulation
"""
from typing import List

from mastapy.system_model.part_model.gears import _2531
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6948
from mastapy.system_model.analyses_and_results.system_deflections import _2816
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7097, _7098, _7033
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'WormGearSetAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetAdvancedTimeSteppingAnalysisForModulation',)


class WormGearSetAdvancedTimeSteppingAnalysisForModulation(_7033.GearSetAdvancedTimeSteppingAnalysisForModulation):
    """WormGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_WormGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting WormGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'WormGearSetAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7033.GearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7072
            
            return self._parent._cast(_7072.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6969
            
            return self._parent._cast(_6969.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7053
            
            return self._parent._cast(_7053.PartAdvancedTimeSteppingAnalysisForModulation)

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
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(self) -> 'WormGearSetAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2531.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6948.WormGearSetLoadCase':
        """WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2816.WormGearSetSystemDeflection':
        """WormGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gears_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7097.WormGearAdvancedTimeSteppingAnalysisForModulation]':
        """List[WormGearAdvancedTimeSteppingAnalysisForModulation]: 'WormGearsAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7098.WormGearMeshAdvancedTimeSteppingAnalysisForModulation]':
        """List[WormGearMeshAdvancedTimeSteppingAnalysisForModulation]: 'WormMeshesAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'WormGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearSetAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_WormGearSetAdvancedTimeSteppingAnalysisForModulation(self)
