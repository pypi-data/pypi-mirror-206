"""_3418.py

HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.part_model.gears import _2514
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3287
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3416, _3417, _3360
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft',)


class HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft(_3360.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft):
    """HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3360.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3388
            
            return self._parent._cast(_3388.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3414
            
            return self._parent._cast(_3414.GearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3452
            
            return self._parent._cast(_3452.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3354
            
            return self._parent._cast(_3354.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3433
            
            return self._parent._cast(_3433.PartCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2514.HypoidGearSet':
        """HypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2514.HypoidGearSet':
        """HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3287.HypoidGearSetSteadyStateSynchronousResponseOnAShaft]':
        """List[HypoidGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gears_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3416.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft]: 'HypoidGearsCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsCompoundSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3417.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]: 'HypoidMeshesCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesCompoundSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3287.HypoidGearSetSteadyStateSynchronousResponseOnAShaft]':
        """List[HypoidGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft(self)
