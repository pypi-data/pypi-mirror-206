"""_3166.py

KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.part_model.gears import _2518
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3033
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3164, _3165, _3163
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse',)


class KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse(_3163.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse'):
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
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(self) -> 'KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2518.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2518.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3033.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse]':
        """List[KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_steady_state_synchronous_response(self) -> 'List[_3164.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse]':
        """List[KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse]: 'KlingelnbergCycloPalloidHypoidGearsCompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_steady_state_synchronous_response(self) -> 'List[_3165.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse]: 'KlingelnbergCycloPalloidHypoidMeshesCompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3033.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse]':
        """List[KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse(self)
