"""_4074.py

HypoidGearSetPowerFlow
"""
from typing import List

from mastapy.system_model.part_model.gears import _2514
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6871
from mastapy.gears.rating.hypoid import _436
from mastapy.system_model.analyses_and_results.power_flows import _4073, _4072, _4015
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'HypoidGearSetPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetPowerFlow',)


class HypoidGearSetPowerFlow(_4015.AGMAGleasonConicalGearSetPowerFlow):
    """HypoidGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_POWER_FLOW

    class _Cast_HypoidGearSetPowerFlow:
        """Special nested class for casting HypoidGearSetPowerFlow to subclasses."""

        def __init__(self, parent: 'HypoidGearSetPowerFlow'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_power_flow(self):
            return self._parent._cast(_4015.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4043
            
            return self._parent._cast(_4043.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4070
            
            return self._parent._cast(_4070.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4110
            
            return self._parent._cast(_4110.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4009
            
            return self._parent._cast(_4009.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4089
            
            return self._parent._cast(_4089.PartPowerFlow)

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
        def hypoid_gear_set_power_flow(self) -> 'HypoidGearSetPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearSetPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2514.HypoidGearSet':
        """HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6871.HypoidGearSetLoadCase':
        """HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_436.HypoidGearSetRating':
        """HypoidGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_436.HypoidGearSetRating':
        """HypoidGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears_power_flow(self) -> 'List[_4073.HypoidGearPowerFlow]':
        """List[HypoidGearPowerFlow]: 'GearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gears_power_flow(self) -> 'List[_4073.HypoidGearPowerFlow]':
        """List[HypoidGearPowerFlow]: 'HypoidGearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_power_flow(self) -> 'List[_4072.HypoidGearMeshPowerFlow]':
        """List[HypoidGearMeshPowerFlow]: 'MeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_power_flow(self) -> 'List[_4072.HypoidGearMeshPowerFlow]':
        """List[HypoidGearMeshPowerFlow]: 'HypoidMeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow':
        return self._Cast_HypoidGearSetPowerFlow(self)
