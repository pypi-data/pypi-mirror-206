"""_6892.py

PartLoadCase
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy.system_model.analyses_and_results.static_loads import _6861, _6769, _6770
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model import _2448
from mastapy.electric_machines.harmonic_load_data import _1368
from mastapy.system_model.analyses_and_results import _2636
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PartLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('PartLoadCase',)


class PartLoadCase(_2636.PartAnalysis):
    """PartLoadCase

    This is a mastapy class.
    """

    TYPE = _PART_LOAD_CASE

    class _Cast_PartLoadCase:
        """Special nested class for casting PartLoadCase to subclasses."""

        def __init__(self, parent: 'PartLoadCase'):
            self._parent = parent

        @property
        def part_analysis(self):
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
        def abstract_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6771
            
            return self._parent._cast(_6771.AbstractAssemblyLoadCase)

        @property
        def abstract_shaft_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6772
            
            return self._parent._cast(_6772.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6773
            
            return self._parent._cast(_6773.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6778
            
            return self._parent._cast(_6778.AGMAGleasonConicalGearLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6780
            
            return self._parent._cast(_6780.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6783
            
            return self._parent._cast(_6783.AssemblyLoadCase)

        @property
        def bearing_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6784
            
            return self._parent._cast(_6784.BearingLoadCase)

        @property
        def belt_drive_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6786
            
            return self._parent._cast(_6786.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6787
            
            return self._parent._cast(_6787.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6789
            
            return self._parent._cast(_6789.BevelDifferentialGearSetLoadCase)

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
        def bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6794
            
            return self._parent._cast(_6794.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6795
            
            return self._parent._cast(_6795.BoltedJointLoadCase)

        @property
        def bolt_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6796
            
            return self._parent._cast(_6796.BoltLoadCase)

        @property
        def clutch_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6798
            
            return self._parent._cast(_6798.ClutchHalfLoadCase)

        @property
        def clutch_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6799
            
            return self._parent._cast(_6799.ClutchLoadCase)

        @property
        def component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6801
            
            return self._parent._cast(_6801.ComponentLoadCase)

        @property
        def concept_coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6803
            
            return self._parent._cast(_6803.ConceptCouplingHalfLoadCase)

        @property
        def concept_coupling_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6804
            
            return self._parent._cast(_6804.ConceptCouplingLoadCase)

        @property
        def concept_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6805
            
            return self._parent._cast(_6805.ConceptGearLoadCase)

        @property
        def concept_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6807
            
            return self._parent._cast(_6807.ConceptGearSetLoadCase)

        @property
        def conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6808
            
            return self._parent._cast(_6808.ConicalGearLoadCase)

        @property
        def conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6812
            
            return self._parent._cast(_6812.ConicalGearSetLoadCase)

        @property
        def connector_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6814
            
            return self._parent._cast(_6814.ConnectorLoadCase)

        @property
        def coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6816
            
            return self._parent._cast(_6816.CouplingHalfLoadCase)

        @property
        def coupling_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6817
            
            return self._parent._cast(_6817.CouplingLoadCase)

        @property
        def cvt_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6819
            
            return self._parent._cast(_6819.CVTLoadCase)

        @property
        def cvt_pulley_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6820
            
            return self._parent._cast(_6820.CVTPulleyLoadCase)

        @property
        def cycloidal_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6821
            
            return self._parent._cast(_6821.CycloidalAssemblyLoadCase)

        @property
        def cycloidal_disc_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6823
            
            return self._parent._cast(_6823.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6825
            
            return self._parent._cast(_6825.CylindricalGearLoadCase)

        @property
        def cylindrical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6829
            
            return self._parent._cast(_6829.CylindricalGearSetLoadCase)

        @property
        def cylindrical_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6830
            
            return self._parent._cast(_6830.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6833
            
            return self._parent._cast(_6833.DatumLoadCase)

        @property
        def external_cad_model_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6847
            
            return self._parent._cast(_6847.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6848
            
            return self._parent._cast(_6848.FaceGearLoadCase)

        @property
        def face_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6850
            
            return self._parent._cast(_6850.FaceGearSetLoadCase)

        @property
        def fe_part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6851
            
            return self._parent._cast(_6851.FEPartLoadCase)

        @property
        def flexible_pin_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6852
            
            return self._parent._cast(_6852.FlexiblePinAssemblyLoadCase)

        @property
        def gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6854
            
            return self._parent._cast(_6854.GearLoadCase)

        @property
        def gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6859
            
            return self._parent._cast(_6859.GearSetLoadCase)

        @property
        def guide_dxf_model_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6860
            
            return self._parent._cast(_6860.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6869
            
            return self._parent._cast(_6869.HypoidGearLoadCase)

        @property
        def hypoid_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6871
            
            return self._parent._cast(_6871.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6876
            
            return self._parent._cast(_6876.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6878
            
            return self._parent._cast(_6878.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6879
            
            return self._parent._cast(_6879.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6881
            
            return self._parent._cast(_6881.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6882
            
            return self._parent._cast(_6882.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6884
            
            return self._parent._cast(_6884.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        @property
        def mass_disc_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6885
            
            return self._parent._cast(_6885.MassDiscLoadCase)

        @property
        def measurement_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6886
            
            return self._parent._cast(_6886.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6888
            
            return self._parent._cast(_6888.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6890
            
            return self._parent._cast(_6890.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6894
            
            return self._parent._cast(_6894.PartToPartShearCouplingHalfLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6895
            
            return self._parent._cast(_6895.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6897
            
            return self._parent._cast(_6897.PlanetaryGearSetLoadCase)

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
        def rolling_ring_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6909
            
            return self._parent._cast(_6909.RollingRingAssemblyLoadCase)

        @property
        def rolling_ring_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6911
            
            return self._parent._cast(_6911.RollingRingLoadCase)

        @property
        def root_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6912
            
            return self._parent._cast(_6912.RootAssemblyLoadCase)

        @property
        def shaft_hub_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6913
            
            return self._parent._cast(_6913.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6914
            
            return self._parent._cast(_6914.ShaftLoadCase)

        @property
        def specialised_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6916
            
            return self._parent._cast(_6916.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6917
            
            return self._parent._cast(_6917.SpiralBevelGearLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6919
            
            return self._parent._cast(_6919.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6921
            
            return self._parent._cast(_6921.SpringDamperHalfLoadCase)

        @property
        def spring_damper_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6922
            
            return self._parent._cast(_6922.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6923
            
            return self._parent._cast(_6923.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6925
            
            return self._parent._cast(_6925.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6926
            
            return self._parent._cast(_6926.StraightBevelGearLoadCase)

        @property
        def straight_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6928
            
            return self._parent._cast(_6928.StraightBevelGearSetLoadCase)

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
        def synchroniser_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6932
            
            return self._parent._cast(_6932.SynchroniserLoadCase)

        @property
        def synchroniser_part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6933
            
            return self._parent._cast(_6933.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6934
            
            return self._parent._cast(_6934.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6937
            
            return self._parent._cast(_6937.TorqueConverterLoadCase)

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
        def worm_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6948
            
            return self._parent._cast(_6948.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6949
            
            return self._parent._cast(_6949.ZerolBevelGearLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6951
            
            return self._parent._cast(_6951.ZerolBevelGearSetLoadCase)

        @property
        def part_load_case(self) -> 'PartLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_data_is_up_to_date(self) -> 'bool':
        """bool: 'ExcitationDataIsUpToDate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationDataIsUpToDate

        if temp is None:
            return False

        return temp

    @property
    def harmonic_excitation_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType':
        """enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType: 'HarmonicExcitationType' is the original name of this property."""

        temp = self.wrapped.HarmonicExcitationType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @harmonic_excitation_type.setter
    def harmonic_excitation_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.HarmonicExcitationType = value

    @property
    def load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up(self) -> 'list_with_selected_item.ListWithSelectedItem_StaticLoadCase':
        """list_with_selected_item.ListWithSelectedItem_StaticLoadCase: 'LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp' is the original name of this property."""

        temp = self.wrapped.LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_StaticLoadCase)(temp) if temp is not None else None

    @load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up.setter
    def load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up(self, value: 'list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp = value

    @property
    def use_this_load_case_for_advanced_system_deflection_current_load_case_set_up(self) -> 'bool':
        """bool: 'UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp' is the original name of this property."""

        temp = self.wrapped.UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp

        if temp is None:
            return False

        return temp

    @use_this_load_case_for_advanced_system_deflection_current_load_case_set_up.setter
    def use_this_load_case_for_advanced_system_deflection_current_load_case_set_up(self, value: 'bool'):
        self.wrapped.UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp = bool(value) if value else False

    @property
    def component_design(self) -> '_2448.Part':
        """Part: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def static_load_case(self) -> '_6769.StaticLoadCase':
        """StaticLoadCase: 'StaticLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def time_series_load_case(self) -> '_6770.TimeSeriesLoadCase':
        """TimeSeriesLoadCase: 'TimeSeriesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeSeriesLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def clear_user_specified_excitation_data_for_this_load_case(self):
        """ 'ClearUserSpecifiedExcitationDataForThisLoadCase' is the original name of this method."""

        self.wrapped.ClearUserSpecifiedExcitationDataForThisLoadCase()

    def get_harmonic_load_data_for_import(self) -> '_1368.HarmonicLoadDataBase':
        """ 'GetHarmonicLoadDataForImport' is the original name of this method.

        Returns:
            mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataBase
        """

        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'PartLoadCase._Cast_PartLoadCase':
        return self._Cast_PartLoadCase(self)
