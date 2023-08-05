"""_3252.py

ConceptCouplingSteadyStateSynchronousResponseOnAShaft
"""
from mastapy.system_model.part_model.couplings import _2560
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6804
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3263
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'ConceptCouplingSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingSteadyStateSynchronousResponseOnAShaft',)


class ConceptCouplingSteadyStateSynchronousResponseOnAShaft(_3263.CouplingSteadyStateSynchronousResponseOnAShaft):
    """ConceptCouplingSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConceptCouplingSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'ConceptCouplingSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3263.CouplingSteadyStateSynchronousResponseOnAShaft)

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
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(self) -> 'ConceptCouplingSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2560.ConceptCoupling':
        """ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6804.ConceptCouplingLoadCase':
        """ConceptCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft(self)
