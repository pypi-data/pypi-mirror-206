"""_4265.py

WormGearCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.part_model.gears import _2530
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _368
from mastapy.system_model.analyses_and_results.power_flows import _4137
from mastapy.system_model.analyses_and_results.power_flows.compound import _4200
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'WormGearCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearCompoundPowerFlow',)


class WormGearCompoundPowerFlow(_4200.GearCompoundPowerFlow):
    """WormGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_COMPOUND_POWER_FLOW

    class _Cast_WormGearCompoundPowerFlow:
        """Special nested class for casting WormGearCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'WormGearCompoundPowerFlow'):
            self._parent = parent

        @property
        def gear_compound_power_flow(self):
            return self._parent._cast(_4200.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4219
            
            return self._parent._cast(_4219.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4167
            
            return self._parent._cast(_4167.ComponentCompoundPowerFlow)

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
        def worm_gear_compound_power_flow(self) -> 'WormGearCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2530.WormGear':
        """WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating(self) -> '_368.WormGearDutyCycleRating':
        """WormGearDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gear_duty_cycle_rating(self) -> '_368.WormGearDutyCycleRating':
        """WormGearDutyCycleRating: 'WormGearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4137.WormGearPowerFlow]':
        """List[WormGearPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4137.WormGearPowerFlow]':
        """List[WormGearPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'WormGearCompoundPowerFlow._Cast_WormGearCompoundPowerFlow':
        return self._Cast_WormGearCompoundPowerFlow(self)
