"""_3168.py

KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2301
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3035
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3162
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse',)


class KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse(_3162.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3162.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3128
            
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
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2301.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        """KlingelnbergCycloPalloidSpiralBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2301.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        """KlingelnbergCycloPalloidSpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3035.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3035.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse(self)
