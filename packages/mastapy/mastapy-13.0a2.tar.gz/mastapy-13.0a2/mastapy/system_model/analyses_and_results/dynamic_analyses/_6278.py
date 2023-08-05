"""_6278.py

ConnectionDynamicAnalysis
"""
from mastapy.system_model.connections_and_sockets import _2253
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _2605
from mastapy.system_model.analyses_and_results.analysis_cases import _7502
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ConnectionDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionDynamicAnalysis',)


class ConnectionDynamicAnalysis(_7502.ConnectionFEAnalysis):
    """ConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_DYNAMIC_ANALYSIS

    class _Cast_ConnectionDynamicAnalysis:
        """Special nested class for casting ConnectionDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectionDynamicAnalysis'):
            self._parent = parent

        @property
        def connection_fe_analysis(self):
            return self._parent._cast(_7502.ConnectionFEAnalysis)

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
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6246
            
            return self._parent._cast(_6246.AbstractShaftToMountableComponentConnectionDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6248
            
            return self._parent._cast(_6248.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def belt_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6252
            
            return self._parent._cast(_6252.BeltConnectionDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6255
            
            return self._parent._cast(_6255.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6260
            
            return self._parent._cast(_6260.BevelGearMeshDynamicAnalysis)

        @property
        def clutch_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6264
            
            return self._parent._cast(_6264.ClutchConnectionDynamicAnalysis)

        @property
        def coaxial_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6267
            
            return self._parent._cast(_6267.CoaxialConnectionDynamicAnalysis)

        @property
        def concept_coupling_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6269
            
            return self._parent._cast(_6269.ConceptCouplingConnectionDynamicAnalysis)

        @property
        def concept_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6273
            
            return self._parent._cast(_6273.ConceptGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276
            
            return self._parent._cast(_6276.ConicalGearMeshDynamicAnalysis)

        @property
        def coupling_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280
            
            return self._parent._cast(_6280.CouplingConnectionDynamicAnalysis)

        @property
        def cvt_belt_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283
            
            return self._parent._cast(_6283.CVTBeltConnectionDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287
            
            return self._parent._cast(_6287.CycloidalDiscCentralBearingConnectionDynamicAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289
            
            return self._parent._cast(_6289.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis)

        @property
        def cylindrical_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291
            
            return self._parent._cast(_6291.CylindricalGearMeshDynamicAnalysis)

        @property
        def face_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298
            
            return self._parent._cast(_6298.FaceGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303
            
            return self._parent._cast(_6303.GearMeshDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307
            
            return self._parent._cast(_6307.HypoidGearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309
            
            return self._parent._cast(_6309.InterMountableComponentConnectionDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311
            
            return self._parent._cast(_6311.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314
            
            return self._parent._cast(_6314.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317
            
            return self._parent._cast(_6317.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324
            
            return self._parent._cast(_6324.PartToPartShearCouplingConnectionDynamicAnalysis)

        @property
        def planetary_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327
            
            return self._parent._cast(_6327.PlanetaryConnectionDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334
            
            return self._parent._cast(_6334.RingPinsToDiscConnectionDynamicAnalysis)

        @property
        def rolling_ring_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336
            
            return self._parent._cast(_6336.RollingRingConnectionDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341
            
            return self._parent._cast(_6341.ShaftToMountableComponentConnectionDynamicAnalysis)

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344
            
            return self._parent._cast(_6344.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def spring_damper_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346
            
            return self._parent._cast(_6346.SpringDamperConnectionDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350
            
            return self._parent._cast(_6350.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353
            
            return self._parent._cast(_6353.StraightBevelGearMeshDynamicAnalysis)

        @property
        def torque_converter_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361
            
            return self._parent._cast(_6361.TorqueConverterConnectionDynamicAnalysis)

        @property
        def worm_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368
            
            return self._parent._cast(_6368.WormGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371
            
            return self._parent._cast(_6371.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def connection_dynamic_analysis(self) -> 'ConnectionDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2253.Connection':
        """Connection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2253.Connection':
        """Connection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def dynamic_analysis(self) -> '_2605.DynamicAnalysis':
        """DynamicAnalysis: 'DynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis':
        return self._Cast_ConnectionDynamicAnalysis(self)
