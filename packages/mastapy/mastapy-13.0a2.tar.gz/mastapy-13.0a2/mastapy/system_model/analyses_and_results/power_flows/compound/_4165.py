"""_4165.py

ClutchHalfCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2558
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4031
from mastapy.system_model.analyses_and_results.power_flows.compound import _4181
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'ClutchHalfCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfCompoundPowerFlow',)


class ClutchHalfCompoundPowerFlow(_4181.CouplingHalfCompoundPowerFlow):
    """ClutchHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_POWER_FLOW

    class _Cast_ClutchHalfCompoundPowerFlow:
        """Special nested class for casting ClutchHalfCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'ClutchHalfCompoundPowerFlow'):
            self._parent = parent

        @property
        def coupling_half_compound_power_flow(self):
            return self._parent._cast(_4181.CouplingHalfCompoundPowerFlow)

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
        def clutch_half_compound_power_flow(self) -> 'ClutchHalfCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchHalfCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2558.ClutchHalf':
        """ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4031.ClutchHalfPowerFlow]':
        """List[ClutchHalfPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4031.ClutchHalfPowerFlow]':
        """List[ClutchHalfPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ClutchHalfCompoundPowerFlow._Cast_ClutchHalfCompoundPowerFlow':
        return self._Cast_ClutchHalfCompoundPowerFlow(self)
