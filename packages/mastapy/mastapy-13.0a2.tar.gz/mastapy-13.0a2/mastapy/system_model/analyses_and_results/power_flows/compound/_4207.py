"""_4207.py

InterMountableComponentConnectionCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4075
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4177
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'InterMountableComponentConnectionCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionCompoundPowerFlow',)


class InterMountableComponentConnectionCompoundPowerFlow(_4177.ConnectionCompoundPowerFlow):
    """InterMountableComponentConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW

    class _Cast_InterMountableComponentConnectionCompoundPowerFlow:
        """Special nested class for casting InterMountableComponentConnectionCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionCompoundPowerFlow'):
            self._parent = parent

        @property
        def connection_compound_power_flow(self):
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
        def agma_gleason_conical_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4147
            
            return self._parent._cast(_4147.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def belt_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4151
            
            return self._parent._cast(_4151.BeltConnectionCompoundPowerFlow)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4154
            
            return self._parent._cast(_4154.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4159
            
            return self._parent._cast(_4159.BevelGearMeshCompoundPowerFlow)

        @property
        def clutch_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4164
            
            return self._parent._cast(_4164.ClutchConnectionCompoundPowerFlow)

        @property
        def concept_coupling_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4169
            
            return self._parent._cast(_4169.ConceptCouplingConnectionCompoundPowerFlow)

        @property
        def concept_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4172
            
            return self._parent._cast(_4172.ConceptGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4175
            
            return self._parent._cast(_4175.ConicalGearMeshCompoundPowerFlow)

        @property
        def coupling_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4180
            
            return self._parent._cast(_4180.CouplingConnectionCompoundPowerFlow)

        @property
        def cvt_belt_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4182
            
            return self._parent._cast(_4182.CVTBeltConnectionCompoundPowerFlow)

        @property
        def cylindrical_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4190
            
            return self._parent._cast(_4190.CylindricalGearMeshCompoundPowerFlow)

        @property
        def face_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4196
            
            return self._parent._cast(_4196.FaceGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4201
            
            return self._parent._cast(_4201.GearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4205
            
            return self._parent._cast(_4205.HypoidGearMeshCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4209
            
            return self._parent._cast(_4209.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4212
            
            return self._parent._cast(_4212.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4215
            
            return self._parent._cast(_4215.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4223
            
            return self._parent._cast(_4223.PartToPartShearCouplingConnectionCompoundPowerFlow)

        @property
        def ring_pins_to_disc_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4232
            
            return self._parent._cast(_4232.RingPinsToDiscConnectionCompoundPowerFlow)

        @property
        def rolling_ring_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4235
            
            return self._parent._cast(_4235.RollingRingConnectionCompoundPowerFlow)

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4242
            
            return self._parent._cast(_4242.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def spring_damper_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4245
            
            return self._parent._cast(_4245.SpringDamperConnectionCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4248
            
            return self._parent._cast(_4248.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4251
            
            return self._parent._cast(_4251.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def torque_converter_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4260
            
            return self._parent._cast(_4260.TorqueConverterConnectionCompoundPowerFlow)

        @property
        def worm_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4266
            
            return self._parent._cast(_4266.WormGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4269
            
            return self._parent._cast(_4269.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(self) -> 'InterMountableComponentConnectionCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4075.InterMountableComponentConnectionPowerFlow]':
        """List[InterMountableComponentConnectionPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4075.InterMountableComponentConnectionPowerFlow]':
        """List[InterMountableComponentConnectionPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow':
        return self._Cast_InterMountableComponentConnectionCompoundPowerFlow(self)
