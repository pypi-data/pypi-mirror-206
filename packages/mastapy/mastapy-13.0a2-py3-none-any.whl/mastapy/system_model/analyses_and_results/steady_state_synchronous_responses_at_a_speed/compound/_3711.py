"""_3711.py

SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3581
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3613
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed',)


class SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed(_3613.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed):
    """SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3613.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3692
            
            return self._parent._cast(_3692.PartCompoundSteadyStateSynchronousResponseAtASpeed)

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
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3619
            
            return self._parent._cast(_3619.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def belt_drive_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3623
            
            return self._parent._cast(_3623.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3626
            
            return self._parent._cast(_3626.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3631
            
            return self._parent._cast(_3631.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bolted_joint_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3633
            
            return self._parent._cast(_3633.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3634
            
            return self._parent._cast(_3634.ClutchCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3639
            
            return self._parent._cast(_3639.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3644
            
            return self._parent._cast(_3644.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3647
            
            return self._parent._cast(_3647.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3650
            
            return self._parent._cast(_3650.CouplingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3654
            
            return self._parent._cast(_3654.CVTCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3656
            
            return self._parent._cast(_3656.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3662
            
            return self._parent._cast(_3662.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def face_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3668
            
            return self._parent._cast(_3668.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3670
            
            return self._parent._cast(_3670.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3673
            
            return self._parent._cast(_3673.GearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3677
            
            return self._parent._cast(_3677.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3681
            
            return self._parent._cast(_3681.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3684
            
            return self._parent._cast(_3684.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3687
            
            return self._parent._cast(_3687.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3693
            
            return self._parent._cast(_3693.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3697
            
            return self._parent._cast(_3697.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3704
            
            return self._parent._cast(_3704.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3714
            
            return self._parent._cast(_3714.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3715
            
            return self._parent._cast(_3715.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3720
            
            return self._parent._cast(_3720.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3723
            
            return self._parent._cast(_3723.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3726
            
            return self._parent._cast(_3726.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3730
            
            return self._parent._cast(_3730.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3738
            
            return self._parent._cast(_3738.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3741
            
            return self._parent._cast(_3741.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(self) -> 'SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_3581.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed]':
        """List[SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3581.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed]':
        """List[SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed(self)
