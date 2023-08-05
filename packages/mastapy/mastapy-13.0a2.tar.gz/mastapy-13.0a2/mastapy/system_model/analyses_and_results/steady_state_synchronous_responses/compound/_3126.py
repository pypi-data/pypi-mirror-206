"""_3126.py

ConceptGearSetCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.part_model.gears import _2501
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2992
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3124, _3125, _3155
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'ConceptGearSetCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetCompoundSteadyStateSynchronousResponse',)


class ConceptGearSetCompoundSteadyStateSynchronousResponse(_3155.GearSetCompoundSteadyStateSynchronousResponse):
    """ConceptGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_ConceptGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'ConceptGearSetCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def gear_set_compound_steady_state_synchronous_response(self):
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
        def concept_gear_set_compound_steady_state_synchronous_response(self) -> 'ConceptGearSetCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearSetCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2501.ConceptGearSet':
        """ConceptGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2501.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2992.ConceptGearSetSteadyStateSynchronousResponse]':
        """List[ConceptGearSetSteadyStateSynchronousResponse]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gears_compound_steady_state_synchronous_response(self) -> 'List[_3124.ConceptGearCompoundSteadyStateSynchronousResponse]':
        """List[ConceptGearCompoundSteadyStateSynchronousResponse]: 'ConceptGearsCompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_compound_steady_state_synchronous_response(self) -> 'List[_3125.ConceptGearMeshCompoundSteadyStateSynchronousResponse]':
        """List[ConceptGearMeshCompoundSteadyStateSynchronousResponse]: 'ConceptMeshesCompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2992.ConceptGearSetSteadyStateSynchronousResponse]':
        """List[ConceptGearSetSteadyStateSynchronousResponse]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearSetCompoundSteadyStateSynchronousResponse._Cast_ConceptGearSetCompoundSteadyStateSynchronousResponse':
        return self._Cast_ConceptGearSetCompoundSteadyStateSynchronousResponse(self)
