"""_3740.py

ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2312
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3610
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3630
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed',)


class ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed(_3630.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed):
    """ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3630.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3618
            
            return self._parent._cast(_3618.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3646
            
            return self._parent._cast(_3646.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3672
            
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
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(self) -> 'ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2312.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2312.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3610.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed]':
        """List[ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3610.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed]':
        """List[ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed(self)
