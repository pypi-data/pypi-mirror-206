"""_3583.py

SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.part_model.gears import _2523
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6919
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3584, _3582, _3500
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed',)


class SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed(_3500.BevelGearSetSteadyStateSynchronousResponseAtASpeed):
    """SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3500.BevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3488
            
            return self._parent._cast(_3488.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3516
            
            return self._parent._cast(_3516.ConicalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3542
            
            return self._parent._cast(_3542.GearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3581
            
            return self._parent._cast(_3581.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3483
            
            return self._parent._cast(_3483.AbstractAssemblySteadyStateSynchronousResponseAtASpeed)

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
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self) -> 'SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2523.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6919.SpiralBevelGearSetLoadCase':
        """SpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spiral_bevel_gears_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3584.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed]':
        """List[SpiralBevelGearSteadyStateSynchronousResponseAtASpeed]: 'SpiralBevelGearsSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearsSteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_meshes_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3582.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed]':
        """List[SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed]: 'SpiralBevelMeshesSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelMeshesSteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed(self)
