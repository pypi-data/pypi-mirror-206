"""_4160.py

BevelGearSetCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4027
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4148
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'BevelGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearSetCompoundPowerFlow',)


class BevelGearSetCompoundPowerFlow(_4148.AGMAGleasonConicalGearSetCompoundPowerFlow):
    """BevelGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_POWER_FLOW

    class _Cast_BevelGearSetCompoundPowerFlow:
        """Special nested class for casting BevelGearSetCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'BevelGearSetCompoundPowerFlow'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(self):
            return self._parent._cast(_4148.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4176
            
            return self._parent._cast(_4176.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4202
            
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
        def bevel_differential_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4155
            
            return self._parent._cast(_4155.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4243
            
            return self._parent._cast(_4243.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4249
            
            return self._parent._cast(_4249.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4252
            
            return self._parent._cast(_4252.StraightBevelGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4270
            
            return self._parent._cast(_4270.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(self) -> 'BevelGearSetCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_4027.BevelGearSetPowerFlow]':
        """List[BevelGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4027.BevelGearSetPowerFlow]':
        """List[BevelGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow':
        return self._Cast_BevelGearSetCompoundPowerFlow(self)
