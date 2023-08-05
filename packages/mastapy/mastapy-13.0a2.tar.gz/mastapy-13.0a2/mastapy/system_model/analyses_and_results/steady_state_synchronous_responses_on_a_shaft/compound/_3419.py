"""_3419.py

InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3289
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3389
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft',)


class InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft(_3389.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft):
    """InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3389.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3392
            
            return self._parent._cast(_3392.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3394
            
            return self._parent._cast(_3394.CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3444
            
            return self._parent._cast(_3444.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3447
            
            return self._parent._cast(_3447.RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_3289.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft]':
        """List[InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3289.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft]':
        """List[InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft(self)
