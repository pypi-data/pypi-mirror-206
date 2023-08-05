"""_4267.py

WormGearSetCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.part_model.gears import _2531
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _371
from mastapy.system_model.analyses_and_results.power_flows import _4138
from mastapy.system_model.analyses_and_results.power_flows.compound import _4265, _4266, _4202
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'WormGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetCompoundPowerFlow',)


class WormGearSetCompoundPowerFlow(_4202.GearSetCompoundPowerFlow):
    """WormGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_COMPOUND_POWER_FLOW

    class _Cast_WormGearSetCompoundPowerFlow:
        """Special nested class for casting WormGearSetCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'WormGearSetCompoundPowerFlow'):
            self._parent = parent

        @property
        def gear_set_compound_power_flow(self):
            return self._parent._cast(_4202.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4240
            
            return self._parent._cast(_4240.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4142
            
            return self._parent._cast(_4142.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4221
            
            return self._parent._cast(_4221.PartCompoundPowerFlow)

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
        def worm_gear_set_compound_power_flow(self) -> 'WormGearSetCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2531.WormGearSet':
        """WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def gear_set_duty_cycle_rating(self) -> '_371.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gear_set_duty_cycle_rating(self) -> '_371.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'WormGearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4138.WormGearSetPowerFlow]':
        """List[WormGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gears_compound_power_flow(self) -> 'List[_4265.WormGearCompoundPowerFlow]':
        """List[WormGearCompoundPowerFlow]: 'WormGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_compound_power_flow(self) -> 'List[_4266.WormGearMeshCompoundPowerFlow]':
        """List[WormGearMeshCompoundPowerFlow]: 'WormMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4138.WormGearSetPowerFlow]':
        """List[WormGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'WormGearSetCompoundPowerFlow._Cast_WormGearSetCompoundPowerFlow':
        return self._Cast_WormGearSetCompoundPowerFlow(self)
