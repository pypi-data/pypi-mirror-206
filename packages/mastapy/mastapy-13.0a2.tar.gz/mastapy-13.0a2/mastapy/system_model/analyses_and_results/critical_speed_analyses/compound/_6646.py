"""_6646.py

AssemblyCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2413
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6515
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6647, _6649, _6652, _6659,
    _6658, _6680, _6660, _6665,
    _6670, _6682, _6684, _6688,
    _6695, _6694, _6696, _6703,
    _6710, _6713, _6714, _6715,
    _6717, _6719, _6724, _6725,
    _6726, _6728, _6730, _6735,
    _6734, _6740, _6741, _6746,
    _6749, _6752, _6756, _6760,
    _6764, _6767, _6639
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'AssemblyCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundCriticalSpeedAnalysis',)


class AssemblyCompoundCriticalSpeedAnalysis(_6639.AbstractAssemblyCompoundCriticalSpeedAnalysis):
    """AssemblyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_AssemblyCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AssemblyCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'AssemblyCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def abstract_assembly_compound_critical_speed_analysis(self):
            return self._parent._cast(_6639.AbstractAssemblyCompoundCriticalSpeedAnalysis)

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
        def root_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6733
            
            return self._parent._cast(_6733.RootAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def assembly_compound_critical_speed_analysis(self) -> 'AssemblyCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2413.Assembly':
        """Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def assembly_analysis_cases_ready(self) -> 'List[_6515.AssemblyCriticalSpeedAnalysis]':
        """List[AssemblyCriticalSpeedAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bearings(self) -> 'List[_6647.BearingCompoundCriticalSpeedAnalysis]':
        """List[BearingCompoundCriticalSpeedAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def belt_drives(self) -> 'List[_6649.BeltDriveCompoundCriticalSpeedAnalysis]':
        """List[BeltDriveCompoundCriticalSpeedAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltDrives

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_6652.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis]':
        """List[BevelDifferentialGearSetCompoundCriticalSpeedAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolted_joints(self) -> 'List[_6659.BoltedJointCompoundCriticalSpeedAnalysis]':
        """List[BoltedJointCompoundCriticalSpeedAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolts(self) -> 'List[_6658.BoltCompoundCriticalSpeedAnalysis]':
        """List[BoltCompoundCriticalSpeedAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cv_ts(self) -> 'List[_6680.CVTCompoundCriticalSpeedAnalysis]':
        """List[CVTCompoundCriticalSpeedAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CVTs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def clutches(self) -> 'List[_6660.ClutchCompoundCriticalSpeedAnalysis]':
        """List[ClutchCompoundCriticalSpeedAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Clutches

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_couplings(self) -> 'List[_6665.ConceptCouplingCompoundCriticalSpeedAnalysis]':
        """List[ConceptCouplingCompoundCriticalSpeedAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gear_sets(self) -> 'List[_6670.ConceptGearSetCompoundCriticalSpeedAnalysis]':
        """List[ConceptGearSetCompoundCriticalSpeedAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_6682.CycloidalAssemblyCompoundCriticalSpeedAnalysis]':
        """List[CycloidalAssemblyCompoundCriticalSpeedAnalysis]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_discs(self) -> 'List[_6684.CycloidalDiscCompoundCriticalSpeedAnalysis]':
        """List[CycloidalDiscCompoundCriticalSpeedAnalysis]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_6688.CylindricalGearSetCompoundCriticalSpeedAnalysis]':
        """List[CylindricalGearSetCompoundCriticalSpeedAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_parts(self) -> 'List[_6695.FEPartCompoundCriticalSpeedAnalysis]':
        """List[FEPartCompoundCriticalSpeedAnalysis]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gear_sets(self) -> 'List[_6694.FaceGearSetCompoundCriticalSpeedAnalysis]':
        """List[FaceGearSetCompoundCriticalSpeedAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_6696.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis]':
        """List[FlexiblePinAssemblyCompoundCriticalSpeedAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_6703.HypoidGearSetCompoundCriticalSpeedAnalysis]':
        """List[HypoidGearSetCompoundCriticalSpeedAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_6710.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_6713.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mass_discs(self) -> 'List[_6714.MassDiscCompoundCriticalSpeedAnalysis]':
        """List[MassDiscCompoundCriticalSpeedAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def measurement_components(self) -> 'List[_6715.MeasurementComponentCompoundCriticalSpeedAnalysis]':
        """List[MeasurementComponentCompoundCriticalSpeedAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasurementComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def oil_seals(self) -> 'List[_6717.OilSealCompoundCriticalSpeedAnalysis]':
        """List[OilSealCompoundCriticalSpeedAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_6719.PartToPartShearCouplingCompoundCriticalSpeedAnalysis]':
        """List[PartToPartShearCouplingCompoundCriticalSpeedAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartToPartShearCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planet_carriers(self) -> 'List[_6724.PlanetCarrierCompoundCriticalSpeedAnalysis]':
        """List[PlanetCarrierCompoundCriticalSpeedAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetCarriers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_loads(self) -> 'List[_6725.PointLoadCompoundCriticalSpeedAnalysis]':
        """List[PointLoadCompoundCriticalSpeedAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_loads(self) -> 'List[_6726.PowerLoadCompoundCriticalSpeedAnalysis]':
        """List[PowerLoadCompoundCriticalSpeedAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def ring_pins(self) -> 'List[_6728.RingPinsCompoundCriticalSpeedAnalysis]':
        """List[RingPinsCompoundCriticalSpeedAnalysis]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPins

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_6730.RollingRingAssemblyCompoundCriticalSpeedAnalysis]':
        """List[RollingRingAssemblyCompoundCriticalSpeedAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingRingAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_6735.ShaftHubConnectionCompoundCriticalSpeedAnalysis]':
        """List[ShaftHubConnectionCompoundCriticalSpeedAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shafts(self) -> 'List[_6734.ShaftCompoundCriticalSpeedAnalysis]':
        """List[ShaftCompoundCriticalSpeedAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_6740.SpiralBevelGearSetCompoundCriticalSpeedAnalysis]':
        """List[SpiralBevelGearSetCompoundCriticalSpeedAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spring_dampers(self) -> 'List[_6741.SpringDamperCompoundCriticalSpeedAnalysis]':
        """List[SpringDamperCompoundCriticalSpeedAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringDampers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_6746.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis]':
        """List[StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_6749.StraightBevelGearSetCompoundCriticalSpeedAnalysis]':
        """List[StraightBevelGearSetCompoundCriticalSpeedAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def synchronisers(self) -> 'List[_6752.SynchroniserCompoundCriticalSpeedAnalysis]':
        """List[SynchroniserCompoundCriticalSpeedAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Synchronisers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def torque_converters(self) -> 'List[_6756.TorqueConverterCompoundCriticalSpeedAnalysis]':
        """List[TorqueConverterCompoundCriticalSpeedAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConverters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def unbalanced_masses(self) -> 'List[_6760.UnbalancedMassCompoundCriticalSpeedAnalysis]':
        """List[UnbalancedMassCompoundCriticalSpeedAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UnbalancedMasses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_sets(self) -> 'List[_6764.WormGearSetCompoundCriticalSpeedAnalysis]':
        """List[WormGearSetCompoundCriticalSpeedAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_6767.ZerolBevelGearSetCompoundCriticalSpeedAnalysis]':
        """List[ZerolBevelGearSetCompoundCriticalSpeedAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6515.AssemblyCriticalSpeedAnalysis]':
        """List[AssemblyCriticalSpeedAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AssemblyCompoundCriticalSpeedAnalysis._Cast_AssemblyCompoundCriticalSpeedAnalysis':
        return self._Cast_AssemblyCompoundCriticalSpeedAnalysis(self)
