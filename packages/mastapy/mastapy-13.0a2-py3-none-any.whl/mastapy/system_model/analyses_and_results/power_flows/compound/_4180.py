"""_4180.py

CouplingConnectionCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4046
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4207
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'CouplingConnectionCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundPowerFlow',)


class CouplingConnectionCompoundPowerFlow(_4207.InterMountableComponentConnectionCompoundPowerFlow):
    """CouplingConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_POWER_FLOW

    class _Cast_CouplingConnectionCompoundPowerFlow:
        """Special nested class for casting CouplingConnectionCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'CouplingConnectionCompoundPowerFlow'):
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
        def clutch_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4164
            
            return self._parent._cast(_4164.ClutchConnectionCompoundPowerFlow)

        @property
        def concept_coupling_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4169
            
            return self._parent._cast(_4169.ConceptCouplingConnectionCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4223
            
            return self._parent._cast(_4223.PartToPartShearCouplingConnectionCompoundPowerFlow)

        @property
        def spring_damper_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4245
            
            return self._parent._cast(_4245.SpringDamperConnectionCompoundPowerFlow)

        @property
        def torque_converter_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4260
            
            return self._parent._cast(_4260.TorqueConverterConnectionCompoundPowerFlow)

        @property
        def coupling_connection_compound_power_flow(self) -> 'CouplingConnectionCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4046.CouplingConnectionPowerFlow]':
        """List[CouplingConnectionPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4046.CouplingConnectionPowerFlow]':
        """List[CouplingConnectionPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow':
        return self._Cast_CouplingConnectionCompoundPowerFlow(self)
