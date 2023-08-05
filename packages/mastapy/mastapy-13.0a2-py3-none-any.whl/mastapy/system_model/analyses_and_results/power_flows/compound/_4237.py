"""_4237.py

ShaftCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.part_model.shaft_model import _2462
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4108
from mastapy.system_model.analyses_and_results.power_flows.compound import _4143
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'ShaftCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftCompoundPowerFlow',)


class ShaftCompoundPowerFlow(_4143.AbstractShaftCompoundPowerFlow):
    """ShaftCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_COMPOUND_POWER_FLOW

    class _Cast_ShaftCompoundPowerFlow:
        """Special nested class for casting ShaftCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'ShaftCompoundPowerFlow'):
            self._parent = parent

        @property
        def abstract_shaft_compound_power_flow(self):
            return self._parent._cast(_4143.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4144
            
            return self._parent._cast(_4144.AbstractShaftOrHousingCompoundPowerFlow)

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
        def shaft_compound_power_flow(self) -> 'ShaftCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2462.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4108.ShaftPowerFlow]':
        """List[ShaftPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4108.ShaftPowerFlow]':
        """List[ShaftPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftCompoundPowerFlow._Cast_ShaftCompoundPowerFlow':
        return self._Cast_ShaftCompoundPowerFlow(self)
