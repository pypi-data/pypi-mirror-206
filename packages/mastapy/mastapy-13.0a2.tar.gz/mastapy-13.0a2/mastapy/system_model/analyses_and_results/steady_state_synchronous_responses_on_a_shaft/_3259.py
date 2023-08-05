"""_3259.py

ConnectionSteadyStateSynchronousResponseOnAShaft
"""
from mastapy.system_model.connections_and_sockets import _2253
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3329
from mastapy.system_model.analyses_and_results.analysis_cases import _7503
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'ConnectionSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionSteadyStateSynchronousResponseOnAShaft',)


class ConnectionSteadyStateSynchronousResponseOnAShaft(_7503.ConnectionStaticLoadAnalysisCase):
    """ConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_ConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'ConnectionSteadyStateSynchronousResponseOnAShaft'):
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
        def connection_steady_state_synchronous_response_on_a_shaft(self) -> 'ConnectionSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionSteadyStateSynchronousResponseOnAShaft.TYPE'):
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
    def steady_state_synchronous_response_on_a_shaft(self) -> '_3329.SteadyStateSynchronousResponseOnAShaft':
        """SteadyStateSynchronousResponseOnAShaft: 'SteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_ConnectionSteadyStateSynchronousResponseOnAShaft(self)
