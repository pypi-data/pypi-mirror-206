"""_4264.py

VirtualComponentCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4135
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'VirtualComponentCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentCompoundPowerFlow',)


class VirtualComponentCompoundPowerFlow(_4219.MountableComponentCompoundPowerFlow):
    """VirtualComponentCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_POWER_FLOW

    class _Cast_VirtualComponentCompoundPowerFlow:
        """Special nested class for casting VirtualComponentCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'VirtualComponentCompoundPowerFlow'):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(self):
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
        def mass_disc_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4217
            
            return self._parent._cast(_4217.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4218
            
            return self._parent._cast(_4218.MeasurementComponentCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4228
            
            return self._parent._cast(_4228.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4229
            
            return self._parent._cast(_4229.PowerLoadCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4263
            
            return self._parent._cast(_4263.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(self) -> 'VirtualComponentCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4135.VirtualComponentPowerFlow]':
        """List[VirtualComponentPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4135.VirtualComponentPowerFlow]':
        """List[VirtualComponentPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow':
        return self._Cast_VirtualComponentCompoundPowerFlow(self)
