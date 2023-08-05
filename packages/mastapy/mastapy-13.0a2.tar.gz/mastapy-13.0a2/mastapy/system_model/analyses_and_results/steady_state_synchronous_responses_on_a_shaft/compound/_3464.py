"""_3464.py

StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.part_model.gears import _2527
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3334
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3462, _3463, _3372
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft',)


class StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft(_3372.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft):
    """StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3372.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3360
            
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
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2527.StraightBevelGearSet':
        """StraightBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2527.StraightBevelGearSet':
        """StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3334.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft]':
        """List[StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gears_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3462.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft]: 'StraightBevelGearsCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsCompoundSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3463.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]: 'StraightBevelMeshesCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesCompoundSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3334.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft]':
        """List[StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft(self)
