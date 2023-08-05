"""_4144.py

AbstractShaftOrHousingCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4010
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4167
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'AbstractShaftOrHousingCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingCompoundPowerFlow',)


class AbstractShaftOrHousingCompoundPowerFlow(_4167.ComponentCompoundPowerFlow):
    """AbstractShaftOrHousingCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_POWER_FLOW

    class _Cast_AbstractShaftOrHousingCompoundPowerFlow:
        """Special nested class for casting AbstractShaftOrHousingCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingCompoundPowerFlow'):
            self._parent = parent

        @property
        def component_compound_power_flow(self):
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
        def abstract_shaft_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4143
            
            return self._parent._cast(_4143.AbstractShaftCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4187
            
            return self._parent._cast(_4187.CycloidalDiscCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4198
            
            return self._parent._cast(_4198.FEPartCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4237
            
            return self._parent._cast(_4237.ShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(self) -> 'AbstractShaftOrHousingCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4010.AbstractShaftOrHousingPowerFlow]':
        """List[AbstractShaftOrHousingPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4010.AbstractShaftOrHousingPowerFlow]':
        """List[AbstractShaftOrHousingPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow':
        return self._Cast_AbstractShaftOrHousingCompoundPowerFlow(self)
