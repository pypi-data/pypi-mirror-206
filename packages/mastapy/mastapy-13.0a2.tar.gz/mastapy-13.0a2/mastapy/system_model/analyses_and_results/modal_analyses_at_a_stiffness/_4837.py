"""_4837.py

AssemblyModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.part_model import _2413
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6783
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4838, _4840, _4843, _4849,
    _4850, _4871, _4853, _4858,
    _4861, _4873, _4875, _4879,
    _4887, _4886, _4888, _4895,
    _4902, _4905, _4906, _4907,
    _4909, _4913, _4916, _4917,
    _4918, _4920, _4922, _4926,
    _4927, _4932, _4935, _4938,
    _4941, _4945, _4949, _4952,
    _4956, _4959, _4830
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'AssemblyModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyModalAnalysisAtAStiffness',)


class AssemblyModalAnalysisAtAStiffness(_4830.AbstractAssemblyModalAnalysisAtAStiffness):
    """AssemblyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_AssemblyModalAnalysisAtAStiffness:
        """Special nested class for casting AssemblyModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'AssemblyModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4830.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4910
            
            return self._parent._cast(_4910.PartModalAnalysisAtAStiffness)

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
        def root_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4925
            
            return self._parent._cast(_4925.RootAssemblyModalAnalysisAtAStiffness)

        @property
        def assembly_modal_analysis_at_a_stiffness(self) -> 'AssemblyModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AssemblyModalAnalysisAtAStiffness.TYPE'):
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
    def bearings(self) -> 'List[_4838.BearingModalAnalysisAtAStiffness]':
        """List[BearingModalAnalysisAtAStiffness]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def belt_drives(self) -> 'List[_4840.BeltDriveModalAnalysisAtAStiffness]':
        """List[BeltDriveModalAnalysisAtAStiffness]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltDrives

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_4843.BevelDifferentialGearSetModalAnalysisAtAStiffness]':
        """List[BevelDifferentialGearSetModalAnalysisAtAStiffness]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolted_joints(self) -> 'List[_4849.BoltedJointModalAnalysisAtAStiffness]':
        """List[BoltedJointModalAnalysisAtAStiffness]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolts(self) -> 'List[_4850.BoltModalAnalysisAtAStiffness]':
        """List[BoltModalAnalysisAtAStiffness]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cv_ts(self) -> 'List[_4871.CVTModalAnalysisAtAStiffness]':
        """List[CVTModalAnalysisAtAStiffness]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CVTs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def clutches(self) -> 'List[_4853.ClutchModalAnalysisAtAStiffness]':
        """List[ClutchModalAnalysisAtAStiffness]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Clutches

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_couplings(self) -> 'List[_4858.ConceptCouplingModalAnalysisAtAStiffness]':
        """List[ConceptCouplingModalAnalysisAtAStiffness]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gear_sets(self) -> 'List[_4861.ConceptGearSetModalAnalysisAtAStiffness]':
        """List[ConceptGearSetModalAnalysisAtAStiffness]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_4873.CycloidalAssemblyModalAnalysisAtAStiffness]':
        """List[CycloidalAssemblyModalAnalysisAtAStiffness]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_discs(self) -> 'List[_4875.CycloidalDiscModalAnalysisAtAStiffness]':
        """List[CycloidalDiscModalAnalysisAtAStiffness]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_4879.CylindricalGearSetModalAnalysisAtAStiffness]':
        """List[CylindricalGearSetModalAnalysisAtAStiffness]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_parts(self) -> 'List[_4887.FEPartModalAnalysisAtAStiffness]':
        """List[FEPartModalAnalysisAtAStiffness]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gear_sets(self) -> 'List[_4886.FaceGearSetModalAnalysisAtAStiffness]':
        """List[FaceGearSetModalAnalysisAtAStiffness]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_4888.FlexiblePinAssemblyModalAnalysisAtAStiffness]':
        """List[FlexiblePinAssemblyModalAnalysisAtAStiffness]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_4895.HypoidGearSetModalAnalysisAtAStiffness]':
        """List[HypoidGearSetModalAnalysisAtAStiffness]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_4902.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness]':
        """List[KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_4905.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mass_discs(self) -> 'List[_4906.MassDiscModalAnalysisAtAStiffness]':
        """List[MassDiscModalAnalysisAtAStiffness]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def measurement_components(self) -> 'List[_4907.MeasurementComponentModalAnalysisAtAStiffness]':
        """List[MeasurementComponentModalAnalysisAtAStiffness]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasurementComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def oil_seals(self) -> 'List[_4909.OilSealModalAnalysisAtAStiffness]':
        """List[OilSealModalAnalysisAtAStiffness]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_4913.PartToPartShearCouplingModalAnalysisAtAStiffness]':
        """List[PartToPartShearCouplingModalAnalysisAtAStiffness]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartToPartShearCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planet_carriers(self) -> 'List[_4916.PlanetCarrierModalAnalysisAtAStiffness]':
        """List[PlanetCarrierModalAnalysisAtAStiffness]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetCarriers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_loads(self) -> 'List[_4917.PointLoadModalAnalysisAtAStiffness]':
        """List[PointLoadModalAnalysisAtAStiffness]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_loads(self) -> 'List[_4918.PowerLoadModalAnalysisAtAStiffness]':
        """List[PowerLoadModalAnalysisAtAStiffness]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def ring_pins(self) -> 'List[_4920.RingPinsModalAnalysisAtAStiffness]':
        """List[RingPinsModalAnalysisAtAStiffness]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPins

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_4922.RollingRingAssemblyModalAnalysisAtAStiffness]':
        """List[RollingRingAssemblyModalAnalysisAtAStiffness]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingRingAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_4926.ShaftHubConnectionModalAnalysisAtAStiffness]':
        """List[ShaftHubConnectionModalAnalysisAtAStiffness]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shafts(self) -> 'List[_4927.ShaftModalAnalysisAtAStiffness]':
        """List[ShaftModalAnalysisAtAStiffness]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_4932.SpiralBevelGearSetModalAnalysisAtAStiffness]':
        """List[SpiralBevelGearSetModalAnalysisAtAStiffness]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spring_dampers(self) -> 'List[_4935.SpringDamperModalAnalysisAtAStiffness]':
        """List[SpringDamperModalAnalysisAtAStiffness]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringDampers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_4938.StraightBevelDiffGearSetModalAnalysisAtAStiffness]':
        """List[StraightBevelDiffGearSetModalAnalysisAtAStiffness]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_4941.StraightBevelGearSetModalAnalysisAtAStiffness]':
        """List[StraightBevelGearSetModalAnalysisAtAStiffness]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def synchronisers(self) -> 'List[_4945.SynchroniserModalAnalysisAtAStiffness]':
        """List[SynchroniserModalAnalysisAtAStiffness]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Synchronisers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def torque_converters(self) -> 'List[_4949.TorqueConverterModalAnalysisAtAStiffness]':
        """List[TorqueConverterModalAnalysisAtAStiffness]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConverters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def unbalanced_masses(self) -> 'List[_4952.UnbalancedMassModalAnalysisAtAStiffness]':
        """List[UnbalancedMassModalAnalysisAtAStiffness]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UnbalancedMasses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_sets(self) -> 'List[_4956.WormGearSetModalAnalysisAtAStiffness]':
        """List[WormGearSetModalAnalysisAtAStiffness]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_4959.ZerolBevelGearSetModalAnalysisAtAStiffness]':
        """List[ZerolBevelGearSetModalAnalysisAtAStiffness]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AssemblyModalAnalysisAtAStiffness._Cast_AssemblyModalAnalysisAtAStiffness':
        return self._Cast_AssemblyModalAnalysisAtAStiffness(self)
