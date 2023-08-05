"""_3100.py

AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2966
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3128
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse',)


class AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse(_3128.ConicalGearMeshCompoundSteadyStateSynchronousResponse):
    """AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3128.ConicalGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3154
            
            return self._parent._cast(_3154.GearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3160
            
            return self._parent._cast(_3160.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3130
            
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
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3107
            
            return self._parent._cast(_3107.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3112
            
            return self._parent._cast(_3112.BevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3158
            
            return self._parent._cast(_3158.HypoidGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3195
            
            return self._parent._cast(_3195.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3201
            
            return self._parent._cast(_3201.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3204
            
            return self._parent._cast(_3204.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3222
            
            return self._parent._cast(_3222.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(self) -> 'AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_2966.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse]':
        """List[AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2966.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse]':
        """List[AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse':
        return self._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse(self)
