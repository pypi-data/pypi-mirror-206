"""_4075.py

InterMountableComponentConnectionPowerFlow
"""
from mastapy.system_model.connections_and_sockets import _2262
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4044
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'InterMountableComponentConnectionPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionPowerFlow',)


class InterMountableComponentConnectionPowerFlow(_4044.ConnectionPowerFlow):
    """InterMountableComponentConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW

    class _Cast_InterMountableComponentConnectionPowerFlow:
        """Special nested class for casting InterMountableComponentConnectionPowerFlow to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionPowerFlow'):
            self._parent = parent

        @property
        def connection_power_flow(self):
            return self._parent._cast(_4044.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7503
            
            return self._parent._cast(_7503.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7500
            
            return self._parent._cast(_7500.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2628
            
            return self._parent._cast(_2628.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4013
            
            return self._parent._cast(_4013.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def belt_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4018
            
            return self._parent._cast(_4018.BeltConnectionPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4020
            
            return self._parent._cast(_4020.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4025
            
            return self._parent._cast(_4025.BevelGearMeshPowerFlow)

        @property
        def clutch_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4030
            
            return self._parent._cast(_4030.ClutchConnectionPowerFlow)

        @property
        def concept_coupling_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4035
            
            return self._parent._cast(_4035.ConceptCouplingConnectionPowerFlow)

        @property
        def concept_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4038
            
            return self._parent._cast(_4038.ConceptGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4041
            
            return self._parent._cast(_4041.ConicalGearMeshPowerFlow)

        @property
        def coupling_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4046
            
            return self._parent._cast(_4046.CouplingConnectionPowerFlow)

        @property
        def cvt_belt_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4049
            
            return self._parent._cast(_4049.CVTBeltConnectionPowerFlow)

        @property
        def cylindrical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4057
            
            return self._parent._cast(_4057.CylindricalGearMeshPowerFlow)

        @property
        def face_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4063
            
            return self._parent._cast(_4063.FaceGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4068
            
            return self._parent._cast(_4068.GearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4072
            
            return self._parent._cast(_4072.HypoidGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4076
            
            return self._parent._cast(_4076.KlingelnbergCycloPalloidConicalGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4079
            
            return self._parent._cast(_4079.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4082
            
            return self._parent._cast(_4082.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow)

        @property
        def part_to_part_shear_coupling_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4090
            
            return self._parent._cast(_4090.PartToPartShearCouplingConnectionPowerFlow)

        @property
        def ring_pins_to_disc_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4102
            
            return self._parent._cast(_4102.RingPinsToDiscConnectionPowerFlow)

        @property
        def rolling_ring_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4104
            
            return self._parent._cast(_4104.RollingRingConnectionPowerFlow)

        @property
        def spiral_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4111
            
            return self._parent._cast(_4111.SpiralBevelGearMeshPowerFlow)

        @property
        def spring_damper_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4114
            
            return self._parent._cast(_4114.SpringDamperConnectionPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4117
            
            return self._parent._cast(_4117.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4120
            
            return self._parent._cast(_4120.StraightBevelGearMeshPowerFlow)

        @property
        def torque_converter_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4130
            
            return self._parent._cast(_4130.TorqueConverterConnectionPowerFlow)

        @property
        def worm_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4136
            
            return self._parent._cast(_4136.WormGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4139
            
            return self._parent._cast(_4139.ZerolBevelGearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(self) -> 'InterMountableComponentConnectionPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2262.InterMountableComponentConnection':
        """InterMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow':
        return self._Cast_InterMountableComponentConnectionPowerFlow(self)
