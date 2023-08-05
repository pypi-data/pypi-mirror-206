"""_2969.py

AssemblySteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.part_model import _2413
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6783
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2970, _2972, _2974, _2981,
    _2982, _3004, _2985, _2990,
    _2992, _3005, _3008, _3010,
    _3019, _3017, _3020, _3026,
    _3033, _3036, _3038, _3039,
    _3041, _3045, _3048, _3049,
    _3050, _3052, _3054, _3058,
    _3059, _3063, _3067, _3072,
    _3075, _3082, _3085, _3087,
    _3090, _3093, _2962
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'AssemblySteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblySteadyStateSynchronousResponse',)


class AssemblySteadyStateSynchronousResponse(_2962.AbstractAssemblySteadyStateSynchronousResponse):
    """AssemblySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_AssemblySteadyStateSynchronousResponse:
        """Special nested class for casting AssemblySteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'AssemblySteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def abstract_assembly_steady_state_synchronous_response(self):
            return self._parent._cast(_2962.AbstractAssemblySteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3042
            
            return self._parent._cast(_3042.PartSteadyStateSynchronousResponse)

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
        def root_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3057
            
            return self._parent._cast(_3057.RootAssemblySteadyStateSynchronousResponse)

        @property
        def assembly_steady_state_synchronous_response(self) -> 'AssemblySteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AssemblySteadyStateSynchronousResponse.TYPE'):
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
    def bearings(self) -> 'List[_2970.BearingSteadyStateSynchronousResponse]':
        """List[BearingSteadyStateSynchronousResponse]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def belt_drives(self) -> 'List[_2972.BeltDriveSteadyStateSynchronousResponse]':
        """List[BeltDriveSteadyStateSynchronousResponse]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltDrives

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_2974.BevelDifferentialGearSetSteadyStateSynchronousResponse]':
        """List[BevelDifferentialGearSetSteadyStateSynchronousResponse]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolted_joints(self) -> 'List[_2981.BoltedJointSteadyStateSynchronousResponse]':
        """List[BoltedJointSteadyStateSynchronousResponse]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolts(self) -> 'List[_2982.BoltSteadyStateSynchronousResponse]':
        """List[BoltSteadyStateSynchronousResponse]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cv_ts(self) -> 'List[_3004.CVTSteadyStateSynchronousResponse]':
        """List[CVTSteadyStateSynchronousResponse]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CVTs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def clutches(self) -> 'List[_2985.ClutchSteadyStateSynchronousResponse]':
        """List[ClutchSteadyStateSynchronousResponse]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Clutches

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_couplings(self) -> 'List[_2990.ConceptCouplingSteadyStateSynchronousResponse]':
        """List[ConceptCouplingSteadyStateSynchronousResponse]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gear_sets(self) -> 'List[_2992.ConceptGearSetSteadyStateSynchronousResponse]':
        """List[ConceptGearSetSteadyStateSynchronousResponse]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_3005.CycloidalAssemblySteadyStateSynchronousResponse]':
        """List[CycloidalAssemblySteadyStateSynchronousResponse]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_discs(self) -> 'List[_3008.CycloidalDiscSteadyStateSynchronousResponse]':
        """List[CycloidalDiscSteadyStateSynchronousResponse]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3010.CylindricalGearSetSteadyStateSynchronousResponse]':
        """List[CylindricalGearSetSteadyStateSynchronousResponse]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_parts(self) -> 'List[_3019.FEPartSteadyStateSynchronousResponse]':
        """List[FEPartSteadyStateSynchronousResponse]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gear_sets(self) -> 'List[_3017.FaceGearSetSteadyStateSynchronousResponse]':
        """List[FaceGearSetSteadyStateSynchronousResponse]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3020.FlexiblePinAssemblySteadyStateSynchronousResponse]':
        """List[FlexiblePinAssemblySteadyStateSynchronousResponse]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3026.HypoidGearSetSteadyStateSynchronousResponse]':
        """List[HypoidGearSetSteadyStateSynchronousResponse]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3033.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse]':
        """List[KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3036.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mass_discs(self) -> 'List[_3038.MassDiscSteadyStateSynchronousResponse]':
        """List[MassDiscSteadyStateSynchronousResponse]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def measurement_components(self) -> 'List[_3039.MeasurementComponentSteadyStateSynchronousResponse]':
        """List[MeasurementComponentSteadyStateSynchronousResponse]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasurementComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def oil_seals(self) -> 'List[_3041.OilSealSteadyStateSynchronousResponse]':
        """List[OilSealSteadyStateSynchronousResponse]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_3045.PartToPartShearCouplingSteadyStateSynchronousResponse]':
        """List[PartToPartShearCouplingSteadyStateSynchronousResponse]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartToPartShearCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planet_carriers(self) -> 'List[_3048.PlanetCarrierSteadyStateSynchronousResponse]':
        """List[PlanetCarrierSteadyStateSynchronousResponse]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetCarriers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_loads(self) -> 'List[_3049.PointLoadSteadyStateSynchronousResponse]':
        """List[PointLoadSteadyStateSynchronousResponse]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_loads(self) -> 'List[_3050.PowerLoadSteadyStateSynchronousResponse]':
        """List[PowerLoadSteadyStateSynchronousResponse]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def ring_pins(self) -> 'List[_3052.RingPinsSteadyStateSynchronousResponse]':
        """List[RingPinsSteadyStateSynchronousResponse]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPins

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3054.RollingRingAssemblySteadyStateSynchronousResponse]':
        """List[RollingRingAssemblySteadyStateSynchronousResponse]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingRingAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3058.ShaftHubConnectionSteadyStateSynchronousResponse]':
        """List[ShaftHubConnectionSteadyStateSynchronousResponse]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shafts(self) -> 'List[_3059.ShaftSteadyStateSynchronousResponse]':
        """List[ShaftSteadyStateSynchronousResponse]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3063.SpiralBevelGearSetSteadyStateSynchronousResponse]':
        """List[SpiralBevelGearSetSteadyStateSynchronousResponse]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spring_dampers(self) -> 'List[_3067.SpringDamperSteadyStateSynchronousResponse]':
        """List[SpringDamperSteadyStateSynchronousResponse]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringDampers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3072.StraightBevelDiffGearSetSteadyStateSynchronousResponse]':
        """List[StraightBevelDiffGearSetSteadyStateSynchronousResponse]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3075.StraightBevelGearSetSteadyStateSynchronousResponse]':
        """List[StraightBevelGearSetSteadyStateSynchronousResponse]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def synchronisers(self) -> 'List[_3082.SynchroniserSteadyStateSynchronousResponse]':
        """List[SynchroniserSteadyStateSynchronousResponse]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Synchronisers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def torque_converters(self) -> 'List[_3085.TorqueConverterSteadyStateSynchronousResponse]':
        """List[TorqueConverterSteadyStateSynchronousResponse]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConverters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3087.UnbalancedMassSteadyStateSynchronousResponse]':
        """List[UnbalancedMassSteadyStateSynchronousResponse]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UnbalancedMasses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3090.WormGearSetSteadyStateSynchronousResponse]':
        """List[WormGearSetSteadyStateSynchronousResponse]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3093.ZerolBevelGearSetSteadyStateSynchronousResponse]':
        """List[ZerolBevelGearSetSteadyStateSynchronousResponse]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AssemblySteadyStateSynchronousResponse._Cast_AssemblySteadyStateSynchronousResponse':
        return self._Cast_AssemblySteadyStateSynchronousResponse(self)
