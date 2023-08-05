"""_3169.py

KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.part_model.gears import _2520
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3036
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3167, _3168, _3163
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse',)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse(_3163.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3163.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3129
            
            return self._parent._cast(_3129.ConicalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3155
            
            return self._parent._cast(_3155.GearSetCompoundSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3193
            
            return self._parent._cast(_3193.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3095
            
            return self._parent._cast(_3095.AbstractAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3174
            
            return self._parent._cast(_3174.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2520.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2520.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3036.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_steady_state_synchronous_response(self) -> 'List[_3167.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse]: 'KlingelnbergCycloPalloidSpiralBevelGearsCompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_steady_state_synchronous_response(self) -> 'List[_3168.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse]: 'KlingelnbergCycloPalloidSpiralBevelMeshesCompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3036.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse(self)
