"""_6515.py

AssemblyCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2413
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6783
from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
    _6516, _6518, _6521, _6528,
    _6527, _6551, _6530, _6535,
    _6539, _6553, _6555, _6559,
    _6566, _6565, _6567, _6574,
    _6581, _6584, _6585, _6586,
    _6588, _6591, _6595, _6596,
    _6597, _6599, _6601, _6606,
    _6605, _6611, _6613, _6617,
    _6620, _6623, _6628, _6631,
    _6635, _6638, _6508
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'AssemblyCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCriticalSpeedAnalysis',)


class AssemblyCriticalSpeedAnalysis(_6508.AbstractAssemblyCriticalSpeedAnalysis):
    """AssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ASSEMBLY_CRITICAL_SPEED_ANALYSIS

    class _Cast_AssemblyCriticalSpeedAnalysis:
        """Special nested class for casting AssemblyCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'AssemblyCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def abstract_assembly_critical_speed_analysis(self):
            return self._parent._cast(_6508.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6589
            
            return self._parent._cast(_6589.PartCriticalSpeedAnalysis)

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
        def root_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6604
            
            return self._parent._cast(_6604.RootAssemblyCriticalSpeedAnalysis)

        @property
        def assembly_critical_speed_analysis(self) -> 'AssemblyCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AssemblyCriticalSpeedAnalysis.TYPE'):
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
    def bearings(self) -> 'List[_6516.BearingCriticalSpeedAnalysis]':
        """List[BearingCriticalSpeedAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def belt_drives(self) -> 'List[_6518.BeltDriveCriticalSpeedAnalysis]':
        """List[BeltDriveCriticalSpeedAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltDrives

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_6521.BevelDifferentialGearSetCriticalSpeedAnalysis]':
        """List[BevelDifferentialGearSetCriticalSpeedAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolted_joints(self) -> 'List[_6528.BoltedJointCriticalSpeedAnalysis]':
        """List[BoltedJointCriticalSpeedAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolts(self) -> 'List[_6527.BoltCriticalSpeedAnalysis]':
        """List[BoltCriticalSpeedAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cv_ts(self) -> 'List[_6551.CVTCriticalSpeedAnalysis]':
        """List[CVTCriticalSpeedAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CVTs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def clutches(self) -> 'List[_6530.ClutchCriticalSpeedAnalysis]':
        """List[ClutchCriticalSpeedAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Clutches

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_couplings(self) -> 'List[_6535.ConceptCouplingCriticalSpeedAnalysis]':
        """List[ConceptCouplingCriticalSpeedAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gear_sets(self) -> 'List[_6539.ConceptGearSetCriticalSpeedAnalysis]':
        """List[ConceptGearSetCriticalSpeedAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_6553.CycloidalAssemblyCriticalSpeedAnalysis]':
        """List[CycloidalAssemblyCriticalSpeedAnalysis]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_discs(self) -> 'List[_6555.CycloidalDiscCriticalSpeedAnalysis]':
        """List[CycloidalDiscCriticalSpeedAnalysis]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_6559.CylindricalGearSetCriticalSpeedAnalysis]':
        """List[CylindricalGearSetCriticalSpeedAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_parts(self) -> 'List[_6566.FEPartCriticalSpeedAnalysis]':
        """List[FEPartCriticalSpeedAnalysis]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gear_sets(self) -> 'List[_6565.FaceGearSetCriticalSpeedAnalysis]':
        """List[FaceGearSetCriticalSpeedAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_6567.FlexiblePinAssemblyCriticalSpeedAnalysis]':
        """List[FlexiblePinAssemblyCriticalSpeedAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_6574.HypoidGearSetCriticalSpeedAnalysis]':
        """List[HypoidGearSetCriticalSpeedAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_6581.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_6584.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mass_discs(self) -> 'List[_6585.MassDiscCriticalSpeedAnalysis]':
        """List[MassDiscCriticalSpeedAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def measurement_components(self) -> 'List[_6586.MeasurementComponentCriticalSpeedAnalysis]':
        """List[MeasurementComponentCriticalSpeedAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasurementComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def oil_seals(self) -> 'List[_6588.OilSealCriticalSpeedAnalysis]':
        """List[OilSealCriticalSpeedAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_6591.PartToPartShearCouplingCriticalSpeedAnalysis]':
        """List[PartToPartShearCouplingCriticalSpeedAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartToPartShearCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planet_carriers(self) -> 'List[_6595.PlanetCarrierCriticalSpeedAnalysis]':
        """List[PlanetCarrierCriticalSpeedAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetCarriers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_loads(self) -> 'List[_6596.PointLoadCriticalSpeedAnalysis]':
        """List[PointLoadCriticalSpeedAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_loads(self) -> 'List[_6597.PowerLoadCriticalSpeedAnalysis]':
        """List[PowerLoadCriticalSpeedAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def ring_pins(self) -> 'List[_6599.RingPinsCriticalSpeedAnalysis]':
        """List[RingPinsCriticalSpeedAnalysis]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPins

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_6601.RollingRingAssemblyCriticalSpeedAnalysis]':
        """List[RollingRingAssemblyCriticalSpeedAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingRingAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_6606.ShaftHubConnectionCriticalSpeedAnalysis]':
        """List[ShaftHubConnectionCriticalSpeedAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shafts(self) -> 'List[_6605.ShaftCriticalSpeedAnalysis]':
        """List[ShaftCriticalSpeedAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_6611.SpiralBevelGearSetCriticalSpeedAnalysis]':
        """List[SpiralBevelGearSetCriticalSpeedAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spring_dampers(self) -> 'List[_6613.SpringDamperCriticalSpeedAnalysis]':
        """List[SpringDamperCriticalSpeedAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringDampers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_6617.StraightBevelDiffGearSetCriticalSpeedAnalysis]':
        """List[StraightBevelDiffGearSetCriticalSpeedAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_6620.StraightBevelGearSetCriticalSpeedAnalysis]':
        """List[StraightBevelGearSetCriticalSpeedAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def synchronisers(self) -> 'List[_6623.SynchroniserCriticalSpeedAnalysis]':
        """List[SynchroniserCriticalSpeedAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Synchronisers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def torque_converters(self) -> 'List[_6628.TorqueConverterCriticalSpeedAnalysis]':
        """List[TorqueConverterCriticalSpeedAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConverters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def unbalanced_masses(self) -> 'List[_6631.UnbalancedMassCriticalSpeedAnalysis]':
        """List[UnbalancedMassCriticalSpeedAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UnbalancedMasses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_sets(self) -> 'List[_6635.WormGearSetCriticalSpeedAnalysis]':
        """List[WormGearSetCriticalSpeedAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_6638.ZerolBevelGearSetCriticalSpeedAnalysis]':
        """List[ZerolBevelGearSetCriticalSpeedAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AssemblyCriticalSpeedAnalysis._Cast_AssemblyCriticalSpeedAnalysis':
        return self._Cast_AssemblyCriticalSpeedAnalysis(self)
