"""_3285.py

GuideDxfModelSteadyStateSynchronousResponseOnAShaft
"""
from mastapy.system_model.part_model import _2435
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6860
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3249
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'GuideDxfModelSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelSteadyStateSynchronousResponseOnAShaft',)


class GuideDxfModelSteadyStateSynchronousResponseOnAShaft(_3249.ComponentSteadyStateSynchronousResponseOnAShaft):
    """GuideDxfModelSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_GuideDxfModelSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting GuideDxfModelSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'GuideDxfModelSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3249.ComponentSteadyStateSynchronousResponseOnAShaft)

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
        def guide_dxf_model_steady_state_synchronous_response_on_a_shaft(self) -> 'GuideDxfModelSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GuideDxfModelSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2435.GuideDxfModel':
        """GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6860.GuideDxfModelLoadCase':
        """GuideDxfModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GuideDxfModelSteadyStateSynchronousResponseOnAShaft._Cast_GuideDxfModelSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_GuideDxfModelSteadyStateSynchronousResponseOnAShaft(self)
