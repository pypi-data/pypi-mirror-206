"""_4022.py

BevelDifferentialGearSetPowerFlow
"""
from typing import List

from mastapy.system_model.part_model.gears import _2495
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6789
from mastapy.gears.rating.bevel import _551
from mastapy.system_model.analyses_and_results.power_flows import _4021, _4020, _4027
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'BevelDifferentialGearSetPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetPowerFlow',)


class BevelDifferentialGearSetPowerFlow(_4027.BevelGearSetPowerFlow):
    """BevelDifferentialGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_POWER_FLOW

    class _Cast_BevelDifferentialGearSetPowerFlow:
        """Special nested class for casting BevelDifferentialGearSetPowerFlow to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearSetPowerFlow'):
            self._parent = parent

        @property
        def bevel_gear_set_power_flow(self):
            return self._parent._cast(_4027.BevelGearSetPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4015
            
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
        def bevel_differential_gear_set_power_flow(self) -> 'BevelDifferentialGearSetPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2495.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6789.BevelDifferentialGearSetLoadCase':
        """BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_551.BevelGearSetRating':
        """BevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_551.BevelGearSetRating':
        """BevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears_power_flow(self) -> 'List[_4021.BevelDifferentialGearPowerFlow]':
        """List[BevelDifferentialGearPowerFlow]: 'GearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gears_power_flow(self) -> 'List[_4021.BevelDifferentialGearPowerFlow]':
        """List[BevelDifferentialGearPowerFlow]: 'BevelDifferentialGearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_power_flow(self) -> 'List[_4020.BevelDifferentialGearMeshPowerFlow]':
        """List[BevelDifferentialGearMeshPowerFlow]: 'MeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_power_flow(self) -> 'List[_4020.BevelDifferentialGearMeshPowerFlow]':
        """List[BevelDifferentialGearMeshPowerFlow]: 'BevelDifferentialMeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearSetPowerFlow._Cast_BevelDifferentialGearSetPowerFlow':
        return self._Cast_BevelDifferentialGearSetPowerFlow(self)
