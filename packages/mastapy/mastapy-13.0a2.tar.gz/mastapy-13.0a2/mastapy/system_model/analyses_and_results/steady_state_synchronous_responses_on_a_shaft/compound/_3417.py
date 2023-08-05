"""_3417.py

HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2296
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3286
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3359
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft',)


class HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(_3359.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft):
    """HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3359.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3387
            
            return self._parent._cast(_3387.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3413
            
            return self._parent._cast(_3413.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3419
            
            return self._parent._cast(_3419.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3389
            
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
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2296.HypoidGearMesh':
        """HypoidGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2296.HypoidGearMesh':
        """HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3286.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft]':
        """List[HypoidGearMeshSteadyStateSynchronousResponseOnAShaft]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3286.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft]':
        """List[HypoidGearMeshSteadyStateSynchronousResponseOnAShaft]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(self)
