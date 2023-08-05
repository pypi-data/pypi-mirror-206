"""_3254.py

ConceptGearSetSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.part_model.gears import _2501
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6807
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3255, _3253, _3283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'ConceptGearSetSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetSteadyStateSynchronousResponseOnAShaft',)


class ConceptGearSetSteadyStateSynchronousResponseOnAShaft(_3283.GearSetSteadyStateSynchronousResponseOnAShaft):
    """ConceptGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_ConceptGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConceptGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'ConceptGearSetSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3283.GearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3322
            
            return self._parent._cast(_3322.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3224
            
            return self._parent._cast(_3224.AbstractAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def part_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3303
            
            return self._parent._cast(_3303.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(self) -> 'ConceptGearSetSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearSetSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self) -> '_6807.ConceptGearSetLoadCase':
        """ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gears_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3255.ConceptGearSteadyStateSynchronousResponseOnAShaft]':
        """List[ConceptGearSteadyStateSynchronousResponseOnAShaft]: 'ConceptGearsSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3253.ConceptGearMeshSteadyStateSynchronousResponseOnAShaft]':
        """List[ConceptGearMeshSteadyStateSynchronousResponseOnAShaft]: 'ConceptMeshesSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearSetSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_ConceptGearSetSteadyStateSynchronousResponseOnAShaft(self)
