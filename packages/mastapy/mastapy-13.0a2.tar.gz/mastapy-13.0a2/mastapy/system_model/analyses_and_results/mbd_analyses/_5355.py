"""_5355.py

AssemblyMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2413
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6783
from mastapy.system_model.analyses_and_results.mbd_analyses import (
    _5356, _5359, _5362, _5368,
    _5369, _5391, _5372, _5378,
    _5381, _5420, _5393, _5395,
    _5399, _5406, _5405, _5407,
    _5411, _5415, _5426, _5429,
    _5430, _5434, _5436, _5440,
    _5443, _5444, _5445, _5447,
    _5449, _5455, _5456, _5349,
    _5462, _5465, _5468, _5471,
    _5475, _5480, _5484, _5489,
    _5492, _5347
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'AssemblyMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyMultibodyDynamicsAnalysis',)


class AssemblyMultibodyDynamicsAnalysis(_5347.AbstractAssemblyMultibodyDynamicsAnalysis):
    """AssemblyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_AssemblyMultibodyDynamicsAnalysis:
        """Special nested class for casting AssemblyMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'AssemblyMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def abstract_assembly_multibody_dynamics_analysis(self):
            return self._parent._cast(_5347.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437
            
            return self._parent._cast(_5437.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartTimeSeriesLoadAnalysisCase)

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
        def root_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452
            
            return self._parent._cast(_5452.RootAssemblyMultibodyDynamicsAnalysis)

        @property
        def assembly_multibody_dynamics_analysis(self) -> 'AssemblyMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AssemblyMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2413.Assembly':
        """Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6783.AssemblyLoadCase':
        """AssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearings(self) -> 'List[_5356.BearingMultibodyDynamicsAnalysis]':
        """List[BearingMultibodyDynamicsAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def belt_drives(self) -> 'List[_5359.BeltDriveMultibodyDynamicsAnalysis]':
        """List[BeltDriveMultibodyDynamicsAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltDrives

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5362.BevelDifferentialGearSetMultibodyDynamicsAnalysis]':
        """List[BevelDifferentialGearSetMultibodyDynamicsAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolted_joints(self) -> 'List[_5368.BoltedJointMultibodyDynamicsAnalysis]':
        """List[BoltedJointMultibodyDynamicsAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolts(self) -> 'List[_5369.BoltMultibodyDynamicsAnalysis]':
        """List[BoltMultibodyDynamicsAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cv_ts(self) -> 'List[_5391.CVTMultibodyDynamicsAnalysis]':
        """List[CVTMultibodyDynamicsAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CVTs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def clutches(self) -> 'List[_5372.ClutchMultibodyDynamicsAnalysis]':
        """List[ClutchMultibodyDynamicsAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Clutches

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_couplings(self) -> 'List[_5378.ConceptCouplingMultibodyDynamicsAnalysis]':
        """List[ConceptCouplingMultibodyDynamicsAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5381.ConceptGearSetMultibodyDynamicsAnalysis]':
        """List[ConceptGearSetMultibodyDynamicsAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connections(self) -> 'List[_5420.InterMountableComponentConnectionMultibodyDynamicsAnalysis]':
        """List[InterMountableComponentConnectionMultibodyDynamicsAnalysis]: 'Connections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_5393.CycloidalAssemblyMultibodyDynamicsAnalysis]':
        """List[CycloidalAssemblyMultibodyDynamicsAnalysis]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_discs(self) -> 'List[_5395.CycloidalDiscMultibodyDynamicsAnalysis]':
        """List[CycloidalDiscMultibodyDynamicsAnalysis]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5399.CylindricalGearSetMultibodyDynamicsAnalysis]':
        """List[CylindricalGearSetMultibodyDynamicsAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_parts(self) -> 'List[_5406.FEPartMultibodyDynamicsAnalysis]':
        """List[FEPartMultibodyDynamicsAnalysis]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gear_sets(self) -> 'List[_5405.FaceGearSetMultibodyDynamicsAnalysis]':
        """List[FaceGearSetMultibodyDynamicsAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5407.FlexiblePinAssemblyMultibodyDynamicsAnalysis]':
        """List[FlexiblePinAssemblyMultibodyDynamicsAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_sets(self) -> 'List[_5411.GearSetMultibodyDynamicsAnalysis]':
        """List[GearSetMultibodyDynamicsAnalysis]: 'GearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5415.HypoidGearSetMultibodyDynamicsAnalysis]':
        """List[HypoidGearSetMultibodyDynamicsAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5426.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5429.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mass_discs(self) -> 'List[_5430.MassDiscMultibodyDynamicsAnalysis]':
        """List[MassDiscMultibodyDynamicsAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def measurement_components(self) -> 'List[_5434.MeasurementComponentMultibodyDynamicsAnalysis]':
        """List[MeasurementComponentMultibodyDynamicsAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasurementComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def oil_seals(self) -> 'List[_5436.OilSealMultibodyDynamicsAnalysis]':
        """List[OilSealMultibodyDynamicsAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5440.PartToPartShearCouplingMultibodyDynamicsAnalysis]':
        """List[PartToPartShearCouplingMultibodyDynamicsAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartToPartShearCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planet_carriers(self) -> 'List[_5443.PlanetCarrierMultibodyDynamicsAnalysis]':
        """List[PlanetCarrierMultibodyDynamicsAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetCarriers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_loads(self) -> 'List[_5444.PointLoadMultibodyDynamicsAnalysis]':
        """List[PointLoadMultibodyDynamicsAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_loads(self) -> 'List[_5445.PowerLoadMultibodyDynamicsAnalysis]':
        """List[PowerLoadMultibodyDynamicsAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def ring_pins(self) -> 'List[_5447.RingPinsMultibodyDynamicsAnalysis]':
        """List[RingPinsMultibodyDynamicsAnalysis]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPins

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5449.RollingRingAssemblyMultibodyDynamicsAnalysis]':
        """List[RollingRingAssemblyMultibodyDynamicsAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingRingAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5455.ShaftHubConnectionMultibodyDynamicsAnalysis]':
        """List[ShaftHubConnectionMultibodyDynamicsAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shafts(self) -> 'List[_5456.ShaftMultibodyDynamicsAnalysis]':
        """List[ShaftMultibodyDynamicsAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shafts_and_housings(self) -> 'List[_5349.AbstractShaftOrHousingMultibodyDynamicsAnalysis]':
        """List[AbstractShaftOrHousingMultibodyDynamicsAnalysis]: 'ShaftsAndHousings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftsAndHousings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5462.SpiralBevelGearSetMultibodyDynamicsAnalysis]':
        """List[SpiralBevelGearSetMultibodyDynamicsAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spring_dampers(self) -> 'List[_5465.SpringDamperMultibodyDynamicsAnalysis]':
        """List[SpringDamperMultibodyDynamicsAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringDampers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5468.StraightBevelDiffGearSetMultibodyDynamicsAnalysis]':
        """List[StraightBevelDiffGearSetMultibodyDynamicsAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5471.StraightBevelGearSetMultibodyDynamicsAnalysis]':
        """List[StraightBevelGearSetMultibodyDynamicsAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def synchronisers(self) -> 'List[_5475.SynchroniserMultibodyDynamicsAnalysis]':
        """List[SynchroniserMultibodyDynamicsAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Synchronisers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def torque_converters(self) -> 'List[_5480.TorqueConverterMultibodyDynamicsAnalysis]':
        """List[TorqueConverterMultibodyDynamicsAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConverters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5484.UnbalancedMassMultibodyDynamicsAnalysis]':
        """List[UnbalancedMassMultibodyDynamicsAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UnbalancedMasses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5489.WormGearSetMultibodyDynamicsAnalysis]':
        """List[WormGearSetMultibodyDynamicsAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5492.ZerolBevelGearSetMultibodyDynamicsAnalysis]':
        """List[ZerolBevelGearSetMultibodyDynamicsAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AssemblyMultibodyDynamicsAnalysis._Cast_AssemblyMultibodyDynamicsAnalysis':
        return self._Cast_AssemblyMultibodyDynamicsAnalysis(self)
