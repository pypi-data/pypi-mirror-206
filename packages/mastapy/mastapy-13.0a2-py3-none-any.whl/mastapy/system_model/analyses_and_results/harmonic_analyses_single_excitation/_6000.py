"""_6000.py

ComponentHarmonicAnalysisOfSingleExcitation
"""
from mastapy.system_model.part_model import _2424
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6055
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'ComponentHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentHarmonicAnalysisOfSingleExcitation',)


class ComponentHarmonicAnalysisOfSingleExcitation(_6055.PartHarmonicAnalysisOfSingleExcitation):
    """ComponentHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_ComponentHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ComponentHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'ComponentHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def part_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6055.PartHarmonicAnalysisOfSingleExcitation)

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
        def abstract_shaft_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5976
            
            return self._parent._cast(_5976.AbstractShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5977
            
            return self._parent._cast(_5977.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5979
            
            return self._parent._cast(_5979.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bearing_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5983
            
            return self._parent._cast(_5983.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5986
            
            return self._parent._cast(_5986.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5989
            
            return self._parent._cast(_5989.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5990
            
            return self._parent._cast(_5990.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5991
            
            return self._parent._cast(_5991.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bolt_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5995
            
            return self._parent._cast(_5995.BoltHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5997
            
            return self._parent._cast(_5997.ClutchHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6002
            
            return self._parent._cast(_6002.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6004
            
            return self._parent._cast(_6004.ConceptGearHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6007
            
            return self._parent._cast(_6007.ConicalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def connector_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6011
            
            return self._parent._cast(_6011.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6013
            
            return self._parent._cast(_6013.CouplingHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6017
            
            return self._parent._cast(_6017.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6020
            
            return self._parent._cast(_6020.CycloidalDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6022
            
            return self._parent._cast(_6022.CylindricalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6025
            
            return self._parent._cast(_6025.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation)

        @property
        def datum_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6026
            
            return self._parent._cast(_6026.DatumHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6027
            
            return self._parent._cast(_6027.ExternalCADModelHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6028
            
            return self._parent._cast(_6028.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def fe_part_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6031
            
            return self._parent._cast(_6031.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6033
            
            return self._parent._cast(_6033.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6036
            
            return self._parent._cast(_6036.GuideDxfModelHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6038
            
            return self._parent._cast(_6038.HypoidGearHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6042
            
            return self._parent._cast(_6042.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6045
            
            return self._parent._cast(_6045.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6048
            
            return self._parent._cast(_6048.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6051
            
            return self._parent._cast(_6051.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6052
            
            return self._parent._cast(_6052.MeasurementComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6053
            
            return self._parent._cast(_6053.MountableComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6054
            
            return self._parent._cast(_6054.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6057
            
            return self._parent._cast(_6057.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6061
            
            return self._parent._cast(_6061.PlanetCarrierHarmonicAnalysisOfSingleExcitation)

        @property
        def point_load_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6062
            
            return self._parent._cast(_6062.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6063
            
            return self._parent._cast(_6063.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6064
            
            return self._parent._cast(_6064.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6065
            
            return self._parent._cast(_6065.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6069
            
            return self._parent._cast(_6069.RollingRingHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6071
            
            return self._parent._cast(_6071.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6072
            
            return self._parent._cast(_6072.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6075
            
            return self._parent._cast(_6075.SpiralBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6079
            
            return self._parent._cast(_6079.SpringDamperHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6081
            
            return self._parent._cast(_6081.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6084
            
            return self._parent._cast(_6084.StraightBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6087
            
            return self._parent._cast(_6087.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6088
            
            return self._parent._cast(_6088.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6089
            
            return self._parent._cast(_6089.SynchroniserHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6091
            
            return self._parent._cast(_6091.SynchroniserPartHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6092
            
            return self._parent._cast(_6092.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6095
            
            return self._parent._cast(_6095.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6096
            
            return self._parent._cast(_6096.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation)

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6097
            
            return self._parent._cast(_6097.UnbalancedMassHarmonicAnalysisOfSingleExcitation)

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6098
            
            return self._parent._cast(_6098.VirtualComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6099
            
            return self._parent._cast(_6099.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6102
            
            return self._parent._cast(_6102.ZerolBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def component_harmonic_analysis_of_single_excitation(self) -> 'ComponentHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2424.Component':
        """Component: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation':
        return self._Cast_ComponentHarmonicAnalysisOfSingleExcitation(self)
