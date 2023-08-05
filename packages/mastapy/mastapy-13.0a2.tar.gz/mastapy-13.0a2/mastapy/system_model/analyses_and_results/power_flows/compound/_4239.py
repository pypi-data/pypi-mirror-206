"""_4239.py

ShaftToMountableComponentConnectionCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4109
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4145
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'ShaftToMountableComponentConnectionCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnectionCompoundPowerFlow',)


class ShaftToMountableComponentConnectionCompoundPowerFlow(_4145.AbstractShaftToMountableComponentConnectionCompoundPowerFlow):
    """ShaftToMountableComponentConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW

    class _Cast_ShaftToMountableComponentConnectionCompoundPowerFlow:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'ShaftToMountableComponentConnectionCompoundPowerFlow'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_power_flow(self):
            return self._parent._cast(_4145.AbstractShaftToMountableComponentConnectionCompoundPowerFlow)

        @property
        def connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4177
            
            return self._parent._cast(_4177.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4166
            
            return self._parent._cast(_4166.CoaxialConnectionCompoundPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4186
            
            return self._parent._cast(_4186.CycloidalDiscCentralBearingConnectionCompoundPowerFlow)

        @property
        def planetary_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4225
            
            return self._parent._cast(_4225.PlanetaryConnectionCompoundPowerFlow)

        @property
        def shaft_to_mountable_component_connection_compound_power_flow(self) -> 'ShaftToMountableComponentConnectionCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnectionCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4109.ShaftToMountableComponentConnectionPowerFlow]':
        """List[ShaftToMountableComponentConnectionPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4109.ShaftToMountableComponentConnectionPowerFlow]':
        """List[ShaftToMountableComponentConnectionPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow':
        return self._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow(self)
