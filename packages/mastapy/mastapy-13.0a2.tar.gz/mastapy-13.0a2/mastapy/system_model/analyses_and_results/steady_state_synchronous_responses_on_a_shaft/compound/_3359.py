"""_3359.py

AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3228
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3387
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft',)


class AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(_3387.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft):
    """AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
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
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3366
            
            return self._parent._cast(_3366.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3371
            
            return self._parent._cast(_3371.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3417
            
            return self._parent._cast(_3417.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3454
            
            return self._parent._cast(_3454.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3460
            
            return self._parent._cast(_3460.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3463
            
            return self._parent._cast(_3463.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3481
            
            return self._parent._cast(_3481.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_3228.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft]':
        """List[AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3228.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft]':
        """List[AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(self)
