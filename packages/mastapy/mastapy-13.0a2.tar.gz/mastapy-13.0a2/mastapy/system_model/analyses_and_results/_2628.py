"""_2628.py

ConnectionAnalysis
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2632
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'ConnectionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionAnalysis',)


class ConnectionAnalysis(_2632.DesignEntitySingleContextAnalysis):
    """ConnectionAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_ANALYSIS

    class _Cast_ConnectionAnalysis:
        """Special nested class for casting ConnectionAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectionAnalysis'):
            self._parent = parent

        @property
        def design_entity_single_context_analysis(self):
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
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2965
            
            return self._parent._cast(_2965.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2966
            
            return self._parent._cast(_2966.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse)

        @property
        def belt_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2971
            
            return self._parent._cast(_2971.BeltConnectionSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2973
            
            return self._parent._cast(_2973.BevelDifferentialGearMeshSteadyStateSynchronousResponse)

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2978
            
            return self._parent._cast(_2978.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def clutch_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2983
            
            return self._parent._cast(_2983.ClutchConnectionSteadyStateSynchronousResponse)

        @property
        def coaxial_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2986
            
            return self._parent._cast(_2986.CoaxialConnectionSteadyStateSynchronousResponse)

        @property
        def concept_coupling_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2988
            
            return self._parent._cast(_2988.ConceptCouplingConnectionSteadyStateSynchronousResponse)

        @property
        def concept_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2991
            
            return self._parent._cast(_2991.ConceptGearMeshSteadyStateSynchronousResponse)

        @property
        def conical_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2994
            
            return self._parent._cast(_2994.ConicalGearMeshSteadyStateSynchronousResponse)

        @property
        def connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2997
            
            return self._parent._cast(_2997.ConnectionSteadyStateSynchronousResponse)

        @property
        def coupling_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2999
            
            return self._parent._cast(_2999.CouplingConnectionSteadyStateSynchronousResponse)

        @property
        def cvt_belt_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3002
            
            return self._parent._cast(_3002.CVTBeltConnectionSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3006
            
            return self._parent._cast(_3006.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3007
            
            return self._parent._cast(_3007.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3009
            
            return self._parent._cast(_3009.CylindricalGearMeshSteadyStateSynchronousResponse)

        @property
        def face_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3016
            
            return self._parent._cast(_3016.FaceGearMeshSteadyStateSynchronousResponse)

        @property
        def gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3021
            
            return self._parent._cast(_3021.GearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3025
            
            return self._parent._cast(_3025.HypoidGearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3028
            
            return self._parent._cast(_3028.InterMountableComponentConnectionSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3029
            
            return self._parent._cast(_3029.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3032
            
            return self._parent._cast(_3032.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3035
            
            return self._parent._cast(_3035.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3043
            
            return self._parent._cast(_3043.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse)

        @property
        def planetary_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3046
            
            return self._parent._cast(_3046.PlanetaryConnectionSteadyStateSynchronousResponse)

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3053
            
            return self._parent._cast(_3053.RingPinsToDiscConnectionSteadyStateSynchronousResponse)

        @property
        def rolling_ring_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3055
            
            return self._parent._cast(_3055.RollingRingConnectionSteadyStateSynchronousResponse)

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3060
            
            return self._parent._cast(_3060.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3062
            
            return self._parent._cast(_3062.SpiralBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def spring_damper_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3065
            
            return self._parent._cast(_3065.SpringDamperConnectionSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3071
            
            return self._parent._cast(_3071.StraightBevelDiffGearMeshSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3074
            
            return self._parent._cast(_3074.StraightBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def torque_converter_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3083
            
            return self._parent._cast(_3083.TorqueConverterConnectionSteadyStateSynchronousResponse)

        @property
        def worm_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3089
            
            return self._parent._cast(_3089.WormGearMeshSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3092
            
            return self._parent._cast(_3092.ZerolBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3227
            
            return self._parent._cast(_3227.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3228
            
            return self._parent._cast(_3228.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def belt_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3233
            
            return self._parent._cast(_3233.BeltConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3235
            
            return self._parent._cast(_3235.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3240
            
            return self._parent._cast(_3240.BevelGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3245
            
            return self._parent._cast(_3245.ClutchConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def coaxial_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3248
            
            return self._parent._cast(_3248.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3250
            
            return self._parent._cast(_3250.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3253
            
            return self._parent._cast(_3253.ConceptGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3256
            
            return self._parent._cast(_3256.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3259
            
            return self._parent._cast(_3259.ConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3261
            
            return self._parent._cast(_3261.CouplingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_belt_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3264
            
            return self._parent._cast(_3264.CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3268
            
            return self._parent._cast(_3268.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3269
            
            return self._parent._cast(_3269.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3271
            
            return self._parent._cast(_3271.CylindricalGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3277
            
            return self._parent._cast(_3277.FaceGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3282
            
            return self._parent._cast(_3282.GearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3286
            
            return self._parent._cast(_3286.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3289
            
            return self._parent._cast(_3289.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3290
            
            return self._parent._cast(_3290.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3293
            
            return self._parent._cast(_3293.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3296
            
            return self._parent._cast(_3296.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3304
            
            return self._parent._cast(_3304.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def planetary_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3307
            
            return self._parent._cast(_3307.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3314
            
            return self._parent._cast(_3314.RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def rolling_ring_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3316
            
            return self._parent._cast(_3316.RollingRingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3321
            
            return self._parent._cast(_3321.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3323
            
            return self._parent._cast(_3323.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3326
            
            return self._parent._cast(_3326.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3330
            
            return self._parent._cast(_3330.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3333
            
            return self._parent._cast(_3333.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3342
            
            return self._parent._cast(_3342.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def worm_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3348
            
            return self._parent._cast(_3348.WormGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3351
            
            return self._parent._cast(_3351.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3486
            
            return self._parent._cast(_3486.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3487
            
            return self._parent._cast(_3487.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def belt_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3492
            
            return self._parent._cast(_3492.BeltConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3494
            
            return self._parent._cast(_3494.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3499
            
            return self._parent._cast(_3499.BevelGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3504
            
            return self._parent._cast(_3504.ClutchConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def coaxial_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3507
            
            return self._parent._cast(_3507.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3509
            
            return self._parent._cast(_3509.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3512
            
            return self._parent._cast(_3512.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3515
            
            return self._parent._cast(_3515.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3518
            
            return self._parent._cast(_3518.ConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3520
            
            return self._parent._cast(_3520.CouplingConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_belt_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3523
            
            return self._parent._cast(_3523.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3527
            
            return self._parent._cast(_3527.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3528
            
            return self._parent._cast(_3528.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3530
            
            return self._parent._cast(_3530.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def face_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3536
            
            return self._parent._cast(_3536.FaceGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3541
            
            return self._parent._cast(_3541.GearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3545
            
            return self._parent._cast(_3545.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3548
            
            return self._parent._cast(_3548.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3549
            
            return self._parent._cast(_3549.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3552
            
            return self._parent._cast(_3552.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3555
            
            return self._parent._cast(_3555.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3563
            
            return self._parent._cast(_3563.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def planetary_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3566
            
            return self._parent._cast(_3566.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3573
            
            return self._parent._cast(_3573.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3575
            
            return self._parent._cast(_3575.RollingRingConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3580
            
            return self._parent._cast(_3580.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3582
            
            return self._parent._cast(_3582.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3585
            
            return self._parent._cast(_3585.SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3589
            
            return self._parent._cast(_3589.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3592
            
            return self._parent._cast(_3592.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3601
            
            return self._parent._cast(_3601.TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def worm_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3607
            
            return self._parent._cast(_3607.WormGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3610
            
            return self._parent._cast(_3610.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3745
            
            return self._parent._cast(_3745.AbstractShaftToMountableComponentConnectionStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3746
            
            return self._parent._cast(_3746.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def belt_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3751
            
            return self._parent._cast(_3751.BeltConnectionStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3753
            
            return self._parent._cast(_3753.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3758
            
            return self._parent._cast(_3758.BevelGearMeshStabilityAnalysis)

        @property
        def clutch_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3763
            
            return self._parent._cast(_3763.ClutchConnectionStabilityAnalysis)

        @property
        def coaxial_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3766
            
            return self._parent._cast(_3766.CoaxialConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3768
            
            return self._parent._cast(_3768.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def concept_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3771
            
            return self._parent._cast(_3771.ConceptGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3774
            
            return self._parent._cast(_3774.ConicalGearMeshStabilityAnalysis)

        @property
        def connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3777
            
            return self._parent._cast(_3777.ConnectionStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3779
            
            return self._parent._cast(_3779.CouplingConnectionStabilityAnalysis)

        @property
        def cvt_belt_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3783
            
            return self._parent._cast(_3783.CVTBeltConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3787
            
            return self._parent._cast(_3787.CycloidalDiscCentralBearingConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3788
            
            return self._parent._cast(_3788.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3790
            
            return self._parent._cast(_3790.CylindricalGearMeshStabilityAnalysis)

        @property
        def face_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3796
            
            return self._parent._cast(_3796.FaceGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3801
            
            return self._parent._cast(_3801.GearMeshStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3805
            
            return self._parent._cast(_3805.HypoidGearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3808
            
            return self._parent._cast(_3808.InterMountableComponentConnectionStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3809
            
            return self._parent._cast(_3809.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3812
            
            return self._parent._cast(_3812.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3815
            
            return self._parent._cast(_3815.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3823
            
            return self._parent._cast(_3823.PartToPartShearCouplingConnectionStabilityAnalysis)

        @property
        def planetary_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3826
            
            return self._parent._cast(_3826.PlanetaryConnectionStabilityAnalysis)

        @property
        def ring_pins_to_disc_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3833
            
            return self._parent._cast(_3833.RingPinsToDiscConnectionStabilityAnalysis)

        @property
        def rolling_ring_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3835
            
            return self._parent._cast(_3835.RollingRingConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3840
            
            return self._parent._cast(_3840.ShaftToMountableComponentConnectionStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3842
            
            return self._parent._cast(_3842.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def spring_damper_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3845
            
            return self._parent._cast(_3845.SpringDamperConnectionStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3850
            
            return self._parent._cast(_3850.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3853
            
            return self._parent._cast(_3853.StraightBevelGearMeshStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3862
            
            return self._parent._cast(_3862.TorqueConverterConnectionStabilityAnalysis)

        @property
        def worm_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3868
            
            return self._parent._cast(_3868.WormGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3871
            
            return self._parent._cast(_3871.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4012
            
            return self._parent._cast(_4012.AbstractShaftToMountableComponentConnectionPowerFlow)

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
        def coaxial_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4033
            
            return self._parent._cast(_4033.CoaxialConnectionPowerFlow)

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
        def connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4044
            
            return self._parent._cast(_4044.ConnectionPowerFlow)

        @property
        def coupling_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4046
            
            return self._parent._cast(_4046.CouplingConnectionPowerFlow)

        @property
        def cvt_belt_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4049
            
            return self._parent._cast(_4049.CVTBeltConnectionPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4053
            
            return self._parent._cast(_4053.CycloidalDiscCentralBearingConnectionPowerFlow)

        @property
        def cycloidal_disc_planetary_bearing_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4054
            
            return self._parent._cast(_4054.CycloidalDiscPlanetaryBearingConnectionPowerFlow)

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
        def inter_mountable_component_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4075
            
            return self._parent._cast(_4075.InterMountableComponentConnectionPowerFlow)

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
        def planetary_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4093
            
            return self._parent._cast(_4093.PlanetaryConnectionPowerFlow)

        @property
        def ring_pins_to_disc_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4102
            
            return self._parent._cast(_4102.RingPinsToDiscConnectionPowerFlow)

        @property
        def rolling_ring_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4104
            
            return self._parent._cast(_4104.RollingRingConnectionPowerFlow)

        @property
        def shaft_to_mountable_component_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4109
            
            return self._parent._cast(_4109.ShaftToMountableComponentConnectionPowerFlow)

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
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4274
            
            return self._parent._cast(_4274.AbstractShaftToMountableComponentConnectionParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4275
            
            return self._parent._cast(_4275.AGMAGleasonConicalGearMeshParametricStudyTool)

        @property
        def belt_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4280
            
            return self._parent._cast(_4280.BeltConnectionParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4282
            
            return self._parent._cast(_4282.BevelDifferentialGearMeshParametricStudyTool)

        @property
        def bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4287
            
            return self._parent._cast(_4287.BevelGearMeshParametricStudyTool)

        @property
        def clutch_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4292
            
            return self._parent._cast(_4292.ClutchConnectionParametricStudyTool)

        @property
        def coaxial_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4295
            
            return self._parent._cast(_4295.CoaxialConnectionParametricStudyTool)

        @property
        def concept_coupling_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4297
            
            return self._parent._cast(_4297.ConceptCouplingConnectionParametricStudyTool)

        @property
        def concept_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4300
            
            return self._parent._cast(_4300.ConceptGearMeshParametricStudyTool)

        @property
        def conical_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4303
            
            return self._parent._cast(_4303.ConicalGearMeshParametricStudyTool)

        @property
        def connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4306
            
            return self._parent._cast(_4306.ConnectionParametricStudyTool)

        @property
        def coupling_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4308
            
            return self._parent._cast(_4308.CouplingConnectionParametricStudyTool)

        @property
        def cvt_belt_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4311
            
            return self._parent._cast(_4311.CVTBeltConnectionParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4315
            
            return self._parent._cast(_4315.CycloidalDiscCentralBearingConnectionParametricStudyTool)

        @property
        def cycloidal_disc_planetary_bearing_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4317
            
            return self._parent._cast(_4317.CycloidalDiscPlanetaryBearingConnectionParametricStudyTool)

        @property
        def cylindrical_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4318
            
            return self._parent._cast(_4318.CylindricalGearMeshParametricStudyTool)

        @property
        def face_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4331
            
            return self._parent._cast(_4331.FaceGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4336
            
            return self._parent._cast(_4336.GearMeshParametricStudyTool)

        @property
        def hypoid_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4340
            
            return self._parent._cast(_4340.HypoidGearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4343
            
            return self._parent._cast(_4343.InterMountableComponentConnectionParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4344
            
            return self._parent._cast(_4344.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4347
            
            return self._parent._cast(_4347.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4350
            
            return self._parent._cast(_4350.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool)

        @property
        def part_to_part_shear_coupling_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4369
            
            return self._parent._cast(_4369.PartToPartShearCouplingConnectionParametricStudyTool)

        @property
        def planetary_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4372
            
            return self._parent._cast(_4372.PlanetaryConnectionParametricStudyTool)

        @property
        def ring_pins_to_disc_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4379
            
            return self._parent._cast(_4379.RingPinsToDiscConnectionParametricStudyTool)

        @property
        def rolling_ring_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4381
            
            return self._parent._cast(_4381.RollingRingConnectionParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4386
            
            return self._parent._cast(_4386.ShaftToMountableComponentConnectionParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4388
            
            return self._parent._cast(_4388.SpiralBevelGearMeshParametricStudyTool)

        @property
        def spring_damper_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4391
            
            return self._parent._cast(_4391.SpringDamperConnectionParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4394
            
            return self._parent._cast(_4394.StraightBevelDiffGearMeshParametricStudyTool)

        @property
        def straight_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4397
            
            return self._parent._cast(_4397.StraightBevelGearMeshParametricStudyTool)

        @property
        def torque_converter_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4406
            
            return self._parent._cast(_4406.TorqueConverterConnectionParametricStudyTool)

        @property
        def worm_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4412
            
            return self._parent._cast(_4412.WormGearMeshParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4415
            
            return self._parent._cast(_4415.ZerolBevelGearMeshParametricStudyTool)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4550
            
            return self._parent._cast(_4550.AbstractShaftToMountableComponentConnectionModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4551
            
            return self._parent._cast(_4551.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def belt_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4556
            
            return self._parent._cast(_4556.BeltConnectionModalAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4558
            
            return self._parent._cast(_4558.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4563
            
            return self._parent._cast(_4563.BevelGearMeshModalAnalysis)

        @property
        def clutch_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4568
            
            return self._parent._cast(_4568.ClutchConnectionModalAnalysis)

        @property
        def coaxial_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4571
            
            return self._parent._cast(_4571.CoaxialConnectionModalAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573
            
            return self._parent._cast(_4573.ConceptCouplingConnectionModalAnalysis)

        @property
        def concept_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4576
            
            return self._parent._cast(_4576.ConceptGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579
            
            return self._parent._cast(_4579.ConicalGearMeshModalAnalysis)

        @property
        def connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582
            
            return self._parent._cast(_4582.ConnectionModalAnalysis)

        @property
        def coupling_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585
            
            return self._parent._cast(_4585.CouplingConnectionModalAnalysis)

        @property
        def cvt_belt_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588
            
            return self._parent._cast(_4588.CVTBeltConnectionModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4592
            
            return self._parent._cast(_4592.CycloidalDiscCentralBearingConnectionModalAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594
            
            return self._parent._cast(_4594.CycloidalDiscPlanetaryBearingConnectionModalAnalysis)

        @property
        def cylindrical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595
            
            return self._parent._cast(_4595.CylindricalGearMeshModalAnalysis)

        @property
        def face_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603
            
            return self._parent._cast(_4603.FaceGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609
            
            return self._parent._cast(_4609.GearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613
            
            return self._parent._cast(_4613.HypoidGearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616
            
            return self._parent._cast(_4616.InterMountableComponentConnectionModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617
            
            return self._parent._cast(_4617.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620
            
            return self._parent._cast(_4620.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623
            
            return self._parent._cast(_4623.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636
            
            return self._parent._cast(_4636.PartToPartShearCouplingConnectionModalAnalysis)

        @property
        def planetary_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639
            
            return self._parent._cast(_4639.PlanetaryConnectionModalAnalysis)

        @property
        def ring_pins_to_disc_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646
            
            return self._parent._cast(_4646.RingPinsToDiscConnectionModalAnalysis)

        @property
        def rolling_ring_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648
            
            return self._parent._cast(_4648.RollingRingConnectionModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654
            
            return self._parent._cast(_4654.ShaftToMountableComponentConnectionModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4656
            
            return self._parent._cast(_4656.SpiralBevelGearMeshModalAnalysis)

        @property
        def spring_damper_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659
            
            return self._parent._cast(_4659.SpringDamperConnectionModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662
            
            return self._parent._cast(_4662.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665
            
            return self._parent._cast(_4665.StraightBevelGearMeshModalAnalysis)

        @property
        def torque_converter_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674
            
            return self._parent._cast(_4674.TorqueConverterConnectionModalAnalysis)

        @property
        def worm_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683
            
            return self._parent._cast(_4683.WormGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686
            
            return self._parent._cast(_4686.ZerolBevelGearMeshModalAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4833
            
            return self._parent._cast(_4833.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4834
            
            return self._parent._cast(_4834.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def belt_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4839
            
            return self._parent._cast(_4839.BeltConnectionModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4841
            
            return self._parent._cast(_4841.BevelDifferentialGearMeshModalAnalysisAtAStiffness)

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4846
            
            return self._parent._cast(_4846.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def clutch_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4851
            
            return self._parent._cast(_4851.ClutchConnectionModalAnalysisAtAStiffness)

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4854
            
            return self._parent._cast(_4854.CoaxialConnectionModalAnalysisAtAStiffness)

        @property
        def concept_coupling_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4856
            
            return self._parent._cast(_4856.ConceptCouplingConnectionModalAnalysisAtAStiffness)

        @property
        def concept_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4859
            
            return self._parent._cast(_4859.ConceptGearMeshModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4862
            
            return self._parent._cast(_4862.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4865
            
            return self._parent._cast(_4865.ConnectionModalAnalysisAtAStiffness)

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4867
            
            return self._parent._cast(_4867.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def cvt_belt_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4870
            
            return self._parent._cast(_4870.CVTBeltConnectionModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4874
            
            return self._parent._cast(_4874.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4876
            
            return self._parent._cast(_4876.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4877
            
            return self._parent._cast(_4877.CylindricalGearMeshModalAnalysisAtAStiffness)

        @property
        def face_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4884
            
            return self._parent._cast(_4884.FaceGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4889
            
            return self._parent._cast(_4889.GearMeshModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4893
            
            return self._parent._cast(_4893.HypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4896
            
            return self._parent._cast(_4896.InterMountableComponentConnectionModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4897
            
            return self._parent._cast(_4897.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4900
            
            return self._parent._cast(_4900.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4903
            
            return self._parent._cast(_4903.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4911
            
            return self._parent._cast(_4911.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness)

        @property
        def planetary_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4914
            
            return self._parent._cast(_4914.PlanetaryConnectionModalAnalysisAtAStiffness)

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4921
            
            return self._parent._cast(_4921.RingPinsToDiscConnectionModalAnalysisAtAStiffness)

        @property
        def rolling_ring_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4923
            
            return self._parent._cast(_4923.RollingRingConnectionModalAnalysisAtAStiffness)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4928
            
            return self._parent._cast(_4928.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4930
            
            return self._parent._cast(_4930.SpiralBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def spring_damper_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4933
            
            return self._parent._cast(_4933.SpringDamperConnectionModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4936
            
            return self._parent._cast(_4936.StraightBevelDiffGearMeshModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4939
            
            return self._parent._cast(_4939.StraightBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4948
            
            return self._parent._cast(_4948.TorqueConverterConnectionModalAnalysisAtAStiffness)

        @property
        def worm_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4954
            
            return self._parent._cast(_4954.WormGearMeshModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4957
            
            return self._parent._cast(_4957.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5092
            
            return self._parent._cast(_5092.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5093
            
            return self._parent._cast(_5093.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed)

        @property
        def belt_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5098
            
            return self._parent._cast(_5098.BeltConnectionModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5100
            
            return self._parent._cast(_5100.BevelDifferentialGearMeshModalAnalysisAtASpeed)

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5105
            
            return self._parent._cast(_5105.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def clutch_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5110
            
            return self._parent._cast(_5110.ClutchConnectionModalAnalysisAtASpeed)

        @property
        def coaxial_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5113
            
            return self._parent._cast(_5113.CoaxialConnectionModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5115
            
            return self._parent._cast(_5115.ConceptCouplingConnectionModalAnalysisAtASpeed)

        @property
        def concept_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5118
            
            return self._parent._cast(_5118.ConceptGearMeshModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5121
            
            return self._parent._cast(_5121.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5124
            
            return self._parent._cast(_5124.ConnectionModalAnalysisAtASpeed)

        @property
        def coupling_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5126
            
            return self._parent._cast(_5126.CouplingConnectionModalAnalysisAtASpeed)

        @property
        def cvt_belt_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5129
            
            return self._parent._cast(_5129.CVTBeltConnectionModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5133
            
            return self._parent._cast(_5133.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5135
            
            return self._parent._cast(_5135.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5136
            
            return self._parent._cast(_5136.CylindricalGearMeshModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5142
            
            return self._parent._cast(_5142.FaceGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5147
            
            return self._parent._cast(_5147.GearMeshModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5151
            
            return self._parent._cast(_5151.HypoidGearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5154
            
            return self._parent._cast(_5154.InterMountableComponentConnectionModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5155
            
            return self._parent._cast(_5155.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5158
            
            return self._parent._cast(_5158.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5161
            
            return self._parent._cast(_5161.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5169
            
            return self._parent._cast(_5169.PartToPartShearCouplingConnectionModalAnalysisAtASpeed)

        @property
        def planetary_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5172
            
            return self._parent._cast(_5172.PlanetaryConnectionModalAnalysisAtASpeed)

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5179
            
            return self._parent._cast(_5179.RingPinsToDiscConnectionModalAnalysisAtASpeed)

        @property
        def rolling_ring_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5181
            
            return self._parent._cast(_5181.RollingRingConnectionModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5186
            
            return self._parent._cast(_5186.ShaftToMountableComponentConnectionModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5188
            
            return self._parent._cast(_5188.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def spring_damper_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5191
            
            return self._parent._cast(_5191.SpringDamperConnectionModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5194
            
            return self._parent._cast(_5194.StraightBevelDiffGearMeshModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5197
            
            return self._parent._cast(_5197.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5206
            
            return self._parent._cast(_5206.TorqueConverterConnectionModalAnalysisAtASpeed)

        @property
        def worm_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5212
            
            return self._parent._cast(_5212.WormGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5215
            
            return self._parent._cast(_5215.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5350
            
            return self._parent._cast(_5350.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5351
            
            return self._parent._cast(_5351.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def belt_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5358
            
            return self._parent._cast(_5358.BeltConnectionMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5360
            
            return self._parent._cast(_5360.BevelDifferentialGearMeshMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5365
            
            return self._parent._cast(_5365.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5370
            
            return self._parent._cast(_5370.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5374
            
            return self._parent._cast(_5374.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5376
            
            return self._parent._cast(_5376.ConceptCouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379
            
            return self._parent._cast(_5379.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382
            
            return self._parent._cast(_5382.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5385
            
            return self._parent._cast(_5385.ConnectionMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387
            
            return self._parent._cast(_5387.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390
            
            return self._parent._cast(_5390.CVTBeltConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5394
            
            return self._parent._cast(_5394.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396
            
            return self._parent._cast(_5396.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397
            
            return self._parent._cast(_5397.CylindricalGearMeshMultibodyDynamicsAnalysis)

        @property
        def face_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403
            
            return self._parent._cast(_5403.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408
            
            return self._parent._cast(_5408.GearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413
            
            return self._parent._cast(_5413.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420
            
            return self._parent._cast(_5420.InterMountableComponentConnectionMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421
            
            return self._parent._cast(_5421.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424
            
            return self._parent._cast(_5424.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427
            
            return self._parent._cast(_5427.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438
            
            return self._parent._cast(_5438.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def planetary_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441
            
            return self._parent._cast(_5441.PlanetaryConnectionMultibodyDynamicsAnalysis)

        @property
        def ring_pins_to_disc_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448
            
            return self._parent._cast(_5448.RingPinsToDiscConnectionMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5450
            
            return self._parent._cast(_5450.RollingRingConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457
            
            return self._parent._cast(_5457.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460
            
            return self._parent._cast(_5460.SpiralBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def spring_damper_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463
            
            return self._parent._cast(_5463.SpringDamperConnectionMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466
            
            return self._parent._cast(_5466.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469
            
            return self._parent._cast(_5469.StraightBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def torque_converter_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478
            
            return self._parent._cast(_5478.TorqueConverterConnectionMultibodyDynamicsAnalysis)

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487
            
            return self._parent._cast(_5487.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5490
            
            return self._parent._cast(_5490.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5652
            
            return self._parent._cast(_5652.AbstractShaftToMountableComponentConnectionHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5654
            
            return self._parent._cast(_5654.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def belt_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5658
            
            return self._parent._cast(_5658.BeltConnectionHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5661
            
            return self._parent._cast(_5661.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5666
            
            return self._parent._cast(_5666.BevelGearMeshHarmonicAnalysis)

        @property
        def clutch_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5670
            
            return self._parent._cast(_5670.ClutchConnectionHarmonicAnalysis)

        @property
        def coaxial_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5673
            
            return self._parent._cast(_5673.CoaxialConnectionHarmonicAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5676
            
            return self._parent._cast(_5676.ConceptCouplingConnectionHarmonicAnalysis)

        @property
        def concept_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5680
            
            return self._parent._cast(_5680.ConceptGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5683
            
            return self._parent._cast(_5683.ConicalGearMeshHarmonicAnalysis)

        @property
        def connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5685
            
            return self._parent._cast(_5685.ConnectionHarmonicAnalysis)

        @property
        def coupling_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5687
            
            return self._parent._cast(_5687.CouplingConnectionHarmonicAnalysis)

        @property
        def cvt_belt_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5690
            
            return self._parent._cast(_5690.CVTBeltConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5694
            
            return self._parent._cast(_5694.CycloidalDiscCentralBearingConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5696
            
            return self._parent._cast(_5696.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis)

        @property
        def cylindrical_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5698
            
            return self._parent._cast(_5698.CylindricalGearMeshHarmonicAnalysis)

        @property
        def face_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5717
            
            return self._parent._cast(_5717.FaceGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5724
            
            return self._parent._cast(_5724.GearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5739
            
            return self._parent._cast(_5739.HypoidGearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5741
            
            return self._parent._cast(_5741.InterMountableComponentConnectionHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5743
            
            return self._parent._cast(_5743.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5746
            
            return self._parent._cast(_5746.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5749
            
            return self._parent._cast(_5749.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5756
            
            return self._parent._cast(_5756.PartToPartShearCouplingConnectionHarmonicAnalysis)

        @property
        def planetary_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5760
            
            return self._parent._cast(_5760.PlanetaryConnectionHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5768
            
            return self._parent._cast(_5768.RingPinsToDiscConnectionHarmonicAnalysis)

        @property
        def rolling_ring_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5770
            
            return self._parent._cast(_5770.RollingRingConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5775
            
            return self._parent._cast(_5775.ShaftToMountableComponentConnectionHarmonicAnalysis)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5780
            
            return self._parent._cast(_5780.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def spring_damper_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5782
            
            return self._parent._cast(_5782.SpringDamperConnectionHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5787
            
            return self._parent._cast(_5787.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5790
            
            return self._parent._cast(_5790.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5798
            
            return self._parent._cast(_5798.TorqueConverterConnectionHarmonicAnalysis)

        @property
        def worm_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5806
            
            return self._parent._cast(_5806.WormGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5809
            
            return self._parent._cast(_5809.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5978
            
            return self._parent._cast(_5978.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5980
            
            return self._parent._cast(_5980.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5984
            
            return self._parent._cast(_5984.BeltConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5987
            
            return self._parent._cast(_5987.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5992
            
            return self._parent._cast(_5992.BevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5996
            
            return self._parent._cast(_5996.ClutchConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5999
            
            return self._parent._cast(_5999.CoaxialConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6001
            
            return self._parent._cast(_6001.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6005
            
            return self._parent._cast(_6005.ConceptGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6008
            
            return self._parent._cast(_6008.ConicalGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6010
            
            return self._parent._cast(_6010.ConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6012
            
            return self._parent._cast(_6012.CouplingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_belt_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6015
            
            return self._parent._cast(_6015.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6019
            
            return self._parent._cast(_6019.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6021
            
            return self._parent._cast(_6021.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6023
            
            return self._parent._cast(_6023.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6029
            
            return self._parent._cast(_6029.FaceGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6034
            
            return self._parent._cast(_6034.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6039
            
            return self._parent._cast(_6039.HypoidGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6041
            
            return self._parent._cast(_6041.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6043
            
            return self._parent._cast(_6043.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6046
            
            return self._parent._cast(_6046.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6049
            
            return self._parent._cast(_6049.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6056
            
            return self._parent._cast(_6056.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6059
            
            return self._parent._cast(_6059.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_to_disc_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6066
            
            return self._parent._cast(_6066.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6068
            
            return self._parent._cast(_6068.RollingRingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6073
            
            return self._parent._cast(_6073.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6076
            
            return self._parent._cast(_6076.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6078
            
            return self._parent._cast(_6078.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6082
            
            return self._parent._cast(_6082.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6085
            
            return self._parent._cast(_6085.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6093
            
            return self._parent._cast(_6093.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6100
            
            return self._parent._cast(_6100.WormGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6103
            
            return self._parent._cast(_6103.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation)

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
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6511
            
            return self._parent._cast(_6511.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6513
            
            return self._parent._cast(_6513.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis)

        @property
        def belt_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6517
            
            return self._parent._cast(_6517.BeltConnectionCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6520
            
            return self._parent._cast(_6520.BevelDifferentialGearMeshCriticalSpeedAnalysis)

        @property
        def bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6525
            
            return self._parent._cast(_6525.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def clutch_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6529
            
            return self._parent._cast(_6529.ClutchConnectionCriticalSpeedAnalysis)

        @property
        def coaxial_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6532
            
            return self._parent._cast(_6532.CoaxialConnectionCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6534
            
            return self._parent._cast(_6534.ConceptCouplingConnectionCriticalSpeedAnalysis)

        @property
        def concept_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6538
            
            return self._parent._cast(_6538.ConceptGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6541
            
            return self._parent._cast(_6541.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6543
            
            return self._parent._cast(_6543.ConnectionCriticalSpeedAnalysis)

        @property
        def coupling_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6545
            
            return self._parent._cast(_6545.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def cvt_belt_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6550
            
            return self._parent._cast(_6550.CVTBeltConnectionCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6554
            
            return self._parent._cast(_6554.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6556
            
            return self._parent._cast(_6556.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6558
            
            return self._parent._cast(_6558.CylindricalGearMeshCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6564
            
            return self._parent._cast(_6564.FaceGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6569
            
            return self._parent._cast(_6569.GearMeshCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6573
            
            return self._parent._cast(_6573.HypoidGearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6575
            
            return self._parent._cast(_6575.InterMountableComponentConnectionCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6577
            
            return self._parent._cast(_6577.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6580
            
            return self._parent._cast(_6580.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6583
            
            return self._parent._cast(_6583.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6590
            
            return self._parent._cast(_6590.PartToPartShearCouplingConnectionCriticalSpeedAnalysis)

        @property
        def planetary_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6593
            
            return self._parent._cast(_6593.PlanetaryConnectionCriticalSpeedAnalysis)

        @property
        def ring_pins_to_disc_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6600
            
            return self._parent._cast(_6600.RingPinsToDiscConnectionCriticalSpeedAnalysis)

        @property
        def rolling_ring_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6602
            
            return self._parent._cast(_6602.RollingRingConnectionCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6607
            
            return self._parent._cast(_6607.ShaftToMountableComponentConnectionCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6610
            
            return self._parent._cast(_6610.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6612
            
            return self._parent._cast(_6612.SpringDamperConnectionCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6616
            
            return self._parent._cast(_6616.StraightBevelDiffGearMeshCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6619
            
            return self._parent._cast(_6619.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6627
            
            return self._parent._cast(_6627.TorqueConverterConnectionCriticalSpeedAnalysis)

        @property
        def worm_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6634
            
            return self._parent._cast(_6634.WormGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6637
            
            return self._parent._cast(_6637.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6774
            
            return self._parent._cast(_6774.AbstractShaftToMountableComponentConnectionLoadCase)

        @property
        def agma_gleason_conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6779
            
            return self._parent._cast(_6779.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6785
            
            return self._parent._cast(_6785.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6788
            
            return self._parent._cast(_6788.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6793
            
            return self._parent._cast(_6793.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6797
            
            return self._parent._cast(_6797.ClutchConnectionLoadCase)

        @property
        def coaxial_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6800
            
            return self._parent._cast(_6800.CoaxialConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6802
            
            return self._parent._cast(_6802.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6806
            
            return self._parent._cast(_6806.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6810
            
            return self._parent._cast(_6810.ConicalGearMeshLoadCase)

        @property
        def connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6813
            
            return self._parent._cast(_6813.ConnectionLoadCase)

        @property
        def coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6815
            
            return self._parent._cast(_6815.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6818
            
            return self._parent._cast(_6818.CVTBeltConnectionLoadCase)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6822
            
            return self._parent._cast(_6822.CycloidalDiscCentralBearingConnectionLoadCase)

        @property
        def cycloidal_disc_planetary_bearing_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6824
            
            return self._parent._cast(_6824.CycloidalDiscPlanetaryBearingConnectionLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6827
            
            return self._parent._cast(_6827.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6849
            
            return self._parent._cast(_6849.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6856
            
            return self._parent._cast(_6856.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6870
            
            return self._parent._cast(_6870.HypoidGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6875
            
            return self._parent._cast(_6875.InterMountableComponentConnectionLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6877
            
            return self._parent._cast(_6877.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6880
            
            return self._parent._cast(_6880.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6883
            
            return self._parent._cast(_6883.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        @property
        def part_to_part_shear_coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6893
            
            return self._parent._cast(_6893.PartToPartShearCouplingConnectionLoadCase)

        @property
        def planetary_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6896
            
            return self._parent._cast(_6896.PlanetaryConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6908
            
            return self._parent._cast(_6908.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6910
            
            return self._parent._cast(_6910.RollingRingConnectionLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6915
            
            return self._parent._cast(_6915.ShaftToMountableComponentConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6918
            
            return self._parent._cast(_6918.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6920
            
            return self._parent._cast(_6920.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6924
            
            return self._parent._cast(_6924.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6927
            
            return self._parent._cast(_6927.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6936
            
            return self._parent._cast(_6936.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6947
            
            return self._parent._cast(_6947.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6950
            
            return self._parent._cast(_6950.ZerolBevelGearMeshLoadCase)

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6972
            
            return self._parent._cast(_6972.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6977
            
            return self._parent._cast(_6977.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def belt_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6982
            
            return self._parent._cast(_6982.BeltConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6985
            
            return self._parent._cast(_6985.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6990
            
            return self._parent._cast(_6990.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def clutch_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6995
            
            return self._parent._cast(_6995.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6997
            
            return self._parent._cast(_6997.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7000
            
            return self._parent._cast(_7000.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7003
            
            return self._parent._cast(_7003.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7006
            
            return self._parent._cast(_7006.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7008
            
            return self._parent._cast(_7008.ConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7011
            
            return self._parent._cast(_7011.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cvt_belt_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7014
            
            return self._parent._cast(_7014.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7018
            
            return self._parent._cast(_7018.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7019
            
            return self._parent._cast(_7019.CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7021
            
            return self._parent._cast(_7021.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7027
            
            return self._parent._cast(_7027.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7032
            
            return self._parent._cast(_7032.GearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7037
            
            return self._parent._cast(_7037.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7039
            
            return self._parent._cast(_7039.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7041
            
            return self._parent._cast(_7041.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7044
            
            return self._parent._cast(_7044.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7047
            
            return self._parent._cast(_7047.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_to_part_shear_coupling_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7055
            
            return self._parent._cast(_7055.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planetary_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7057
            
            return self._parent._cast(_7057.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def ring_pins_to_disc_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7064
            
            return self._parent._cast(_7064.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def rolling_ring_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7067
            
            return self._parent._cast(_7067.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7071
            
            return self._parent._cast(_7071.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7074
            
            return self._parent._cast(_7074.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7077
            
            return self._parent._cast(_7077.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7080
            
            return self._parent._cast(_7080.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7083
            
            return self._parent._cast(_7083.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7092
            
            return self._parent._cast(_7092.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7098
            
            return self._parent._cast(_7098.WormGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7101
            
            return self._parent._cast(_7101.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7235
            
            return self._parent._cast(_7235.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7240
            
            return self._parent._cast(_7240.AGMAGleasonConicalGearMeshAdvancedSystemDeflection)

        @property
        def belt_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7244
            
            return self._parent._cast(_7244.BeltConnectionAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7247
            
            return self._parent._cast(_7247.BevelDifferentialGearMeshAdvancedSystemDeflection)

        @property
        def bevel_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7252
            
            return self._parent._cast(_7252.BevelGearMeshAdvancedSystemDeflection)

        @property
        def clutch_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7257
            
            return self._parent._cast(_7257.ClutchConnectionAdvancedSystemDeflection)

        @property
        def coaxial_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7259
            
            return self._parent._cast(_7259.CoaxialConnectionAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7262
            
            return self._parent._cast(_7262.ConceptCouplingConnectionAdvancedSystemDeflection)

        @property
        def concept_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7265
            
            return self._parent._cast(_7265.ConceptGearMeshAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7268
            
            return self._parent._cast(_7268.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7270
            
            return self._parent._cast(_7270.ConnectionAdvancedSystemDeflection)

        @property
        def coupling_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7274
            
            return self._parent._cast(_7274.CouplingConnectionAdvancedSystemDeflection)

        @property
        def cvt_belt_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7277
            
            return self._parent._cast(_7277.CVTBeltConnectionAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7281
            
            return self._parent._cast(_7281.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection)

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7282
            
            return self._parent._cast(_7282.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection)

        @property
        def cylindrical_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7284
            
            return self._parent._cast(_7284.CylindricalGearMeshAdvancedSystemDeflection)

        @property
        def face_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7291
            
            return self._parent._cast(_7291.FaceGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7296
            
            return self._parent._cast(_7296.GearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7300
            
            return self._parent._cast(_7300.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7302
            
            return self._parent._cast(_7302.InterMountableComponentConnectionAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7304
            
            return self._parent._cast(_7304.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7307
            
            return self._parent._cast(_7307.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7310
            
            return self._parent._cast(_7310.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7319
            
            return self._parent._cast(_7319.PartToPartShearCouplingConnectionAdvancedSystemDeflection)

        @property
        def planetary_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7321
            
            return self._parent._cast(_7321.PlanetaryConnectionAdvancedSystemDeflection)

        @property
        def ring_pins_to_disc_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7328
            
            return self._parent._cast(_7328.RingPinsToDiscConnectionAdvancedSystemDeflection)

        @property
        def rolling_ring_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7331
            
            return self._parent._cast(_7331.RollingRingConnectionAdvancedSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7335
            
            return self._parent._cast(_7335.ShaftToMountableComponentConnectionAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7338
            
            return self._parent._cast(_7338.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def spring_damper_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7341
            
            return self._parent._cast(_7341.SpringDamperConnectionAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7344
            
            return self._parent._cast(_7344.StraightBevelDiffGearMeshAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7347
            
            return self._parent._cast(_7347.StraightBevelGearMeshAdvancedSystemDeflection)

        @property
        def torque_converter_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7356
            
            return self._parent._cast(_7356.TorqueConverterConnectionAdvancedSystemDeflection)

        @property
        def worm_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7363
            
            return self._parent._cast(_7363.WormGearMeshAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7366
            
            return self._parent._cast(_7366.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7500
            
            return self._parent._cast(_7500.ConnectionAnalysisCase)

        @property
        def connection_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7502
            
            return self._parent._cast(_7502.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7503
            
            return self._parent._cast(_7503.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis(self) -> 'ConnectionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def short_name(self) -> 'str':
        """str: 'ShortName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShortName

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'ConnectionAnalysis._Cast_ConnectionAnalysis':
        return self._Cast_ConnectionAnalysis(self)
