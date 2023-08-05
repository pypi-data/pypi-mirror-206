"""_7501.py

ConnectionCompoundAnalysis
"""
from mastapy.system_model.analyses_and_results.analysis_cases import _7505
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'ConnectionCompoundAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionCompoundAnalysis',)


class ConnectionCompoundAnalysis(_7505.DesignEntityCompoundAnalysis):
    """ConnectionCompoundAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_ANALYSIS

    class _Cast_ConnectionCompoundAnalysis:
        """Special nested class for casting ConnectionCompoundAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectionCompoundAnalysis'):
            self._parent = parent

        @property
        def design_entity_compound_analysis(self):
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2833
            
            return self._parent._cast(_2833.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2835
            
            return self._parent._cast(_2835.AGMAGleasonConicalGearMeshCompoundSystemDeflection)

        @property
        def belt_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2839
            
            return self._parent._cast(_2839.BeltConnectionCompoundSystemDeflection)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2842
            
            return self._parent._cast(_2842.BevelDifferentialGearMeshCompoundSystemDeflection)

        @property
        def bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2847
            
            return self._parent._cast(_2847.BevelGearMeshCompoundSystemDeflection)

        @property
        def clutch_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2852
            
            return self._parent._cast(_2852.ClutchConnectionCompoundSystemDeflection)

        @property
        def coaxial_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2854
            
            return self._parent._cast(_2854.CoaxialConnectionCompoundSystemDeflection)

        @property
        def concept_coupling_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2857
            
            return self._parent._cast(_2857.ConceptCouplingConnectionCompoundSystemDeflection)

        @property
        def concept_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2860
            
            return self._parent._cast(_2860.ConceptGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2863
            
            return self._parent._cast(_2863.ConicalGearMeshCompoundSystemDeflection)

        @property
        def connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2865
            
            return self._parent._cast(_2865.ConnectionCompoundSystemDeflection)

        @property
        def coupling_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2868
            
            return self._parent._cast(_2868.CouplingConnectionCompoundSystemDeflection)

        @property
        def cvt_belt_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2870
            
            return self._parent._cast(_2870.CVTBeltConnectionCompoundSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2874
            
            return self._parent._cast(_2874.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2876
            
            return self._parent._cast(_2876.CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection)

        @property
        def cylindrical_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2878
            
            return self._parent._cast(_2878.CylindricalGearMeshCompoundSystemDeflection)

        @property
        def face_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2885
            
            return self._parent._cast(_2885.FaceGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2890
            
            return self._parent._cast(_2890.GearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2894
            
            return self._parent._cast(_2894.HypoidGearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2896
            
            return self._parent._cast(_2896.InterMountableComponentConnectionCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2898
            
            return self._parent._cast(_2898.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2901
            
            return self._parent._cast(_2901.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2904
            
            return self._parent._cast(_2904.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2912
            
            return self._parent._cast(_2912.PartToPartShearCouplingConnectionCompoundSystemDeflection)

        @property
        def planetary_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2914
            
            return self._parent._cast(_2914.PlanetaryConnectionCompoundSystemDeflection)

        @property
        def ring_pins_to_disc_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2921
            
            return self._parent._cast(_2921.RingPinsToDiscConnectionCompoundSystemDeflection)

        @property
        def rolling_ring_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2924
            
            return self._parent._cast(_2924.RollingRingConnectionCompoundSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2929
            
            return self._parent._cast(_2929.ShaftToMountableComponentConnectionCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2932
            
            return self._parent._cast(_2932.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def spring_damper_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2935
            
            return self._parent._cast(_2935.SpringDamperConnectionCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2938
            
            return self._parent._cast(_2938.StraightBevelDiffGearMeshCompoundSystemDeflection)

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2941
            
            return self._parent._cast(_2941.StraightBevelGearMeshCompoundSystemDeflection)

        @property
        def torque_converter_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2950
            
            return self._parent._cast(_2950.TorqueConverterConnectionCompoundSystemDeflection)

        @property
        def worm_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2956
            
            return self._parent._cast(_2956.WormGearMeshCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2959
            
            return self._parent._cast(_2959.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3098
            
            return self._parent._cast(_3098.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3100
            
            return self._parent._cast(_3100.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def belt_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3104
            
            return self._parent._cast(_3104.BeltConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3107
            
            return self._parent._cast(_3107.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3112
            
            return self._parent._cast(_3112.BevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def clutch_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3117
            
            return self._parent._cast(_3117.ClutchConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3119
            
            return self._parent._cast(_3119.CoaxialConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3122
            
            return self._parent._cast(_3122.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3125
            
            return self._parent._cast(_3125.ConceptGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3128
            
            return self._parent._cast(_3128.ConicalGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3130
            
            return self._parent._cast(_3130.ConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def coupling_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3133
            
            return self._parent._cast(_3133.CouplingConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3135
            
            return self._parent._cast(_3135.CVTBeltConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3139
            
            return self._parent._cast(_3139.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3141
            
            return self._parent._cast(_3141.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3143
            
            return self._parent._cast(_3143.CylindricalGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3149
            
            return self._parent._cast(_3149.FaceGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3154
            
            return self._parent._cast(_3154.GearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3158
            
            return self._parent._cast(_3158.HypoidGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3160
            
            return self._parent._cast(_3160.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3162
            
            return self._parent._cast(_3162.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3165
            
            return self._parent._cast(_3165.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3168
            
            return self._parent._cast(_3168.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3176
            
            return self._parent._cast(_3176.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def planetary_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3178
            
            return self._parent._cast(_3178.PlanetaryConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3185
            
            return self._parent._cast(_3185.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3188
            
            return self._parent._cast(_3188.RollingRingConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3192
            
            return self._parent._cast(_3192.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3195
            
            return self._parent._cast(_3195.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3198
            
            return self._parent._cast(_3198.SpringDamperConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3201
            
            return self._parent._cast(_3201.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3204
            
            return self._parent._cast(_3204.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3213
            
            return self._parent._cast(_3213.TorqueConverterConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3219
            
            return self._parent._cast(_3219.WormGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3222
            
            return self._parent._cast(_3222.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3357
            
            return self._parent._cast(_3357.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3359
            
            return self._parent._cast(_3359.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def belt_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3363
            
            return self._parent._cast(_3363.BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3366
            
            return self._parent._cast(_3366.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3371
            
            return self._parent._cast(_3371.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3376
            
            return self._parent._cast(_3376.ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3378
            
            return self._parent._cast(_3378.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3381
            
            return self._parent._cast(_3381.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3384
            
            return self._parent._cast(_3384.ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3387
            
            return self._parent._cast(_3387.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3389
            
            return self._parent._cast(_3389.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3392
            
            return self._parent._cast(_3392.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3394
            
            return self._parent._cast(_3394.CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3398
            
            return self._parent._cast(_3398.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3400
            
            return self._parent._cast(_3400.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3402
            
            return self._parent._cast(_3402.CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3408
            
            return self._parent._cast(_3408.FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3413
            
            return self._parent._cast(_3413.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3417
            
            return self._parent._cast(_3417.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3419
            
            return self._parent._cast(_3419.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3421
            
            return self._parent._cast(_3421.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3424
            
            return self._parent._cast(_3424.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3427
            
            return self._parent._cast(_3427.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3435
            
            return self._parent._cast(_3435.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def planetary_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3437
            
            return self._parent._cast(_3437.PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3444
            
            return self._parent._cast(_3444.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3447
            
            return self._parent._cast(_3447.RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3451
            
            return self._parent._cast(_3451.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3454
            
            return self._parent._cast(_3454.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3457
            
            return self._parent._cast(_3457.SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3460
            
            return self._parent._cast(_3460.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3463
            
            return self._parent._cast(_3463.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3472
            
            return self._parent._cast(_3472.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3478
            
            return self._parent._cast(_3478.WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3481
            
            return self._parent._cast(_3481.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3616
            
            return self._parent._cast(_3616.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3618
            
            return self._parent._cast(_3618.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def belt_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3622
            
            return self._parent._cast(_3622.BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3625
            
            return self._parent._cast(_3625.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3630
            
            return self._parent._cast(_3630.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3635
            
            return self._parent._cast(_3635.ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3637
            
            return self._parent._cast(_3637.CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3640
            
            return self._parent._cast(_3640.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3643
            
            return self._parent._cast(_3643.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3646
            
            return self._parent._cast(_3646.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3648
            
            return self._parent._cast(_3648.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3651
            
            return self._parent._cast(_3651.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3653
            
            return self._parent._cast(_3653.CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3657
            
            return self._parent._cast(_3657.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3659
            
            return self._parent._cast(_3659.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3661
            
            return self._parent._cast(_3661.CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3667
            
            return self._parent._cast(_3667.FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3672
            
            return self._parent._cast(_3672.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3676
            
            return self._parent._cast(_3676.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3678
            
            return self._parent._cast(_3678.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3680
            
            return self._parent._cast(_3680.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3683
            
            return self._parent._cast(_3683.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3686
            
            return self._parent._cast(_3686.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3694
            
            return self._parent._cast(_3694.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def planetary_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3696
            
            return self._parent._cast(_3696.PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3703
            
            return self._parent._cast(_3703.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3706
            
            return self._parent._cast(_3706.RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3710
            
            return self._parent._cast(_3710.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3713
            
            return self._parent._cast(_3713.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3716
            
            return self._parent._cast(_3716.SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3719
            
            return self._parent._cast(_3719.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3722
            
            return self._parent._cast(_3722.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3731
            
            return self._parent._cast(_3731.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3737
            
            return self._parent._cast(_3737.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3740
            
            return self._parent._cast(_3740.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3877
            
            return self._parent._cast(_3877.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3879
            
            return self._parent._cast(_3879.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis)

        @property
        def belt_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3883
            
            return self._parent._cast(_3883.BeltConnectionCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3886
            
            return self._parent._cast(_3886.BevelDifferentialGearMeshCompoundStabilityAnalysis)

        @property
        def bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3891
            
            return self._parent._cast(_3891.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def clutch_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3896
            
            return self._parent._cast(_3896.ClutchConnectionCompoundStabilityAnalysis)

        @property
        def coaxial_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3898
            
            return self._parent._cast(_3898.CoaxialConnectionCompoundStabilityAnalysis)

        @property
        def concept_coupling_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3901
            
            return self._parent._cast(_3901.ConceptCouplingConnectionCompoundStabilityAnalysis)

        @property
        def concept_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3904
            
            return self._parent._cast(_3904.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3907
            
            return self._parent._cast(_3907.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3909
            
            return self._parent._cast(_3909.ConnectionCompoundStabilityAnalysis)

        @property
        def coupling_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3912
            
            return self._parent._cast(_3912.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def cvt_belt_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3914
            
            return self._parent._cast(_3914.CVTBeltConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3918
            
            return self._parent._cast(_3918.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3920
            
            return self._parent._cast(_3920.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3922
            
            return self._parent._cast(_3922.CylindricalGearMeshCompoundStabilityAnalysis)

        @property
        def face_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3928
            
            return self._parent._cast(_3928.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3933
            
            return self._parent._cast(_3933.GearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3937
            
            return self._parent._cast(_3937.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3939
            
            return self._parent._cast(_3939.InterMountableComponentConnectionCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3941
            
            return self._parent._cast(_3941.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3944
            
            return self._parent._cast(_3944.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3947
            
            return self._parent._cast(_3947.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3955
            
            return self._parent._cast(_3955.PartToPartShearCouplingConnectionCompoundStabilityAnalysis)

        @property
        def planetary_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3957
            
            return self._parent._cast(_3957.PlanetaryConnectionCompoundStabilityAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3964
            
            return self._parent._cast(_3964.RingPinsToDiscConnectionCompoundStabilityAnalysis)

        @property
        def rolling_ring_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3967
            
            return self._parent._cast(_3967.RollingRingConnectionCompoundStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3971
            
            return self._parent._cast(_3971.ShaftToMountableComponentConnectionCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3974
            
            return self._parent._cast(_3974.SpiralBevelGearMeshCompoundStabilityAnalysis)

        @property
        def spring_damper_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3977
            
            return self._parent._cast(_3977.SpringDamperConnectionCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3980
            
            return self._parent._cast(_3980.StraightBevelDiffGearMeshCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3983
            
            return self._parent._cast(_3983.StraightBevelGearMeshCompoundStabilityAnalysis)

        @property
        def torque_converter_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3992
            
            return self._parent._cast(_3992.TorqueConverterConnectionCompoundStabilityAnalysis)

        @property
        def worm_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3998
            
            return self._parent._cast(_3998.WormGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4001
            
            return self._parent._cast(_4001.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4145
            
            return self._parent._cast(_4145.AbstractShaftToMountableComponentConnectionCompoundPowerFlow)

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
        def coaxial_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4166
            
            return self._parent._cast(_4166.CoaxialConnectionCompoundPowerFlow)

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
        def connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4177
            
            return self._parent._cast(_4177.ConnectionCompoundPowerFlow)

        @property
        def coupling_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4180
            
            return self._parent._cast(_4180.CouplingConnectionCompoundPowerFlow)

        @property
        def cvt_belt_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4182
            
            return self._parent._cast(_4182.CVTBeltConnectionCompoundPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4186
            
            return self._parent._cast(_4186.CycloidalDiscCentralBearingConnectionCompoundPowerFlow)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4188
            
            return self._parent._cast(_4188.CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow)

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
        def inter_mountable_component_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4207
            
            return self._parent._cast(_4207.InterMountableComponentConnectionCompoundPowerFlow)

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
        def planetary_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4225
            
            return self._parent._cast(_4225.PlanetaryConnectionCompoundPowerFlow)

        @property
        def ring_pins_to_disc_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4232
            
            return self._parent._cast(_4232.RingPinsToDiscConnectionCompoundPowerFlow)

        @property
        def rolling_ring_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4235
            
            return self._parent._cast(_4235.RollingRingConnectionCompoundPowerFlow)

        @property
        def shaft_to_mountable_component_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4239
            
            return self._parent._cast(_4239.ShaftToMountableComponentConnectionCompoundPowerFlow)

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
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4421
            
            return self._parent._cast(_4421.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4423
            
            return self._parent._cast(_4423.AGMAGleasonConicalGearMeshCompoundParametricStudyTool)

        @property
        def belt_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4427
            
            return self._parent._cast(_4427.BeltConnectionCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4430
            
            return self._parent._cast(_4430.BevelDifferentialGearMeshCompoundParametricStudyTool)

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4435
            
            return self._parent._cast(_4435.BevelGearMeshCompoundParametricStudyTool)

        @property
        def clutch_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4440
            
            return self._parent._cast(_4440.ClutchConnectionCompoundParametricStudyTool)

        @property
        def coaxial_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4442
            
            return self._parent._cast(_4442.CoaxialConnectionCompoundParametricStudyTool)

        @property
        def concept_coupling_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4445
            
            return self._parent._cast(_4445.ConceptCouplingConnectionCompoundParametricStudyTool)

        @property
        def concept_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4448
            
            return self._parent._cast(_4448.ConceptGearMeshCompoundParametricStudyTool)

        @property
        def conical_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4451
            
            return self._parent._cast(_4451.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4453
            
            return self._parent._cast(_4453.ConnectionCompoundParametricStudyTool)

        @property
        def coupling_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4456
            
            return self._parent._cast(_4456.CouplingConnectionCompoundParametricStudyTool)

        @property
        def cvt_belt_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4458
            
            return self._parent._cast(_4458.CVTBeltConnectionCompoundParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4462
            
            return self._parent._cast(_4462.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4464
            
            return self._parent._cast(_4464.CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool)

        @property
        def cylindrical_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4466
            
            return self._parent._cast(_4466.CylindricalGearMeshCompoundParametricStudyTool)

        @property
        def face_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4472
            
            return self._parent._cast(_4472.FaceGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4477
            
            return self._parent._cast(_4477.GearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4481
            
            return self._parent._cast(_4481.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4483
            
            return self._parent._cast(_4483.InterMountableComponentConnectionCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4485
            
            return self._parent._cast(_4485.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4488
            
            return self._parent._cast(_4488.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4491
            
            return self._parent._cast(_4491.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4499
            
            return self._parent._cast(_4499.PartToPartShearCouplingConnectionCompoundParametricStudyTool)

        @property
        def planetary_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4501
            
            return self._parent._cast(_4501.PlanetaryConnectionCompoundParametricStudyTool)

        @property
        def ring_pins_to_disc_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4508
            
            return self._parent._cast(_4508.RingPinsToDiscConnectionCompoundParametricStudyTool)

        @property
        def rolling_ring_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4511
            
            return self._parent._cast(_4511.RollingRingConnectionCompoundParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4515
            
            return self._parent._cast(_4515.ShaftToMountableComponentConnectionCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4518
            
            return self._parent._cast(_4518.SpiralBevelGearMeshCompoundParametricStudyTool)

        @property
        def spring_damper_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4521
            
            return self._parent._cast(_4521.SpringDamperConnectionCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4524
            
            return self._parent._cast(_4524.StraightBevelDiffGearMeshCompoundParametricStudyTool)

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4527
            
            return self._parent._cast(_4527.StraightBevelGearMeshCompoundParametricStudyTool)

        @property
        def torque_converter_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4536
            
            return self._parent._cast(_4536.TorqueConverterConnectionCompoundParametricStudyTool)

        @property
        def worm_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4542
            
            return self._parent._cast(_4542.WormGearMeshCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4545
            
            return self._parent._cast(_4545.ZerolBevelGearMeshCompoundParametricStudyTool)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4704
            
            return self._parent._cast(_4704.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4706
            
            return self._parent._cast(_4706.AGMAGleasonConicalGearMeshCompoundModalAnalysis)

        @property
        def belt_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4710
            
            return self._parent._cast(_4710.BeltConnectionCompoundModalAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4713
            
            return self._parent._cast(_4713.BevelDifferentialGearMeshCompoundModalAnalysis)

        @property
        def bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4718
            
            return self._parent._cast(_4718.BevelGearMeshCompoundModalAnalysis)

        @property
        def clutch_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4723
            
            return self._parent._cast(_4723.ClutchConnectionCompoundModalAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4725
            
            return self._parent._cast(_4725.CoaxialConnectionCompoundModalAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4728
            
            return self._parent._cast(_4728.ConceptCouplingConnectionCompoundModalAnalysis)

        @property
        def concept_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4731
            
            return self._parent._cast(_4731.ConceptGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4734
            
            return self._parent._cast(_4734.ConicalGearMeshCompoundModalAnalysis)

        @property
        def connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4736
            
            return self._parent._cast(_4736.ConnectionCompoundModalAnalysis)

        @property
        def coupling_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4739
            
            return self._parent._cast(_4739.CouplingConnectionCompoundModalAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4741
            
            return self._parent._cast(_4741.CVTBeltConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4745
            
            return self._parent._cast(_4745.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4747
            
            return self._parent._cast(_4747.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis)

        @property
        def cylindrical_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4749
            
            return self._parent._cast(_4749.CylindricalGearMeshCompoundModalAnalysis)

        @property
        def face_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4755
            
            return self._parent._cast(_4755.FaceGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4760
            
            return self._parent._cast(_4760.GearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4764
            
            return self._parent._cast(_4764.HypoidGearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4766
            
            return self._parent._cast(_4766.InterMountableComponentConnectionCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4768
            
            return self._parent._cast(_4768.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4771
            
            return self._parent._cast(_4771.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4774
            
            return self._parent._cast(_4774.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4782
            
            return self._parent._cast(_4782.PartToPartShearCouplingConnectionCompoundModalAnalysis)

        @property
        def planetary_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4784
            
            return self._parent._cast(_4784.PlanetaryConnectionCompoundModalAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4791
            
            return self._parent._cast(_4791.RingPinsToDiscConnectionCompoundModalAnalysis)

        @property
        def rolling_ring_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4794
            
            return self._parent._cast(_4794.RollingRingConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4798
            
            return self._parent._cast(_4798.ShaftToMountableComponentConnectionCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4801
            
            return self._parent._cast(_4801.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4804
            
            return self._parent._cast(_4804.SpringDamperConnectionCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4807
            
            return self._parent._cast(_4807.StraightBevelDiffGearMeshCompoundModalAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4810
            
            return self._parent._cast(_4810.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4819
            
            return self._parent._cast(_4819.TorqueConverterConnectionCompoundModalAnalysis)

        @property
        def worm_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4825
            
            return self._parent._cast(_4825.WormGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4828
            
            return self._parent._cast(_4828.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4963
            
            return self._parent._cast(_4963.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4965
            
            return self._parent._cast(_4965.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def belt_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4969
            
            return self._parent._cast(_4969.BeltConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4972
            
            return self._parent._cast(_4972.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4977
            
            return self._parent._cast(_4977.BevelGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4982
            
            return self._parent._cast(_4982.ClutchConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4984
            
            return self._parent._cast(_4984.CoaxialConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4987
            
            return self._parent._cast(_4987.ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4990
            
            return self._parent._cast(_4990.ConceptGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4993
            
            return self._parent._cast(_4993.ConicalGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4995
            
            return self._parent._cast(_4995.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4998
            
            return self._parent._cast(_4998.CouplingConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5000
            
            return self._parent._cast(_5000.CVTBeltConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5004
            
            return self._parent._cast(_5004.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5006
            
            return self._parent._cast(_5006.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5008
            
            return self._parent._cast(_5008.CylindricalGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5014
            
            return self._parent._cast(_5014.FaceGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5019
            
            return self._parent._cast(_5019.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5023
            
            return self._parent._cast(_5023.HypoidGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5025
            
            return self._parent._cast(_5025.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5027
            
            return self._parent._cast(_5027.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5030
            
            return self._parent._cast(_5030.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5033
            
            return self._parent._cast(_5033.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5041
            
            return self._parent._cast(_5041.PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def planetary_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5043
            
            return self._parent._cast(_5043.PlanetaryConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5050
            
            return self._parent._cast(_5050.RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5053
            
            return self._parent._cast(_5053.RollingRingConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5057
            
            return self._parent._cast(_5057.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5060
            
            return self._parent._cast(_5060.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5063
            
            return self._parent._cast(_5063.SpringDamperConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5066
            
            return self._parent._cast(_5066.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5069
            
            return self._parent._cast(_5069.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5078
            
            return self._parent._cast(_5078.TorqueConverterConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5084
            
            return self._parent._cast(_5084.WormGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5087
            
            return self._parent._cast(_5087.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5221
            
            return self._parent._cast(_5221.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5223
            
            return self._parent._cast(_5223.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def belt_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5227
            
            return self._parent._cast(_5227.BeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5230
            
            return self._parent._cast(_5230.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5235
            
            return self._parent._cast(_5235.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def clutch_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5240
            
            return self._parent._cast(_5240.ClutchConnectionCompoundModalAnalysisAtASpeed)

        @property
        def coaxial_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5242
            
            return self._parent._cast(_5242.CoaxialConnectionCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5245
            
            return self._parent._cast(_5245.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5248
            
            return self._parent._cast(_5248.ConceptGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5251
            
            return self._parent._cast(_5251.ConicalGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5253
            
            return self._parent._cast(_5253.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5256
            
            return self._parent._cast(_5256.CouplingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5258
            
            return self._parent._cast(_5258.CVTBeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5262
            
            return self._parent._cast(_5262.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5264
            
            return self._parent._cast(_5264.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5266
            
            return self._parent._cast(_5266.CylindricalGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5272
            
            return self._parent._cast(_5272.FaceGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5277
            
            return self._parent._cast(_5277.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5281
            
            return self._parent._cast(_5281.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5283
            
            return self._parent._cast(_5283.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5285
            
            return self._parent._cast(_5285.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5288
            
            return self._parent._cast(_5288.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5291
            
            return self._parent._cast(_5291.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5299
            
            return self._parent._cast(_5299.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def planetary_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5301
            
            return self._parent._cast(_5301.PlanetaryConnectionCompoundModalAnalysisAtASpeed)

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5308
            
            return self._parent._cast(_5308.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5311
            
            return self._parent._cast(_5311.RollingRingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5315
            
            return self._parent._cast(_5315.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5318
            
            return self._parent._cast(_5318.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5321
            
            return self._parent._cast(_5321.SpringDamperConnectionCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5324
            
            return self._parent._cast(_5324.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5327
            
            return self._parent._cast(_5327.StraightBevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5336
            
            return self._parent._cast(_5336.TorqueConverterConnectionCompoundModalAnalysisAtASpeed)

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5342
            
            return self._parent._cast(_5342.WormGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5345
            
            return self._parent._cast(_5345.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5502
            
            return self._parent._cast(_5502.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5504
            
            return self._parent._cast(_5504.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5508
            
            return self._parent._cast(_5508.BeltConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5511
            
            return self._parent._cast(_5511.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5516
            
            return self._parent._cast(_5516.BevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5521
            
            return self._parent._cast(_5521.ClutchConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5523
            
            return self._parent._cast(_5523.CoaxialConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5526
            
            return self._parent._cast(_5526.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5529
            
            return self._parent._cast(_5529.ConceptGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5532
            
            return self._parent._cast(_5532.ConicalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5534
            
            return self._parent._cast(_5534.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5537
            
            return self._parent._cast(_5537.CouplingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5539
            
            return self._parent._cast(_5539.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5543
            
            return self._parent._cast(_5543.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5545
            
            return self._parent._cast(_5545.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5547
            
            return self._parent._cast(_5547.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5553
            
            return self._parent._cast(_5553.FaceGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5558
            
            return self._parent._cast(_5558.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5562
            
            return self._parent._cast(_5562.HypoidGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5564
            
            return self._parent._cast(_5564.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5566
            
            return self._parent._cast(_5566.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5569
            
            return self._parent._cast(_5569.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5572
            
            return self._parent._cast(_5572.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5580
            
            return self._parent._cast(_5580.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def planetary_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5582
            
            return self._parent._cast(_5582.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5589
            
            return self._parent._cast(_5589.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5592
            
            return self._parent._cast(_5592.RollingRingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5596
            
            return self._parent._cast(_5596.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5599
            
            return self._parent._cast(_5599.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5602
            
            return self._parent._cast(_5602.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5605
            
            return self._parent._cast(_5605.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5608
            
            return self._parent._cast(_5608.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5617
            
            return self._parent._cast(_5617.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5623
            
            return self._parent._cast(_5623.WormGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5626
            
            return self._parent._cast(_5626.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5849
            
            return self._parent._cast(_5849.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5851
            
            return self._parent._cast(_5851.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def belt_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5855
            
            return self._parent._cast(_5855.BeltConnectionCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5858
            
            return self._parent._cast(_5858.BevelDifferentialGearMeshCompoundHarmonicAnalysis)

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5863
            
            return self._parent._cast(_5863.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def clutch_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5868
            
            return self._parent._cast(_5868.ClutchConnectionCompoundHarmonicAnalysis)

        @property
        def coaxial_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5870
            
            return self._parent._cast(_5870.CoaxialConnectionCompoundHarmonicAnalysis)

        @property
        def concept_coupling_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5873
            
            return self._parent._cast(_5873.ConceptCouplingConnectionCompoundHarmonicAnalysis)

        @property
        def concept_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5876
            
            return self._parent._cast(_5876.ConceptGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5879
            
            return self._parent._cast(_5879.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5881
            
            return self._parent._cast(_5881.ConnectionCompoundHarmonicAnalysis)

        @property
        def coupling_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5884
            
            return self._parent._cast(_5884.CouplingConnectionCompoundHarmonicAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5886
            
            return self._parent._cast(_5886.CVTBeltConnectionCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5890
            
            return self._parent._cast(_5890.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5892
            
            return self._parent._cast(_5892.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5894
            
            return self._parent._cast(_5894.CylindricalGearMeshCompoundHarmonicAnalysis)

        @property
        def face_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5900
            
            return self._parent._cast(_5900.FaceGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5905
            
            return self._parent._cast(_5905.GearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5909
            
            return self._parent._cast(_5909.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5911
            
            return self._parent._cast(_5911.InterMountableComponentConnectionCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5913
            
            return self._parent._cast(_5913.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5916
            
            return self._parent._cast(_5916.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5919
            
            return self._parent._cast(_5919.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5927
            
            return self._parent._cast(_5927.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis)

        @property
        def planetary_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5929
            
            return self._parent._cast(_5929.PlanetaryConnectionCompoundHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5936
            
            return self._parent._cast(_5936.RingPinsToDiscConnectionCompoundHarmonicAnalysis)

        @property
        def rolling_ring_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5939
            
            return self._parent._cast(_5939.RollingRingConnectionCompoundHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5943
            
            return self._parent._cast(_5943.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5946
            
            return self._parent._cast(_5946.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def spring_damper_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5949
            
            return self._parent._cast(_5949.SpringDamperConnectionCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5952
            
            return self._parent._cast(_5952.StraightBevelDiffGearMeshCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5955
            
            return self._parent._cast(_5955.StraightBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def torque_converter_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5964
            
            return self._parent._cast(_5964.TorqueConverterConnectionCompoundHarmonicAnalysis)

        @property
        def worm_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5970
            
            return self._parent._cast(_5970.WormGearMeshCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5973
            
            return self._parent._cast(_5973.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6108
            
            return self._parent._cast(_6108.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6110
            
            return self._parent._cast(_6110.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6114
            
            return self._parent._cast(_6114.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6117
            
            return self._parent._cast(_6117.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6122
            
            return self._parent._cast(_6122.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6127
            
            return self._parent._cast(_6127.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def coaxial_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6129
            
            return self._parent._cast(_6129.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6132
            
            return self._parent._cast(_6132.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6135
            
            return self._parent._cast(_6135.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6138
            
            return self._parent._cast(_6138.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6140
            
            return self._parent._cast(_6140.ConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6143
            
            return self._parent._cast(_6143.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_belt_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6145
            
            return self._parent._cast(_6145.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6149
            
            return self._parent._cast(_6149.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6151
            
            return self._parent._cast(_6151.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6153
            
            return self._parent._cast(_6153.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6159
            
            return self._parent._cast(_6159.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6164
            
            return self._parent._cast(_6164.GearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6168
            
            return self._parent._cast(_6168.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6170
            
            return self._parent._cast(_6170.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6172
            
            return self._parent._cast(_6172.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6175
            
            return self._parent._cast(_6175.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6178
            
            return self._parent._cast(_6178.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6186
            
            return self._parent._cast(_6186.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def planetary_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6188
            
            return self._parent._cast(_6188.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6195
            
            return self._parent._cast(_6195.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6198
            
            return self._parent._cast(_6198.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6202
            
            return self._parent._cast(_6202.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6205
            
            return self._parent._cast(_6205.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6208
            
            return self._parent._cast(_6208.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6211
            
            return self._parent._cast(_6211.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6214
            
            return self._parent._cast(_6214.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6223
            
            return self._parent._cast(_6223.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6229
            
            return self._parent._cast(_6229.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6232
            
            return self._parent._cast(_6232.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6376
            
            return self._parent._cast(_6376.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6378
            
            return self._parent._cast(_6378.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis)

        @property
        def belt_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6382
            
            return self._parent._cast(_6382.BeltConnectionCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6385
            
            return self._parent._cast(_6385.BevelDifferentialGearMeshCompoundDynamicAnalysis)

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6390
            
            return self._parent._cast(_6390.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def clutch_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6395
            
            return self._parent._cast(_6395.ClutchConnectionCompoundDynamicAnalysis)

        @property
        def coaxial_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6397
            
            return self._parent._cast(_6397.CoaxialConnectionCompoundDynamicAnalysis)

        @property
        def concept_coupling_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6400
            
            return self._parent._cast(_6400.ConceptCouplingConnectionCompoundDynamicAnalysis)

        @property
        def concept_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6403
            
            return self._parent._cast(_6403.ConceptGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6406
            
            return self._parent._cast(_6406.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6408
            
            return self._parent._cast(_6408.ConnectionCompoundDynamicAnalysis)

        @property
        def coupling_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6411
            
            return self._parent._cast(_6411.CouplingConnectionCompoundDynamicAnalysis)

        @property
        def cvt_belt_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6413
            
            return self._parent._cast(_6413.CVTBeltConnectionCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6417
            
            return self._parent._cast(_6417.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6419
            
            return self._parent._cast(_6419.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6421
            
            return self._parent._cast(_6421.CylindricalGearMeshCompoundDynamicAnalysis)

        @property
        def face_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6427
            
            return self._parent._cast(_6427.FaceGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6432
            
            return self._parent._cast(_6432.GearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6436
            
            return self._parent._cast(_6436.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6438
            
            return self._parent._cast(_6438.InterMountableComponentConnectionCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6440
            
            return self._parent._cast(_6440.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6443
            
            return self._parent._cast(_6443.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6446
            
            return self._parent._cast(_6446.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6454
            
            return self._parent._cast(_6454.PartToPartShearCouplingConnectionCompoundDynamicAnalysis)

        @property
        def planetary_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6456
            
            return self._parent._cast(_6456.PlanetaryConnectionCompoundDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6463
            
            return self._parent._cast(_6463.RingPinsToDiscConnectionCompoundDynamicAnalysis)

        @property
        def rolling_ring_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6466
            
            return self._parent._cast(_6466.RollingRingConnectionCompoundDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6470
            
            return self._parent._cast(_6470.ShaftToMountableComponentConnectionCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6473
            
            return self._parent._cast(_6473.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def spring_damper_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6476
            
            return self._parent._cast(_6476.SpringDamperConnectionCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6479
            
            return self._parent._cast(_6479.StraightBevelDiffGearMeshCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6482
            
            return self._parent._cast(_6482.StraightBevelGearMeshCompoundDynamicAnalysis)

        @property
        def torque_converter_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6491
            
            return self._parent._cast(_6491.TorqueConverterConnectionCompoundDynamicAnalysis)

        @property
        def worm_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6497
            
            return self._parent._cast(_6497.WormGearMeshCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6500
            
            return self._parent._cast(_6500.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6642
            
            return self._parent._cast(_6642.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6644
            
            return self._parent._cast(_6644.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def belt_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6648
            
            return self._parent._cast(_6648.BeltConnectionCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6651
            
            return self._parent._cast(_6651.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6656
            
            return self._parent._cast(_6656.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def clutch_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6661
            
            return self._parent._cast(_6661.ClutchConnectionCompoundCriticalSpeedAnalysis)

        @property
        def coaxial_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6663
            
            return self._parent._cast(_6663.CoaxialConnectionCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6666
            
            return self._parent._cast(_6666.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6669
            
            return self._parent._cast(_6669.ConceptGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6672
            
            return self._parent._cast(_6672.ConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6674
            
            return self._parent._cast(_6674.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def coupling_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6677
            
            return self._parent._cast(_6677.CouplingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def cvt_belt_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6679
            
            return self._parent._cast(_6679.CVTBeltConnectionCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6683
            
            return self._parent._cast(_6683.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6685
            
            return self._parent._cast(_6685.CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6687
            
            return self._parent._cast(_6687.CylindricalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6693
            
            return self._parent._cast(_6693.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6698
            
            return self._parent._cast(_6698.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6702
            
            return self._parent._cast(_6702.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6704
            
            return self._parent._cast(_6704.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6706
            
            return self._parent._cast(_6706.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6709
            
            return self._parent._cast(_6709.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6712
            
            return self._parent._cast(_6712.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6720
            
            return self._parent._cast(_6720.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def planetary_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6722
            
            return self._parent._cast(_6722.PlanetaryConnectionCompoundCriticalSpeedAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6729
            
            return self._parent._cast(_6729.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6732
            
            return self._parent._cast(_6732.RollingRingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6736
            
            return self._parent._cast(_6736.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6739
            
            return self._parent._cast(_6739.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6742
            
            return self._parent._cast(_6742.SpringDamperConnectionCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6745
            
            return self._parent._cast(_6745.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6748
            
            return self._parent._cast(_6748.StraightBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6757
            
            return self._parent._cast(_6757.TorqueConverterConnectionCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6763
            
            return self._parent._cast(_6763.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6766
            
            return self._parent._cast(_6766.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7106
            
            return self._parent._cast(_7106.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7108
            
            return self._parent._cast(_7108.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def belt_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7112
            
            return self._parent._cast(_7112.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7115
            
            return self._parent._cast(_7115.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7120
            
            return self._parent._cast(_7120.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def clutch_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7125
            
            return self._parent._cast(_7125.ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coaxial_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7127
            
            return self._parent._cast(_7127.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7130
            
            return self._parent._cast(_7130.ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7133
            
            return self._parent._cast(_7133.ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7136
            
            return self._parent._cast(_7136.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7138
            
            return self._parent._cast(_7138.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7141
            
            return self._parent._cast(_7141.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cvt_belt_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7143
            
            return self._parent._cast(_7143.CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7147
            
            return self._parent._cast(_7147.CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7149
            
            return self._parent._cast(_7149.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7151
            
            return self._parent._cast(_7151.CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7157
            
            return self._parent._cast(_7157.FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7162
            
            return self._parent._cast(_7162.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7166
            
            return self._parent._cast(_7166.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7168
            
            return self._parent._cast(_7168.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7170
            
            return self._parent._cast(_7170.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7173
            
            return self._parent._cast(_7173.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7176
            
            return self._parent._cast(_7176.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7184
            
            return self._parent._cast(_7184.PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planetary_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7186
            
            return self._parent._cast(_7186.PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def ring_pins_to_disc_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7193
            
            return self._parent._cast(_7193.RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def rolling_ring_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7196
            
            return self._parent._cast(_7196.RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7200
            
            return self._parent._cast(_7200.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7203
            
            return self._parent._cast(_7203.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7206
            
            return self._parent._cast(_7206.SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7209
            
            return self._parent._cast(_7209.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7212
            
            return self._parent._cast(_7212.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7221
            
            return self._parent._cast(_7221.TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7227
            
            return self._parent._cast(_7227.WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7230
            
            return self._parent._cast(_7230.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7371
            
            return self._parent._cast(_7371.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7373
            
            return self._parent._cast(_7373.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def belt_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7377
            
            return self._parent._cast(_7377.BeltConnectionCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7380
            
            return self._parent._cast(_7380.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7385
            
            return self._parent._cast(_7385.BevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def clutch_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7390
            
            return self._parent._cast(_7390.ClutchConnectionCompoundAdvancedSystemDeflection)

        @property
        def coaxial_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7392
            
            return self._parent._cast(_7392.CoaxialConnectionCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7395
            
            return self._parent._cast(_7395.ConceptCouplingConnectionCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7398
            
            return self._parent._cast(_7398.ConceptGearMeshCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7401
            
            return self._parent._cast(_7401.ConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7403
            
            return self._parent._cast(_7403.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def coupling_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7406
            
            return self._parent._cast(_7406.CouplingConnectionCompoundAdvancedSystemDeflection)

        @property
        def cvt_belt_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7408
            
            return self._parent._cast(_7408.CVTBeltConnectionCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7412
            
            return self._parent._cast(_7412.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7414
            
            return self._parent._cast(_7414.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection)

        @property
        def cylindrical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7416
            
            return self._parent._cast(_7416.CylindricalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def face_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7422
            
            return self._parent._cast(_7422.FaceGearMeshCompoundAdvancedSystemDeflection)

        @property
        def gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7427
            
            return self._parent._cast(_7427.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7431
            
            return self._parent._cast(_7431.HypoidGearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7433
            
            return self._parent._cast(_7433.InterMountableComponentConnectionCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7435
            
            return self._parent._cast(_7435.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7438
            
            return self._parent._cast(_7438.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7441
            
            return self._parent._cast(_7441.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7449
            
            return self._parent._cast(_7449.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection)

        @property
        def planetary_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7451
            
            return self._parent._cast(_7451.PlanetaryConnectionCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_to_disc_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7458
            
            return self._parent._cast(_7458.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7461
            
            return self._parent._cast(_7461.RollingRingConnectionCompoundAdvancedSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7465
            
            return self._parent._cast(_7465.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7468
            
            return self._parent._cast(_7468.SpiralBevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def spring_damper_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7471
            
            return self._parent._cast(_7471.SpringDamperConnectionCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7474
            
            return self._parent._cast(_7474.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7477
            
            return self._parent._cast(_7477.StraightBevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def torque_converter_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7486
            
            return self._parent._cast(_7486.TorqueConverterConnectionCompoundAdvancedSystemDeflection)

        @property
        def worm_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7492
            
            return self._parent._cast(_7492.WormGearMeshCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7495
            
            return self._parent._cast(_7495.ZerolBevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(self) -> 'ConnectionCompoundAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionCompoundAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis':
        return self._Cast_ConnectionCompoundAnalysis(self)
