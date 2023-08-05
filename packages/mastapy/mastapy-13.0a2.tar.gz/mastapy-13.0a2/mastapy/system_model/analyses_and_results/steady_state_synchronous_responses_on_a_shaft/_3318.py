"""_3318.py

RootAssemblySteadyStateSynchronousResponseOnAShaft
"""
from mastapy.system_model.part_model import _2454
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3329, _3231
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'RootAssemblySteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblySteadyStateSynchronousResponseOnAShaft',)


class RootAssemblySteadyStateSynchronousResponseOnAShaft(_3231.AssemblySteadyStateSynchronousResponseOnAShaft):
    """RootAssemblySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting RootAssemblySteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'RootAssemblySteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def assembly_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3231.AssemblySteadyStateSynchronousResponseOnAShaft)

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
        def root_assembly_steady_state_synchronous_response_on_a_shaft(self) -> 'RootAssemblySteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblySteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2454.RootAssembly':
        """RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def steady_state_synchronous_response_on_a_shaft_inputs(self) -> '_3329.SteadyStateSynchronousResponseOnAShaft':
        """SteadyStateSynchronousResponseOnAShaft: 'SteadyStateSynchronousResponseOnAShaftInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateSynchronousResponseOnAShaftInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft':
        return self._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft(self)
