"""_3515.py

ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2288
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'ConicalGearMeshSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshSteadyStateSynchronousResponseAtASpeed',)


class ConicalGearMeshSteadyStateSynchronousResponseAtASpeed(_3541.GearMeshSteadyStateSynchronousResponseAtASpeed):
    """ConicalGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_ConicalGearMeshSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConicalGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'ConicalGearMeshSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3541.GearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3548
            
            return self._parent._cast(_3548.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3518
            
            return self._parent._cast(_3518.ConnectionSteadyStateSynchronousResponseAtASpeed)

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
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3487
            
            return self._parent._cast(_3487.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3494
            
            return self._parent._cast(_3494.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3499
            
            return self._parent._cast(_3499.BevelGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3545
            
            return self._parent._cast(_3545.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed)

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
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3582
            
            return self._parent._cast(_3582.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3589
            
            return self._parent._cast(_3589.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3592
            
            return self._parent._cast(_3592.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3610
            
            return self._parent._cast(_3610.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(self) -> 'ConicalGearMeshSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2288.ConicalGearMesh':
        """ConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ConicalGearMeshSteadyStateSynchronousResponseAtASpeed]':
        """List[ConicalGearMeshSteadyStateSynchronousResponseAtASpeed]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearMeshSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_ConicalGearMeshSteadyStateSynchronousResponseAtASpeed(self)
