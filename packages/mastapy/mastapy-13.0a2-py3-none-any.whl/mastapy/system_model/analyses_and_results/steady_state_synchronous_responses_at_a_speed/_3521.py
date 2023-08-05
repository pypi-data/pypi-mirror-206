"""_3521.py

CouplingHalfSteadyStateSynchronousResponseAtASpeed
"""
from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3560
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'CouplingHalfSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfSteadyStateSynchronousResponseAtASpeed',)


class CouplingHalfSteadyStateSynchronousResponseAtASpeed(_3560.MountableComponentSteadyStateSynchronousResponseAtASpeed):
    """CouplingHalfSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_CouplingHalfSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CouplingHalfSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'CouplingHalfSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3560.MountableComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3508
            
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
        def clutch_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3505
            
            return self._parent._cast(_3505.ClutchHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3510
            
            return self._parent._cast(_3510.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3524
            
            return self._parent._cast(_3524.CVTPulleySteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3564
            
            return self._parent._cast(_3564.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3571
            
            return self._parent._cast(_3571.PulleySteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3576
            
            return self._parent._cast(_3576.RollingRingSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3586
            
            return self._parent._cast(_3586.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3597
            
            return self._parent._cast(_3597.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3598
            
            return self._parent._cast(_3598.SynchroniserPartSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3599
            
            return self._parent._cast(_3599.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3602
            
            return self._parent._cast(_3602.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3604
            
            return self._parent._cast(_3604.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(self) -> 'CouplingHalfSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2563.CouplingHalf':
        """CouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_CouplingHalfSteadyStateSynchronousResponseAtASpeed(self)
