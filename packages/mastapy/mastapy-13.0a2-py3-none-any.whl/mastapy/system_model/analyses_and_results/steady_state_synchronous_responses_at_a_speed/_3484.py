"""_3484.py

AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
"""
from mastapy.system_model.part_model import _2416
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed',)


class AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed(_3508.ComponentSteadyStateSynchronousResponseAtASpeed):
    """AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3508.ComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3562
            
            return self._parent._cast(_3562.PartSteadyStateSynchronousResponseAtASpeed)

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
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3485
            
            return self._parent._cast(_3485.AbstractShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3529
            
            return self._parent._cast(_3529.CycloidalDiscSteadyStateSynchronousResponseAtASpeed)

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3539
            
            return self._parent._cast(_3539.FEPartSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3579
            
            return self._parent._cast(_3579.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(self) -> 'AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2416.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed(self)
