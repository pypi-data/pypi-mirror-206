"""_5675.py

ComponentHarmonicAnalysis
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2424
from mastapy.system_model.analyses_and_results.modal_analyses import _4572
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5832
from mastapy.system_model.analyses_and_results.system_deflections import _2694
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5755
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ComponentHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentHarmonicAnalysis',)


class ComponentHarmonicAnalysis(_5755.PartHarmonicAnalysis):
    """ComponentHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_HARMONIC_ANALYSIS

    class _Cast_ComponentHarmonicAnalysis:
        """Special nested class for casting ComponentHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'ComponentHarmonicAnalysis'):
            self._parent = parent

        @property
        def part_harmonic_analysis(self):
            return self._parent._cast(_5755.PartHarmonicAnalysis)

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
        def abstract_shaft_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5650
            
            return self._parent._cast(_5650.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5651
            
            return self._parent._cast(_5651.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5653
            
            return self._parent._cast(_5653.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5657
            
            return self._parent._cast(_5657.BearingHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5660
            
            return self._parent._cast(_5660.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5663
            
            return self._parent._cast(_5663.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5664
            
            return self._parent._cast(_5664.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5665
            
            return self._parent._cast(_5665.BevelGearHarmonicAnalysis)

        @property
        def bolt_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5669
            
            return self._parent._cast(_5669.BoltHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5671
            
            return self._parent._cast(_5671.ClutchHalfHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5677
            
            return self._parent._cast(_5677.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5679
            
            return self._parent._cast(_5679.ConceptGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5682
            
            return self._parent._cast(_5682.ConicalGearHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5686
            
            return self._parent._cast(_5686.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5688
            
            return self._parent._cast(_5688.CouplingHalfHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5692
            
            return self._parent._cast(_5692.CVTPulleyHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5695
            
            return self._parent._cast(_5695.CycloidalDiscHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5697
            
            return self._parent._cast(_5697.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5700
            
            return self._parent._cast(_5700.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def datum_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5701
            
            return self._parent._cast(_5701.DatumHarmonicAnalysis)

        @property
        def external_cad_model_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5715
            
            return self._parent._cast(_5715.ExternalCADModelHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5716
            
            return self._parent._cast(_5716.FaceGearHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5719
            
            return self._parent._cast(_5719.FEPartHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5722
            
            return self._parent._cast(_5722.GearHarmonicAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5729
            
            return self._parent._cast(_5729.GuideDxfModelHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5738
            
            return self._parent._cast(_5738.HypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5742
            
            return self._parent._cast(_5742.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5745
            
            return self._parent._cast(_5745.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5748
            
            return self._parent._cast(_5748.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis)

        @property
        def mass_disc_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5751
            
            return self._parent._cast(_5751.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5752
            
            return self._parent._cast(_5752.MeasurementComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5753
            
            return self._parent._cast(_5753.MountableComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5754
            
            return self._parent._cast(_5754.OilSealHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5757
            
            return self._parent._cast(_5757.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5762
            
            return self._parent._cast(_5762.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5763
            
            return self._parent._cast(_5763.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5764
            
            return self._parent._cast(_5764.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5765
            
            return self._parent._cast(_5765.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5767
            
            return self._parent._cast(_5767.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5771
            
            return self._parent._cast(_5771.RollingRingHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5773
            
            return self._parent._cast(_5773.ShaftHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5774
            
            return self._parent._cast(_5774.ShaftHubConnectionHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5779
            
            return self._parent._cast(_5779.SpiralBevelGearHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5783
            
            return self._parent._cast(_5783.SpringDamperHalfHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5786
            
            return self._parent._cast(_5786.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5789
            
            return self._parent._cast(_5789.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5792
            
            return self._parent._cast(_5792.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5793
            
            return self._parent._cast(_5793.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5794
            
            return self._parent._cast(_5794.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5796
            
            return self._parent._cast(_5796.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5797
            
            return self._parent._cast(_5797.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5800
            
            return self._parent._cast(_5800.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5801
            
            return self._parent._cast(_5801.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5803
            
            return self._parent._cast(_5803.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5804
            
            return self._parent._cast(_5804.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5805
            
            return self._parent._cast(_5805.WormGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5808
            
            return self._parent._cast(_5808.ZerolBevelGearHarmonicAnalysis)

        @property
        def component_harmonic_analysis(self) -> 'ComponentHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

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
    def coupled_modal_analysis(self) -> '_4572.ComponentModalAnalysis':
        """ComponentModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results(self) -> '_5832.HarmonicAnalysisResultsPropertyAccessor':
        """HarmonicAnalysisResultsPropertyAccessor: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2694.ComponentSystemDeflection':
        """ComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis':
        return self._Cast_ComponentHarmonicAnalysis(self)
