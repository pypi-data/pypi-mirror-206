"""_3646.py

ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3515
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3672
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed',)


class ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed(_3672.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed):
    """ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3672.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3678
            
            return self._parent._cast(_3678.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3648
            
            return self._parent._cast(_3648.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

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
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3618
            
            return self._parent._cast(_3618.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3625
            
            return self._parent._cast(_3625.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3630
            
            return self._parent._cast(_3630.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3676
            
            return self._parent._cast(_3676.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

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
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3713
            
            return self._parent._cast(_3713.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3719
            
            return self._parent._cast(_3719.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3722
            
            return self._parent._cast(_3722.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3740
            
            return self._parent._cast(_3740.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self) -> 'ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self) -> 'List[ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]':
        """List[ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3515.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed]':
        """List[ConicalGearMeshSteadyStateSynchronousResponseAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3515.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed]':
        """List[ConicalGearMeshSteadyStateSynchronousResponseAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed(self)
