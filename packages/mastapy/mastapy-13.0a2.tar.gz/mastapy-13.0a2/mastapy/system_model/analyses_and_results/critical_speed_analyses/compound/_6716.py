"""_6716.py

MountableComponentCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6587
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6664
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'MountableComponentCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentCompoundCriticalSpeedAnalysis',)


class MountableComponentCompoundCriticalSpeedAnalysis(_6664.ComponentCompoundCriticalSpeedAnalysis):
    """MountableComponentCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_MountableComponentCompoundCriticalSpeedAnalysis:
        """Special nested class for casting MountableComponentCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'MountableComponentCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def component_compound_critical_speed_analysis(self):
            return self._parent._cast(_6664.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6718
            
            return self._parent._cast(_6718.PartCompoundCriticalSpeedAnalysis)

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
        def agma_gleason_conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6643
            
            return self._parent._cast(_6643.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def bearing_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6647
            
            return self._parent._cast(_6647.BearingCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6650
            
            return self._parent._cast(_6650.BevelDifferentialGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6653
            
            return self._parent._cast(_6653.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6654
            
            return self._parent._cast(_6654.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6655
            
            return self._parent._cast(_6655.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def clutch_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6662
            
            return self._parent._cast(_6662.ClutchHalfCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6667
            
            return self._parent._cast(_6667.ConceptCouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6668
            
            return self._parent._cast(_6668.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6671
            
            return self._parent._cast(_6671.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def connector_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6675
            
            return self._parent._cast(_6675.ConnectorCompoundCriticalSpeedAnalysis)

        @property
        def coupling_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6678
            
            return self._parent._cast(_6678.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def cvt_pulley_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6681
            
            return self._parent._cast(_6681.CVTPulleyCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6686
            
            return self._parent._cast(_6686.CylindricalGearCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6689
            
            return self._parent._cast(_6689.CylindricalPlanetGearCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6692
            
            return self._parent._cast(_6692.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6697
            
            return self._parent._cast(_6697.GearCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6701
            
            return self._parent._cast(_6701.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6705
            
            return self._parent._cast(_6705.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6708
            
            return self._parent._cast(_6708.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6711
            
            return self._parent._cast(_6711.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def mass_disc_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6714
            
            return self._parent._cast(_6714.MassDiscCompoundCriticalSpeedAnalysis)

        @property
        def measurement_component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6715
            
            return self._parent._cast(_6715.MeasurementComponentCompoundCriticalSpeedAnalysis)

        @property
        def oil_seal_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6717
            
            return self._parent._cast(_6717.OilSealCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6721
            
            return self._parent._cast(_6721.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def planet_carrier_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6724
            
            return self._parent._cast(_6724.PlanetCarrierCompoundCriticalSpeedAnalysis)

        @property
        def point_load_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6725
            
            return self._parent._cast(_6725.PointLoadCompoundCriticalSpeedAnalysis)

        @property
        def power_load_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6726
            
            return self._parent._cast(_6726.PowerLoadCompoundCriticalSpeedAnalysis)

        @property
        def pulley_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6727
            
            return self._parent._cast(_6727.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def ring_pins_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6728
            
            return self._parent._cast(_6728.RingPinsCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6731
            
            return self._parent._cast(_6731.RollingRingCompoundCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6735
            
            return self._parent._cast(_6735.ShaftHubConnectionCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6738
            
            return self._parent._cast(_6738.SpiralBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6743
            
            return self._parent._cast(_6743.SpringDamperHalfCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6744
            
            return self._parent._cast(_6744.StraightBevelDiffGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6747
            
            return self._parent._cast(_6747.StraightBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6750
            
            return self._parent._cast(_6750.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6751
            
            return self._parent._cast(_6751.StraightBevelSunGearCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6753
            
            return self._parent._cast(_6753.SynchroniserHalfCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6754
            
            return self._parent._cast(_6754.SynchroniserPartCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6755
            
            return self._parent._cast(_6755.SynchroniserSleeveCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6758
            
            return self._parent._cast(_6758.TorqueConverterPumpCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6759
            
            return self._parent._cast(_6759.TorqueConverterTurbineCompoundCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6760
            
            return self._parent._cast(_6760.UnbalancedMassCompoundCriticalSpeedAnalysis)

        @property
        def virtual_component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6761
            
            return self._parent._cast(_6761.VirtualComponentCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6762
            
            return self._parent._cast(_6762.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6765
            
            return self._parent._cast(_6765.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(self) -> 'MountableComponentCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6587.MountableComponentCriticalSpeedAnalysis]':
        """List[MountableComponentCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6587.MountableComponentCriticalSpeedAnalysis]':
        """List[MountableComponentCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MountableComponentCompoundCriticalSpeedAnalysis._Cast_MountableComponentCompoundCriticalSpeedAnalysis':
        return self._Cast_MountableComponentCompoundCriticalSpeedAnalysis(self)
