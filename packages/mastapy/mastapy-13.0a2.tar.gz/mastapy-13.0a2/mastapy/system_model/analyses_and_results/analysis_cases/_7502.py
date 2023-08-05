"""_7502.py

ConnectionFEAnalysis
"""
from mastapy.system_model.analyses_and_results.analysis_cases import _7503
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_FE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'ConnectionFEAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionFEAnalysis',)


class ConnectionFEAnalysis(_7503.ConnectionStaticLoadAnalysisCase):
    """ConnectionFEAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_FE_ANALYSIS

    class _Cast_ConnectionFEAnalysis:
        """Special nested class for casting ConnectionFEAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectionFEAnalysis'):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(self):
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
        def abstract_shaft_to_mountable_component_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2667
            
            return self._parent._cast(_2667.AbstractShaftToMountableComponentConnectionSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2668
            
            return self._parent._cast(_2668.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def belt_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2678
            
            return self._parent._cast(_2678.BeltConnectionSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2680
            
            return self._parent._cast(_2680.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2685
            
            return self._parent._cast(_2685.BevelGearMeshSystemDeflection)

        @property
        def clutch_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2690
            
            return self._parent._cast(_2690.ClutchConnectionSystemDeflection)

        @property
        def coaxial_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2693
            
            return self._parent._cast(_2693.CoaxialConnectionSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2696
            
            return self._parent._cast(_2696.ConceptCouplingConnectionSystemDeflection)

        @property
        def concept_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2699
            
            return self._parent._cast(_2699.ConceptGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2703
            
            return self._parent._cast(_2703.ConicalGearMeshSystemDeflection)

        @property
        def connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2706
            
            return self._parent._cast(_2706.ConnectionSystemDeflection)

        @property
        def coupling_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2708
            
            return self._parent._cast(_2708.CouplingConnectionSystemDeflection)

        @property
        def cvt_belt_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2711
            
            return self._parent._cast(_2711.CVTBeltConnectionSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2715
            
            return self._parent._cast(_2715.CycloidalDiscCentralBearingConnectionSystemDeflection)

        @property
        def cycloidal_disc_planetary_bearing_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2716
            
            return self._parent._cast(_2716.CycloidalDiscPlanetaryBearingConnectionSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2718
            
            return self._parent._cast(_2718.CylindricalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2719
            
            return self._parent._cast(_2719.CylindricalGearMeshSystemDeflectionTimestep)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2720
            
            return self._parent._cast(_2720.CylindricalGearMeshSystemDeflectionWithLTCAResults)

        @property
        def face_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2733
            
            return self._parent._cast(_2733.FaceGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2738
            
            return self._parent._cast(_2738.GearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2742
            
            return self._parent._cast(_2742.HypoidGearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2746
            
            return self._parent._cast(_2746.InterMountableComponentConnectionSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2747
            
            return self._parent._cast(_2747.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2750
            
            return self._parent._cast(_2750.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2753
            
            return self._parent._cast(_2753.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection)

        @property
        def part_to_part_shear_coupling_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2765
            
            return self._parent._cast(_2765.PartToPartShearCouplingConnectionSystemDeflection)

        @property
        def planetary_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2768
            
            return self._parent._cast(_2768.PlanetaryConnectionSystemDeflection)

        @property
        def ring_pins_to_disc_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2774
            
            return self._parent._cast(_2774.RingPinsToDiscConnectionSystemDeflection)

        @property
        def rolling_ring_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2777
            
            return self._parent._cast(_2777.RollingRingConnectionSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2784
            
            return self._parent._cast(_2784.ShaftToMountableComponentConnectionSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2786
            
            return self._parent._cast(_2786.SpiralBevelGearMeshSystemDeflection)

        @property
        def spring_damper_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2789
            
            return self._parent._cast(_2789.SpringDamperConnectionSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2792
            
            return self._parent._cast(_2792.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2795
            
            return self._parent._cast(_2795.StraightBevelGearMeshSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2807
            
            return self._parent._cast(_2807.TorqueConverterConnectionSystemDeflection)

        @property
        def worm_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2815
            
            return self._parent._cast(_2815.WormGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2818
            
            return self._parent._cast(_2818.ZerolBevelGearMeshSystemDeflection)

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
        def connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6278
            
            return self._parent._cast(_6278.ConnectionDynamicAnalysis)

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
        def connection_fe_analysis(self) -> 'ConnectionFEAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionFEAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConnectionFEAnalysis._Cast_ConnectionFEAnalysis':
        return self._Cast_ConnectionFEAnalysis(self)
