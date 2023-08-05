"""_3160.py

InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3028
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3130
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse',)


class InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse(_3130.ConnectionCompoundSteadyStateSynchronousResponse):
    """InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def connection_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3130.ConnectionCompoundSteadyStateSynchronousResponse)

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
        def coupling_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3133
            
            return self._parent._cast(_3133.CouplingConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3135
            
            return self._parent._cast(_3135.CVTBeltConnectionCompoundSteadyStateSynchronousResponse)

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
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3185
            
            return self._parent._cast(_3185.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3188
            
            return self._parent._cast(_3188.RollingRingConnectionCompoundSteadyStateSynchronousResponse)

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
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(self) -> 'InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_3028.InterMountableComponentConnectionSteadyStateSynchronousResponse]':
        """List[InterMountableComponentConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3028.InterMountableComponentConnectionSteadyStateSynchronousResponse]':
        """List[InterMountableComponentConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse':
        return self._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse(self)
