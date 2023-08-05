"""_3690.py

MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3560
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3638
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed',)


class MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed(_3638.ComponentCompoundSteadyStateSynchronousResponseAtASpeed):
    """MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3638.ComponentCompoundSteadyStateSynchronousResponseAtASpeed)

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
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3617
            
            return self._parent._cast(_3617.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bearing_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3621
            
            return self._parent._cast(_3621.BearingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3624
            
            return self._parent._cast(_3624.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3627
            
            return self._parent._cast(_3627.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3628
            
            return self._parent._cast(_3628.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3629
            
            return self._parent._cast(_3629.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3636
            
            return self._parent._cast(_3636.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3641
            
            return self._parent._cast(_3641.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3642
            
            return self._parent._cast(_3642.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3645
            
            return self._parent._cast(_3645.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def connector_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3649
            
            return self._parent._cast(_3649.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3652
            
            return self._parent._cast(_3652.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3655
            
            return self._parent._cast(_3655.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3660
            
            return self._parent._cast(_3660.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3663
            
            return self._parent._cast(_3663.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def face_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3666
            
            return self._parent._cast(_3666.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3671
            
            return self._parent._cast(_3671.GearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3675
            
            return self._parent._cast(_3675.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3679
            
            return self._parent._cast(_3679.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3682
            
            return self._parent._cast(_3682.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3685
            
            return self._parent._cast(_3685.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def mass_disc_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3688
            
            return self._parent._cast(_3688.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def measurement_component_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3689
            
            return self._parent._cast(_3689.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def oil_seal_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3691
            
            return self._parent._cast(_3691.OilSealCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3695
            
            return self._parent._cast(_3695.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def planet_carrier_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3698
            
            return self._parent._cast(_3698.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def point_load_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3699
            
            return self._parent._cast(_3699.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def power_load_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3700
            
            return self._parent._cast(_3700.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3701
            
            return self._parent._cast(_3701.PulleyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def ring_pins_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3702
            
            return self._parent._cast(_3702.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3705
            
            return self._parent._cast(_3705.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3709
            
            return self._parent._cast(_3709.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3712
            
            return self._parent._cast(_3712.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3717
            
            return self._parent._cast(_3717.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3718
            
            return self._parent._cast(_3718.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3721
            
            return self._parent._cast(_3721.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3724
            
            return self._parent._cast(_3724.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3725
            
            return self._parent._cast(_3725.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3727
            
            return self._parent._cast(_3727.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3728
            
            return self._parent._cast(_3728.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3729
            
            return self._parent._cast(_3729.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3732
            
            return self._parent._cast(_3732.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3733
            
            return self._parent._cast(_3733.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3734
            
            return self._parent._cast(_3734.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3735
            
            return self._parent._cast(_3735.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def worm_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3736
            
            return self._parent._cast(_3736.WormGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3739
            
            return self._parent._cast(_3739.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(self) -> 'MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3560.MountableComponentSteadyStateSynchronousResponseAtASpeed]':
        """List[MountableComponentSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3560.MountableComponentSteadyStateSynchronousResponseAtASpeed]':
        """List[MountableComponentSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed(self)
