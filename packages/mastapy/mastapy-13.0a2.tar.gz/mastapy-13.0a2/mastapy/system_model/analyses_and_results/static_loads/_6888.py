"""_6888.py

MountableComponentLoadCase
"""
from mastapy.system_model.part_model import _2444
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6801
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'MountableComponentLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentLoadCase',)


class MountableComponentLoadCase(_6801.ComponentLoadCase):
    """MountableComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_LOAD_CASE

    class _Cast_MountableComponentLoadCase:
        """Special nested class for casting MountableComponentLoadCase to subclasses."""

        def __init__(self, parent: 'MountableComponentLoadCase'):
            self._parent = parent

        @property
        def component_load_case(self):
            return self._parent._cast(_6801.ComponentLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.PartLoadCase)

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
        def agma_gleason_conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6778
            
            return self._parent._cast(_6778.AGMAGleasonConicalGearLoadCase)

        @property
        def bearing_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6784
            
            return self._parent._cast(_6784.BearingLoadCase)

        @property
        def bevel_differential_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6787
            
            return self._parent._cast(_6787.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6790
            
            return self._parent._cast(_6790.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6791
            
            return self._parent._cast(_6791.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6792
            
            return self._parent._cast(_6792.BevelGearLoadCase)

        @property
        def clutch_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6798
            
            return self._parent._cast(_6798.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6803
            
            return self._parent._cast(_6803.ConceptCouplingHalfLoadCase)

        @property
        def concept_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6805
            
            return self._parent._cast(_6805.ConceptGearLoadCase)

        @property
        def conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6808
            
            return self._parent._cast(_6808.ConicalGearLoadCase)

        @property
        def connector_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6814
            
            return self._parent._cast(_6814.ConnectorLoadCase)

        @property
        def coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6816
            
            return self._parent._cast(_6816.CouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6820
            
            return self._parent._cast(_6820.CVTPulleyLoadCase)

        @property
        def cylindrical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6825
            
            return self._parent._cast(_6825.CylindricalGearLoadCase)

        @property
        def cylindrical_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6830
            
            return self._parent._cast(_6830.CylindricalPlanetGearLoadCase)

        @property
        def face_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6848
            
            return self._parent._cast(_6848.FaceGearLoadCase)

        @property
        def gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6854
            
            return self._parent._cast(_6854.GearLoadCase)

        @property
        def hypoid_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6869
            
            return self._parent._cast(_6869.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6876
            
            return self._parent._cast(_6876.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6879
            
            return self._parent._cast(_6879.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6882
            
            return self._parent._cast(_6882.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        @property
        def mass_disc_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6885
            
            return self._parent._cast(_6885.MassDiscLoadCase)

        @property
        def measurement_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6886
            
            return self._parent._cast(_6886.MeasurementComponentLoadCase)

        @property
        def oil_seal_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6890
            
            return self._parent._cast(_6890.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6894
            
            return self._parent._cast(_6894.PartToPartShearCouplingHalfLoadCase)

        @property
        def planet_carrier_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6899
            
            return self._parent._cast(_6899.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6902
            
            return self._parent._cast(_6902.PointLoadLoadCase)

        @property
        def power_load_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6903
            
            return self._parent._cast(_6903.PowerLoadLoadCase)

        @property
        def pulley_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6904
            
            return self._parent._cast(_6904.PulleyLoadCase)

        @property
        def ring_pins_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6907
            
            return self._parent._cast(_6907.RingPinsLoadCase)

        @property
        def rolling_ring_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6911
            
            return self._parent._cast(_6911.RollingRingLoadCase)

        @property
        def shaft_hub_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6913
            
            return self._parent._cast(_6913.ShaftHubConnectionLoadCase)

        @property
        def spiral_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6917
            
            return self._parent._cast(_6917.SpiralBevelGearLoadCase)

        @property
        def spring_damper_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6921
            
            return self._parent._cast(_6921.SpringDamperHalfLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6923
            
            return self._parent._cast(_6923.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6926
            
            return self._parent._cast(_6926.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6929
            
            return self._parent._cast(_6929.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6930
            
            return self._parent._cast(_6930.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6931
            
            return self._parent._cast(_6931.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6933
            
            return self._parent._cast(_6933.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6934
            
            return self._parent._cast(_6934.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6938
            
            return self._parent._cast(_6938.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6939
            
            return self._parent._cast(_6939.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6944
            
            return self._parent._cast(_6944.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6945
            
            return self._parent._cast(_6945.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6946
            
            return self._parent._cast(_6946.WormGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6949
            
            return self._parent._cast(_6949.ZerolBevelGearLoadCase)

        @property
        def mountable_component_load_case(self) -> 'MountableComponentLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2444.MountableComponent':
        """MountableComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MountableComponentLoadCase._Cast_MountableComponentLoadCase':
        return self._Cast_MountableComponentLoadCase(self)
