"""_5576.py

MountableComponentCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5435
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5524
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'MountableComponentCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentCompoundMultibodyDynamicsAnalysis',)


class MountableComponentCompoundMultibodyDynamicsAnalysis(_5524.ComponentCompoundMultibodyDynamicsAnalysis):
    """MountableComponentCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_MountableComponentCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting MountableComponentCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'MountableComponentCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def component_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5524.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5578
            
            return self._parent._cast(_5578.PartCompoundMultibodyDynamicsAnalysis)

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
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5503
            
            return self._parent._cast(_5503.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bearing_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5507
            
            return self._parent._cast(_5507.BearingCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5510
            
            return self._parent._cast(_5510.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5513
            
            return self._parent._cast(_5513.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5514
            
            return self._parent._cast(_5514.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5515
            
            return self._parent._cast(_5515.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5522
            
            return self._parent._cast(_5522.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5527
            
            return self._parent._cast(_5527.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5528
            
            return self._parent._cast(_5528.ConceptGearCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5531
            
            return self._parent._cast(_5531.ConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def connector_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5535
            
            return self._parent._cast(_5535.ConnectorCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5538
            
            return self._parent._cast(_5538.CouplingHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5541
            
            return self._parent._cast(_5541.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5546
            
            return self._parent._cast(_5546.CylindricalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5549
            
            return self._parent._cast(_5549.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5552
            
            return self._parent._cast(_5552.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5557
            
            return self._parent._cast(_5557.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5561
            
            return self._parent._cast(_5561.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5565
            
            return self._parent._cast(_5565.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5568
            
            return self._parent._cast(_5568.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5571
            
            return self._parent._cast(_5571.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def mass_disc_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5574
            
            return self._parent._cast(_5574.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5575
            
            return self._parent._cast(_5575.MeasurementComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def oil_seal_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5577
            
            return self._parent._cast(_5577.OilSealCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5581
            
            return self._parent._cast(_5581.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def planet_carrier_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5584
            
            return self._parent._cast(_5584.PlanetCarrierCompoundMultibodyDynamicsAnalysis)

        @property
        def point_load_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5585
            
            return self._parent._cast(_5585.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5586
            
            return self._parent._cast(_5586.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5587
            
            return self._parent._cast(_5587.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5588
            
            return self._parent._cast(_5588.RingPinsCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5591
            
            return self._parent._cast(_5591.RollingRingCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5595
            
            return self._parent._cast(_5595.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5598
            
            return self._parent._cast(_5598.SpiralBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5603
            
            return self._parent._cast(_5603.SpringDamperHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5604
            
            return self._parent._cast(_5604.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5607
            
            return self._parent._cast(_5607.StraightBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5610
            
            return self._parent._cast(_5610.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5611
            
            return self._parent._cast(_5611.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis)

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5613
            
            return self._parent._cast(_5613.SynchroniserHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5614
            
            return self._parent._cast(_5614.SynchroniserPartCompoundMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5615
            
            return self._parent._cast(_5615.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5618
            
            return self._parent._cast(_5618.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5619
            
            return self._parent._cast(_5619.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis)

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5620
            
            return self._parent._cast(_5620.UnbalancedMassCompoundMultibodyDynamicsAnalysis)

        @property
        def virtual_component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5621
            
            return self._parent._cast(_5621.VirtualComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5622
            
            return self._parent._cast(_5622.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5625
            
            return self._parent._cast(_5625.ZerolBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(self) -> 'MountableComponentCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5435.MountableComponentMultibodyDynamicsAnalysis]':
        """List[MountableComponentMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5435.MountableComponentMultibodyDynamicsAnalysis]':
        """List[MountableComponentMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis':
        return self._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis(self)
