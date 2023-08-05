"""_4151.py

BeltConnectionCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.connections_and_sockets import _2249
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4018
from mastapy.system_model.analyses_and_results.power_flows.compound import _4207
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'BeltConnectionCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionCompoundPowerFlow',)


class BeltConnectionCompoundPowerFlow(_4207.InterMountableComponentConnectionCompoundPowerFlow):
    """BeltConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_POWER_FLOW

    class _Cast_BeltConnectionCompoundPowerFlow:
        """Special nested class for casting BeltConnectionCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'BeltConnectionCompoundPowerFlow'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_power_flow(self):
            return self._parent._cast(_4207.InterMountableComponentConnectionCompoundPowerFlow)

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
        def cvt_belt_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4182
            
            return self._parent._cast(_4182.CVTBeltConnectionCompoundPowerFlow)

        @property
        def belt_connection_compound_power_flow(self) -> 'BeltConnectionCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltConnectionCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2249.BeltConnection':
        """BeltConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2249.BeltConnection':
        """BeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4018.BeltConnectionPowerFlow]':
        """List[BeltConnectionPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4018.BeltConnectionPowerFlow]':
        """List[BeltConnectionPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BeltConnectionCompoundPowerFlow._Cast_BeltConnectionCompoundPowerFlow':
        return self._Cast_BeltConnectionCompoundPowerFlow(self)
