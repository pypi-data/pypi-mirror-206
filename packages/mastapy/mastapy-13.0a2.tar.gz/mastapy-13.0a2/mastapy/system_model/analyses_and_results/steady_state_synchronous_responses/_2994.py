"""_2994.py

ConicalGearMeshSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2288
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3021
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'ConicalGearMeshSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshSteadyStateSynchronousResponse',)


class ConicalGearMeshSteadyStateSynchronousResponse(_3021.GearMeshSteadyStateSynchronousResponse):
    """ConicalGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_ConicalGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting ConicalGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'ConicalGearMeshSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def gear_mesh_steady_state_synchronous_response(self):
            return self._parent._cast(_3021.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3028
            
            return self._parent._cast(_3028.InterMountableComponentConnectionSteadyStateSynchronousResponse)

        @property
        def connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2997
            
            return self._parent._cast(_2997.ConnectionSteadyStateSynchronousResponse)

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
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2966
            
            return self._parent._cast(_2966.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2973
            
            return self._parent._cast(_2973.BevelDifferentialGearMeshSteadyStateSynchronousResponse)

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2978
            
            return self._parent._cast(_2978.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3025
            
            return self._parent._cast(_3025.HypoidGearMeshSteadyStateSynchronousResponse)

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
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3062
            
            return self._parent._cast(_3062.SpiralBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3071
            
            return self._parent._cast(_3071.StraightBevelDiffGearMeshSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3074
            
            return self._parent._cast(_3074.StraightBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3092
            
            return self._parent._cast(_3092.ZerolBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def conical_gear_mesh_steady_state_synchronous_response(self) -> 'ConicalGearMeshSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshSteadyStateSynchronousResponse.TYPE'):
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
    def planetaries(self) -> 'List[ConicalGearMeshSteadyStateSynchronousResponse]':
        """List[ConicalGearMeshSteadyStateSynchronousResponse]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse':
        return self._Cast_ConicalGearMeshSteadyStateSynchronousResponse(self)
