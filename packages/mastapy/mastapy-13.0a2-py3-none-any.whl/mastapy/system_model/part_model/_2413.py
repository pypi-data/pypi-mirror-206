"""_2413.py

Assembly
"""
from typing import List, TypeVar, Optional

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import (
    _2445, _2419, _2423, _2424,
    _2433, _2446, _2451, _2452,
    _2448, _2414, _2415, _2416,
    _2422, _2427, _2428, _2432,
    _2434, _2435, _2442, _2443,
    _2444, _2449, _2454, _2456,
    _2457, _2459
)
from mastapy.system_model.part_model.gears import (
    _2503, _2505, _2508, _2511,
    _2514, _2516, _2523, _2527,
    _2531, _2492, _2493, _2494,
    _2495, _2496, _2497, _2498,
    _2499, _2500, _2501, _2502,
    _2504, _2506, _2507, _2509,
    _2513, _2515, _2517, _2518,
    _2519, _2520, _2521, _2522,
    _2524, _2525, _2526, _2528,
    _2529, _2530, _2532, _2533
)
from mastapy.system_model.part_model.couplings import (
    _2577, _2555, _2557, _2558,
    _2560, _2561, _2562, _2563,
    _2565, _2566, _2567, _2568,
    _2569, _2575, _2576, _2579,
    _2580, _2581, _2583, _2584,
    _2585, _2586, _2587, _2589
)
from mastapy.system_model.part_model.shaft_model import _2462
from mastapy.system_model.part_model.cycloidal import _2547, _2548, _2549
from mastapy.bearings import _1881, _1854
from mastapy.system_model.part_model.creation_options import (
    _2550, _2551, _2552, _2553,
    _2554
)
from mastapy.gears.gear_designs.creation_options import _1140, _1143
from mastapy.gears import _329
from mastapy._internal.python_net import python_net_import
from mastapy.gears.gear_designs.bevel import _1173
from mastapy.nodal_analysis import _78
from mastapy._internal.cast_exception import CastException

_ARRAY = python_net_import('System', 'Array')
_STRING = python_net_import('System', 'String')
_DOUBLE = python_net_import('System', 'Double')
_INT_32 = python_net_import('System', 'Int32')
_ROLLING_BEARING_TYPE = python_net_import('SMT.MastaAPI.Bearings', 'RollingBearingType')
_BELT_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'BeltCreationOptions')
_CYCLOIDAL_ASSEMBLY_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'CycloidalAssemblyCreationOptions')
_CYLINDRICAL_GEAR_LINEAR_TRAIN_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'CylindricalGearLinearTrainCreationOptions')
_PLANET_CARRIER_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'PlanetCarrierCreationOptions')
_SHAFT_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.CreationOptions', 'ShaftCreationOptions')
_CYLINDRICAL_GEAR_PAIR_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.CreationOptions', 'CylindricalGearPairCreationOptions')
_SPIRAL_BEVEL_GEAR_SET_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.CreationOptions', 'SpiralBevelGearSetCreationOptions')
_HAND = python_net_import('SMT.MastaAPI.Gears', 'Hand')
_AGMA_GLEASON_CONICAL_GEAR_GEOMETRY_METHODS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Bevel', 'AGMAGleasonConicalGearGeometryMethods')
_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Assembly')


__docformat__ = 'restructuredtext en'
__all__ = ('Assembly',)


class Assembly(_2414.AbstractAssembly):
    """Assembly

    This is a mastapy class.
    """

    TYPE = _ASSEMBLY

    class _Cast_Assembly:
        """Special nested class for casting Assembly to subclasses."""

        def __init__(self, parent: 'Assembly'):
            self._parent = parent

        @property
        def abstract_assembly(self):
            return self._parent._cast(_2414.AbstractAssembly)

        @property
        def part(self):
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def root_assembly(self):
            return self._parent._cast(_2454.RootAssembly)

        @property
        def assembly(self) -> 'Assembly':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Assembly.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'AxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_of_widest_cylindrical_gear(self) -> 'float':
        """float: 'FaceWidthOfWidestCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceWidthOfWidestCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def largest_number_of_teeth(self) -> 'int':
        """int: 'LargestNumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LargestNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @property
    def mass_of_bearings(self) -> 'float':
        """float: 'MassOfBearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfBearings

        if temp is None:
            return 0.0

        return temp

    @property
    def mass_of_fe_part_housings(self) -> 'float':
        """float: 'MassOfFEPartHousings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfFEPartHousings

        if temp is None:
            return 0.0

        return temp

    @property
    def mass_of_fe_part_shafts(self) -> 'float':
        """float: 'MassOfFEPartShafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfFEPartShafts

        if temp is None:
            return 0.0

        return temp

    @property
    def mass_of_gears(self) -> 'float':
        """float: 'MassOfGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfGears

        if temp is None:
            return 0.0

        return temp

    @property
    def mass_of_other_parts(self) -> 'float':
        """float: 'MassOfOtherParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfOtherParts

        if temp is None:
            return 0.0

        return temp

    @property
    def mass_of_shafts(self) -> 'float':
        """float: 'MassOfShafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfShafts

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_tip_thickness(self) -> 'float':
        """float: 'MinimumTipThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumTipThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def smallest_number_of_teeth(self) -> 'int':
        """int: 'SmallestNumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @property
    def transverse_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_and_axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseAndAxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseAndAxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_level_specification(self) -> '_2445.OilLevelSpecification':
        """OilLevelSpecification: 'OilLevelSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilLevelSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearings(self) -> 'List[_2419.Bearing]':
        """List[Bearing]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolted_joints(self) -> 'List[_2423.BoltedJoint]':
        """List[BoltedJoint]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_details(self) -> 'List[_2424.Component]':
        """List[Component]: 'ComponentDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def components_with_unknown_scalar_mass(self) -> 'List[_2424.Component]':
        """List[Component]: 'ComponentsWithUnknownScalarMass' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentsWithUnknownScalarMass

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def conical_gear_sets(self) -> 'List[_2503.ConicalGearSet]':
        """List[ConicalGearSet]: 'ConicalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_2505.CylindricalGearSet]':
        """List[CylindricalGearSet]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_parts(self) -> 'List[_2433.FEPart]':
        """List[FEPart]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gear_sets(self) -> 'List[_2508.FaceGearSet]':
        """List[FaceGearSet]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_sets(self) -> 'List[_2511.GearSet]':
        """List[GearSet]: 'GearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_2514.HypoidGearSet]':
        """List[HypoidGearSet]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_gear_sets(self) -> 'List[_2516.KlingelnbergCycloPalloidConicalGearSet]':
        """List[KlingelnbergCycloPalloidConicalGearSet]: 'KlingelnbergCycloPalloidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def oil_seals(self) -> 'List[_2446.OilSeal]':
        """List[OilSeal]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_loads(self) -> 'List[_2451.PointLoad]':
        """List[PointLoad]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_loads(self) -> 'List[_2452.PowerLoad]':
        """List[PowerLoad]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_2577.ShaftHubConnection]':
        """List[ShaftHubConnection]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shafts(self) -> 'List[_2462.Shaft]':
        """List[Shaft]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_2523.SpiralBevelGearSet]':
        """List[SpiralBevelGearSet]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_2527.StraightBevelGearSet]':
        """List[StraightBevelGearSet]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_sets(self) -> 'List[_2531.WormGearSet]':
        """List[WormGearSet]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def get_part_named(self, name: 'str') -> '_2448.Part':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2448.Part.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2448.Part)(method_result) if method_result is not None else None

    def get_part_named_of_type_assembly(self, name: 'str') -> 'Assembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[Assembly.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(Assembly)(method_result) if method_result is not None else None

    def get_part_named_of_type_abstract_assembly(self, name: 'str') -> '_2414.AbstractAssembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2414.AbstractAssembly.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2414.AbstractAssembly)(method_result) if method_result is not None else None

    def get_part_named_of_type_abstract_shaft(self, name: 'str') -> '_2415.AbstractShaft':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2415.AbstractShaft.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2415.AbstractShaft)(method_result) if method_result is not None else None

    def get_part_named_of_type_abstract_shaft_or_housing(self, name: 'str') -> '_2416.AbstractShaftOrHousing':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2416.AbstractShaftOrHousing.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2416.AbstractShaftOrHousing)(method_result) if method_result is not None else None

    def get_part_named_of_type_bearing(self, name: 'str') -> '_2419.Bearing':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2419.Bearing.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2419.Bearing)(method_result) if method_result is not None else None

    def get_part_named_of_type_bolt(self, name: 'str') -> '_2422.Bolt':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2422.Bolt.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2422.Bolt)(method_result) if method_result is not None else None

    def get_part_named_of_type_bolted_joint(self, name: 'str') -> '_2423.BoltedJoint':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2423.BoltedJoint.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2423.BoltedJoint)(method_result) if method_result is not None else None

    def get_part_named_of_type_component(self, name: 'str') -> '_2424.Component':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2424.Component.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2424.Component)(method_result) if method_result is not None else None

    def get_part_named_of_type_connector(self, name: 'str') -> '_2427.Connector':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2427.Connector.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2427.Connector)(method_result) if method_result is not None else None

    def get_part_named_of_type_datum(self, name: 'str') -> '_2428.Datum':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2428.Datum.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2428.Datum)(method_result) if method_result is not None else None

    def get_part_named_of_type_external_cad_model(self, name: 'str') -> '_2432.ExternalCADModel':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2432.ExternalCADModel.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2432.ExternalCADModel)(method_result) if method_result is not None else None

    def get_part_named_of_type_fe_part(self, name: 'str') -> '_2433.FEPart':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2433.FEPart.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2433.FEPart)(method_result) if method_result is not None else None

    def get_part_named_of_type_flexible_pin_assembly(self, name: 'str') -> '_2434.FlexiblePinAssembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2434.FlexiblePinAssembly.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2434.FlexiblePinAssembly)(method_result) if method_result is not None else None

    def get_part_named_of_type_guide_dxf_model(self, name: 'str') -> '_2435.GuideDxfModel':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2435.GuideDxfModel.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2435.GuideDxfModel)(method_result) if method_result is not None else None

    def get_part_named_of_type_mass_disc(self, name: 'str') -> '_2442.MassDisc':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2442.MassDisc.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2442.MassDisc)(method_result) if method_result is not None else None

    def get_part_named_of_type_measurement_component(self, name: 'str') -> '_2443.MeasurementComponent':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2443.MeasurementComponent.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2443.MeasurementComponent)(method_result) if method_result is not None else None

    def get_part_named_of_type_mountable_component(self, name: 'str') -> '_2444.MountableComponent':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2444.MountableComponent.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2444.MountableComponent)(method_result) if method_result is not None else None

    def get_part_named_of_type_oil_seal(self, name: 'str') -> '_2446.OilSeal':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2446.OilSeal.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2446.OilSeal)(method_result) if method_result is not None else None

    def get_part_named_of_type_planet_carrier(self, name: 'str') -> '_2449.PlanetCarrier':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2449.PlanetCarrier.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2449.PlanetCarrier)(method_result) if method_result is not None else None

    def get_part_named_of_type_point_load(self, name: 'str') -> '_2451.PointLoad':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2451.PointLoad.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2451.PointLoad)(method_result) if method_result is not None else None

    def get_part_named_of_type_power_load(self, name: 'str') -> '_2452.PowerLoad':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2452.PowerLoad.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2452.PowerLoad)(method_result) if method_result is not None else None

    def get_part_named_of_type_root_assembly(self, name: 'str') -> '_2454.RootAssembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2454.RootAssembly.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2454.RootAssembly)(method_result) if method_result is not None else None

    def get_part_named_of_type_specialised_assembly(self, name: 'str') -> '_2456.SpecialisedAssembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2456.SpecialisedAssembly.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2456.SpecialisedAssembly)(method_result) if method_result is not None else None

    def get_part_named_of_type_unbalanced_mass(self, name: 'str') -> '_2457.UnbalancedMass':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2457.UnbalancedMass.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2457.UnbalancedMass)(method_result) if method_result is not None else None

    def get_part_named_of_type_virtual_component(self, name: 'str') -> '_2459.VirtualComponent':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2459.VirtualComponent.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2459.VirtualComponent)(method_result) if method_result is not None else None

    def get_part_named_of_type_shaft(self, name: 'str') -> '_2462.Shaft':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2462.Shaft.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2462.Shaft)(method_result) if method_result is not None else None

    def get_part_named_of_type_agma_gleason_conical_gear(self, name: 'str') -> '_2492.AGMAGleasonConicalGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2492.AGMAGleasonConicalGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2492.AGMAGleasonConicalGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_agma_gleason_conical_gear_set(self, name: 'str') -> '_2493.AGMAGleasonConicalGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2493.AGMAGleasonConicalGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2493.AGMAGleasonConicalGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_differential_gear(self, name: 'str') -> '_2494.BevelDifferentialGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2494.BevelDifferentialGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2494.BevelDifferentialGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_differential_gear_set(self, name: 'str') -> '_2495.BevelDifferentialGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2495.BevelDifferentialGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2495.BevelDifferentialGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_differential_planet_gear(self, name: 'str') -> '_2496.BevelDifferentialPlanetGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2496.BevelDifferentialPlanetGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2496.BevelDifferentialPlanetGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_differential_sun_gear(self, name: 'str') -> '_2497.BevelDifferentialSunGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2497.BevelDifferentialSunGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2497.BevelDifferentialSunGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_gear(self, name: 'str') -> '_2498.BevelGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2498.BevelGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2498.BevelGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_bevel_gear_set(self, name: 'str') -> '_2499.BevelGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2499.BevelGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2499.BevelGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_concept_gear(self, name: 'str') -> '_2500.ConceptGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2500.ConceptGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2500.ConceptGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_concept_gear_set(self, name: 'str') -> '_2501.ConceptGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2501.ConceptGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2501.ConceptGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_conical_gear(self, name: 'str') -> '_2502.ConicalGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2502.ConicalGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2502.ConicalGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_conical_gear_set(self, name: 'str') -> '_2503.ConicalGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2503.ConicalGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2503.ConicalGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_cylindrical_gear(self, name: 'str') -> '_2504.CylindricalGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2504.CylindricalGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2504.CylindricalGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_cylindrical_gear_set(self, name: 'str') -> '_2505.CylindricalGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2505.CylindricalGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2505.CylindricalGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_cylindrical_planet_gear(self, name: 'str') -> '_2506.CylindricalPlanetGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2506.CylindricalPlanetGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2506.CylindricalPlanetGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_face_gear(self, name: 'str') -> '_2507.FaceGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2507.FaceGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2507.FaceGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_face_gear_set(self, name: 'str') -> '_2508.FaceGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2508.FaceGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2508.FaceGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_gear(self, name: 'str') -> '_2509.Gear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2509.Gear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2509.Gear)(method_result) if method_result is not None else None

    def get_part_named_of_type_gear_set(self, name: 'str') -> '_2511.GearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2511.GearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2511.GearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_hypoid_gear(self, name: 'str') -> '_2513.HypoidGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2513.HypoidGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2513.HypoidGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_hypoid_gear_set(self, name: 'str') -> '_2514.HypoidGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2514.HypoidGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2514.HypoidGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_conical_gear(self, name: 'str') -> '_2515.KlingelnbergCycloPalloidConicalGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2515.KlingelnbergCycloPalloidConicalGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2515.KlingelnbergCycloPalloidConicalGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self, name: 'str') -> '_2516.KlingelnbergCycloPalloidConicalGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2516.KlingelnbergCycloPalloidConicalGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2516.KlingelnbergCycloPalloidConicalGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self, name: 'str') -> '_2517.KlingelnbergCycloPalloidHypoidGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2517.KlingelnbergCycloPalloidHypoidGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2517.KlingelnbergCycloPalloidHypoidGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self, name: 'str') -> '_2518.KlingelnbergCycloPalloidHypoidGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2518.KlingelnbergCycloPalloidHypoidGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2518.KlingelnbergCycloPalloidHypoidGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, name: 'str') -> '_2519.KlingelnbergCycloPalloidSpiralBevelGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2519.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2519.KlingelnbergCycloPalloidSpiralBevelGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, name: 'str') -> '_2520.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2520.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2520.KlingelnbergCycloPalloidSpiralBevelGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_planetary_gear_set(self, name: 'str') -> '_2521.PlanetaryGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2521.PlanetaryGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2521.PlanetaryGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_spiral_bevel_gear(self, name: 'str') -> '_2522.SpiralBevelGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2522.SpiralBevelGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2522.SpiralBevelGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_spiral_bevel_gear_set(self, name: 'str') -> '_2523.SpiralBevelGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2523.SpiralBevelGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2523.SpiralBevelGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_diff_gear(self, name: 'str') -> '_2524.StraightBevelDiffGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2524.StraightBevelDiffGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2524.StraightBevelDiffGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_diff_gear_set(self, name: 'str') -> '_2525.StraightBevelDiffGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2525.StraightBevelDiffGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2525.StraightBevelDiffGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_gear(self, name: 'str') -> '_2526.StraightBevelGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2526.StraightBevelGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2526.StraightBevelGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_gear_set(self, name: 'str') -> '_2527.StraightBevelGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2527.StraightBevelGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2527.StraightBevelGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_planet_gear(self, name: 'str') -> '_2528.StraightBevelPlanetGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2528.StraightBevelPlanetGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2528.StraightBevelPlanetGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_straight_bevel_sun_gear(self, name: 'str') -> '_2529.StraightBevelSunGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2529.StraightBevelSunGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2529.StraightBevelSunGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_worm_gear(self, name: 'str') -> '_2530.WormGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2530.WormGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2530.WormGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_worm_gear_set(self, name: 'str') -> '_2531.WormGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2531.WormGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2531.WormGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_zerol_bevel_gear(self, name: 'str') -> '_2532.ZerolBevelGear':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2532.ZerolBevelGear.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2532.ZerolBevelGear)(method_result) if method_result is not None else None

    def get_part_named_of_type_zerol_bevel_gear_set(self, name: 'str') -> '_2533.ZerolBevelGearSet':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2533.ZerolBevelGearSet.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2533.ZerolBevelGearSet)(method_result) if method_result is not None else None

    def get_part_named_of_type_cycloidal_assembly(self, name: 'str') -> '_2547.CycloidalAssembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2547.CycloidalAssembly.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2547.CycloidalAssembly)(method_result) if method_result is not None else None

    def get_part_named_of_type_cycloidal_disc(self, name: 'str') -> '_2548.CycloidalDisc':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2548.CycloidalDisc.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2548.CycloidalDisc)(method_result) if method_result is not None else None

    def get_part_named_of_type_ring_pins(self, name: 'str') -> '_2549.RingPins':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2549.RingPins.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2549.RingPins)(method_result) if method_result is not None else None

    def get_part_named_of_type_belt_drive(self, name: 'str') -> '_2555.BeltDrive':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2555.BeltDrive.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2555.BeltDrive)(method_result) if method_result is not None else None

    def get_part_named_of_type_clutch(self, name: 'str') -> '_2557.Clutch':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2557.Clutch.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2557.Clutch)(method_result) if method_result is not None else None

    def get_part_named_of_type_clutch_half(self, name: 'str') -> '_2558.ClutchHalf':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2558.ClutchHalf.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2558.ClutchHalf)(method_result) if method_result is not None else None

    def get_part_named_of_type_concept_coupling(self, name: 'str') -> '_2560.ConceptCoupling':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2560.ConceptCoupling.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2560.ConceptCoupling)(method_result) if method_result is not None else None

    def get_part_named_of_type_concept_coupling_half(self, name: 'str') -> '_2561.ConceptCouplingHalf':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2561.ConceptCouplingHalf.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2561.ConceptCouplingHalf)(method_result) if method_result is not None else None

    def get_part_named_of_type_coupling(self, name: 'str') -> '_2562.Coupling':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2562.Coupling.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2562.Coupling)(method_result) if method_result is not None else None

    def get_part_named_of_type_coupling_half(self, name: 'str') -> '_2563.CouplingHalf':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2563.CouplingHalf.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2563.CouplingHalf)(method_result) if method_result is not None else None

    def get_part_named_of_type_cvt(self, name: 'str') -> '_2565.CVT':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2565.CVT.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2565.CVT)(method_result) if method_result is not None else None

    def get_part_named_of_type_cvt_pulley(self, name: 'str') -> '_2566.CVTPulley':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2566.CVTPulley.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2566.CVTPulley)(method_result) if method_result is not None else None

    def get_part_named_of_type_part_to_part_shear_coupling(self, name: 'str') -> '_2567.PartToPartShearCoupling':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2567.PartToPartShearCoupling.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2567.PartToPartShearCoupling)(method_result) if method_result is not None else None

    def get_part_named_of_type_part_to_part_shear_coupling_half(self, name: 'str') -> '_2568.PartToPartShearCouplingHalf':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2568.PartToPartShearCouplingHalf.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2568.PartToPartShearCouplingHalf)(method_result) if method_result is not None else None

    def get_part_named_of_type_pulley(self, name: 'str') -> '_2569.Pulley':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2569.Pulley.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2569.Pulley)(method_result) if method_result is not None else None

    def get_part_named_of_type_rolling_ring(self, name: 'str') -> '_2575.RollingRing':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2575.RollingRing.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2575.RollingRing)(method_result) if method_result is not None else None

    def get_part_named_of_type_rolling_ring_assembly(self, name: 'str') -> '_2576.RollingRingAssembly':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2576.RollingRingAssembly.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2576.RollingRingAssembly)(method_result) if method_result is not None else None

    def get_part_named_of_type_shaft_hub_connection(self, name: 'str') -> '_2577.ShaftHubConnection':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2577.ShaftHubConnection.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2577.ShaftHubConnection)(method_result) if method_result is not None else None

    def get_part_named_of_type_spring_damper(self, name: 'str') -> '_2579.SpringDamper':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2579.SpringDamper.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2579.SpringDamper)(method_result) if method_result is not None else None

    def get_part_named_of_type_spring_damper_half(self, name: 'str') -> '_2580.SpringDamperHalf':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2580.SpringDamperHalf.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2580.SpringDamperHalf)(method_result) if method_result is not None else None

    def get_part_named_of_type_synchroniser(self, name: 'str') -> '_2581.Synchroniser':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2581.Synchroniser.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2581.Synchroniser)(method_result) if method_result is not None else None

    def get_part_named_of_type_synchroniser_half(self, name: 'str') -> '_2583.SynchroniserHalf':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2583.SynchroniserHalf.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2583.SynchroniserHalf)(method_result) if method_result is not None else None

    def get_part_named_of_type_synchroniser_part(self, name: 'str') -> '_2584.SynchroniserPart':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2584.SynchroniserPart.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2584.SynchroniserPart)(method_result) if method_result is not None else None

    def get_part_named_of_type_synchroniser_sleeve(self, name: 'str') -> '_2585.SynchroniserSleeve':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2585.SynchroniserSleeve.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2585.SynchroniserSleeve)(method_result) if method_result is not None else None

    def get_part_named_of_type_torque_converter(self, name: 'str') -> '_2586.TorqueConverter':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2586.TorqueConverter.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2586.TorqueConverter)(method_result) if method_result is not None else None

    def get_part_named_of_type_torque_converter_pump(self, name: 'str') -> '_2587.TorqueConverterPump':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2587.TorqueConverterPump.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2587.TorqueConverterPump)(method_result) if method_result is not None else None

    def get_part_named_of_type_torque_converter_turbine(self, name: 'str') -> '_2589.TorqueConverterTurbine':
        """ 'GetPartNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            T_get_part_named
        """

        name = str(name)
        method_result = self.wrapped.GetPartNamed[_2589.TorqueConverterTurbine.TYPE](name if name else '')
        return constructor.new_from_mastapy_type(_2589.TorqueConverterTurbine)(method_result) if method_result is not None else None

    def add_part(self, part_type: 'Assembly.PartType', name: 'str') -> '_2448.Part':
        """ 'AddPart' is the original name of this method.

        Args:
            part_type (mastapy.system_model.part_model.Assembly.PartType)
            name (str)

        Returns:
            mastapy.system_model.part_model.Part
        """

        part_type = conversion.mp_to_pn_enum(part_type, Assembly.PartType.type_())
        name = str(name)
        method_result = self.wrapped.AddPart(part_type, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def all_parts(self) -> 'List[_2448.Part]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Part]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2448.Part.TYPE]())

    def all_parts_of_type_assembly(self) -> 'List[Assembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Assembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[Assembly.TYPE]())

    def all_parts_of_type_abstract_assembly(self) -> 'List[_2414.AbstractAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2414.AbstractAssembly.TYPE]())

    def all_parts_of_type_abstract_shaft(self) -> 'List[_2415.AbstractShaft]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaft]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2415.AbstractShaft.TYPE]())

    def all_parts_of_type_abstract_shaft_or_housing(self) -> 'List[_2416.AbstractShaftOrHousing]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaftOrHousing]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2416.AbstractShaftOrHousing.TYPE]())

    def all_parts_of_type_bearing(self) -> 'List[_2419.Bearing]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bearing]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2419.Bearing.TYPE]())

    def all_parts_of_type_bolt(self) -> 'List[_2422.Bolt]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bolt]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2422.Bolt.TYPE]())

    def all_parts_of_type_bolted_joint(self) -> 'List[_2423.BoltedJoint]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.BoltedJoint]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2423.BoltedJoint.TYPE]())

    def all_parts_of_type_component(self) -> 'List[_2424.Component]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Component]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2424.Component.TYPE]())

    def all_parts_of_type_connector(self) -> 'List[_2427.Connector]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Connector]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2427.Connector.TYPE]())

    def all_parts_of_type_datum(self) -> 'List[_2428.Datum]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Datum]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2428.Datum.TYPE]())

    def all_parts_of_type_external_cad_model(self) -> 'List[_2432.ExternalCADModel]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.ExternalCADModel]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2432.ExternalCADModel.TYPE]())

    def all_parts_of_type_fe_part(self) -> 'List[_2433.FEPart]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FEPart]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2433.FEPart.TYPE]())

    def all_parts_of_type_flexible_pin_assembly(self) -> 'List[_2434.FlexiblePinAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FlexiblePinAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2434.FlexiblePinAssembly.TYPE]())

    def all_parts_of_type_guide_dxf_model(self) -> 'List[_2435.GuideDxfModel]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.GuideDxfModel]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2435.GuideDxfModel.TYPE]())

    def all_parts_of_type_mass_disc(self) -> 'List[_2442.MassDisc]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MassDisc]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2442.MassDisc.TYPE]())

    def all_parts_of_type_measurement_component(self) -> 'List[_2443.MeasurementComponent]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MeasurementComponent]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2443.MeasurementComponent.TYPE]())

    def all_parts_of_type_mountable_component(self) -> 'List[_2444.MountableComponent]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MountableComponent]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2444.MountableComponent.TYPE]())

    def all_parts_of_type_oil_seal(self) -> 'List[_2446.OilSeal]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.OilSeal]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2446.OilSeal.TYPE]())

    def all_parts_of_type_planet_carrier(self) -> 'List[_2449.PlanetCarrier]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PlanetCarrier]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2449.PlanetCarrier.TYPE]())

    def all_parts_of_type_point_load(self) -> 'List[_2451.PointLoad]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PointLoad]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2451.PointLoad.TYPE]())

    def all_parts_of_type_power_load(self) -> 'List[_2452.PowerLoad]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PowerLoad]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2452.PowerLoad.TYPE]())

    def all_parts_of_type_root_assembly(self) -> 'List[_2454.RootAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.RootAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2454.RootAssembly.TYPE]())

    def all_parts_of_type_specialised_assembly(self) -> 'List[_2456.SpecialisedAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.SpecialisedAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2456.SpecialisedAssembly.TYPE]())

    def all_parts_of_type_unbalanced_mass(self) -> 'List[_2457.UnbalancedMass]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.UnbalancedMass]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2457.UnbalancedMass.TYPE]())

    def all_parts_of_type_virtual_component(self) -> 'List[_2459.VirtualComponent]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.VirtualComponent]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2459.VirtualComponent.TYPE]())

    def all_parts_of_type_shaft(self) -> 'List[_2462.Shaft]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.shaft_model.Shaft]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2462.Shaft.TYPE]())

    def all_parts_of_type_agma_gleason_conical_gear(self) -> 'List[_2492.AGMAGleasonConicalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2492.AGMAGleasonConicalGear.TYPE]())

    def all_parts_of_type_agma_gleason_conical_gear_set(self) -> 'List[_2493.AGMAGleasonConicalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2493.AGMAGleasonConicalGearSet.TYPE]())

    def all_parts_of_type_bevel_differential_gear(self) -> 'List[_2494.BevelDifferentialGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2494.BevelDifferentialGear.TYPE]())

    def all_parts_of_type_bevel_differential_gear_set(self) -> 'List[_2495.BevelDifferentialGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2495.BevelDifferentialGearSet.TYPE]())

    def all_parts_of_type_bevel_differential_planet_gear(self) -> 'List[_2496.BevelDifferentialPlanetGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2496.BevelDifferentialPlanetGear.TYPE]())

    def all_parts_of_type_bevel_differential_sun_gear(self) -> 'List[_2497.BevelDifferentialSunGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialSunGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2497.BevelDifferentialSunGear.TYPE]())

    def all_parts_of_type_bevel_gear(self) -> 'List[_2498.BevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2498.BevelGear.TYPE]())

    def all_parts_of_type_bevel_gear_set(self) -> 'List[_2499.BevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2499.BevelGearSet.TYPE]())

    def all_parts_of_type_concept_gear(self) -> 'List[_2500.ConceptGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2500.ConceptGear.TYPE]())

    def all_parts_of_type_concept_gear_set(self) -> 'List[_2501.ConceptGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2501.ConceptGearSet.TYPE]())

    def all_parts_of_type_conical_gear(self) -> 'List[_2502.ConicalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2502.ConicalGear.TYPE]())

    def all_parts_of_type_conical_gear_set(self) -> 'List[_2503.ConicalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2503.ConicalGearSet.TYPE]())

    def all_parts_of_type_cylindrical_gear(self) -> 'List[_2504.CylindricalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2504.CylindricalGear.TYPE]())

    def all_parts_of_type_cylindrical_gear_set(self) -> 'List[_2505.CylindricalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2505.CylindricalGearSet.TYPE]())

    def all_parts_of_type_cylindrical_planet_gear(self) -> 'List[_2506.CylindricalPlanetGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalPlanetGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2506.CylindricalPlanetGear.TYPE]())

    def all_parts_of_type_face_gear(self) -> 'List[_2507.FaceGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2507.FaceGear.TYPE]())

    def all_parts_of_type_face_gear_set(self) -> 'List[_2508.FaceGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2508.FaceGearSet.TYPE]())

    def all_parts_of_type_gear(self) -> 'List[_2509.Gear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.Gear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2509.Gear.TYPE]())

    def all_parts_of_type_gear_set(self) -> 'List[_2511.GearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.GearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2511.GearSet.TYPE]())

    def all_parts_of_type_hypoid_gear(self) -> 'List[_2513.HypoidGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2513.HypoidGear.TYPE]())

    def all_parts_of_type_hypoid_gear_set(self) -> 'List[_2514.HypoidGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2514.HypoidGearSet.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> 'List[_2515.KlingelnbergCycloPalloidConicalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2515.KlingelnbergCycloPalloidConicalGear.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> 'List[_2516.KlingelnbergCycloPalloidConicalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2516.KlingelnbergCycloPalloidConicalGearSet.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> 'List[_2517.KlingelnbergCycloPalloidHypoidGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2517.KlingelnbergCycloPalloidHypoidGear.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> 'List[_2518.KlingelnbergCycloPalloidHypoidGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2518.KlingelnbergCycloPalloidHypoidGearSet.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> 'List[_2519.KlingelnbergCycloPalloidSpiralBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2519.KlingelnbergCycloPalloidSpiralBevelGear.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> 'List[_2520.KlingelnbergCycloPalloidSpiralBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2520.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE]())

    def all_parts_of_type_planetary_gear_set(self) -> 'List[_2521.PlanetaryGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.PlanetaryGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2521.PlanetaryGearSet.TYPE]())

    def all_parts_of_type_spiral_bevel_gear(self) -> 'List[_2522.SpiralBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2522.SpiralBevelGear.TYPE]())

    def all_parts_of_type_spiral_bevel_gear_set(self) -> 'List[_2523.SpiralBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2523.SpiralBevelGearSet.TYPE]())

    def all_parts_of_type_straight_bevel_diff_gear(self) -> 'List[_2524.StraightBevelDiffGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2524.StraightBevelDiffGear.TYPE]())

    def all_parts_of_type_straight_bevel_diff_gear_set(self) -> 'List[_2525.StraightBevelDiffGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2525.StraightBevelDiffGearSet.TYPE]())

    def all_parts_of_type_straight_bevel_gear(self) -> 'List[_2526.StraightBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2526.StraightBevelGear.TYPE]())

    def all_parts_of_type_straight_bevel_gear_set(self) -> 'List[_2527.StraightBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2527.StraightBevelGearSet.TYPE]())

    def all_parts_of_type_straight_bevel_planet_gear(self) -> 'List[_2528.StraightBevelPlanetGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelPlanetGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2528.StraightBevelPlanetGear.TYPE]())

    def all_parts_of_type_straight_bevel_sun_gear(self) -> 'List[_2529.StraightBevelSunGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelSunGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2529.StraightBevelSunGear.TYPE]())

    def all_parts_of_type_worm_gear(self) -> 'List[_2530.WormGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2530.WormGear.TYPE]())

    def all_parts_of_type_worm_gear_set(self) -> 'List[_2531.WormGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2531.WormGearSet.TYPE]())

    def all_parts_of_type_zerol_bevel_gear(self) -> 'List[_2532.ZerolBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2532.ZerolBevelGear.TYPE]())

    def all_parts_of_type_zerol_bevel_gear_set(self) -> 'List[_2533.ZerolBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2533.ZerolBevelGearSet.TYPE]())

    def all_parts_of_type_cycloidal_assembly(self) -> 'List[_2547.CycloidalAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.CycloidalAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2547.CycloidalAssembly.TYPE]())

    def all_parts_of_type_cycloidal_disc(self) -> 'List[_2548.CycloidalDisc]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.CycloidalDisc]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2548.CycloidalDisc.TYPE]())

    def all_parts_of_type_ring_pins(self) -> 'List[_2549.RingPins]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.RingPins]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2549.RingPins.TYPE]())

    def all_parts_of_type_belt_drive(self) -> 'List[_2555.BeltDrive]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.BeltDrive]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2555.BeltDrive.TYPE]())

    def all_parts_of_type_clutch(self) -> 'List[_2557.Clutch]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Clutch]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2557.Clutch.TYPE]())

    def all_parts_of_type_clutch_half(self) -> 'List[_2558.ClutchHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ClutchHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2558.ClutchHalf.TYPE]())

    def all_parts_of_type_concept_coupling(self) -> 'List[_2560.ConceptCoupling]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCoupling]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2560.ConceptCoupling.TYPE]())

    def all_parts_of_type_concept_coupling_half(self) -> 'List[_2561.ConceptCouplingHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCouplingHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2561.ConceptCouplingHalf.TYPE]())

    def all_parts_of_type_coupling(self) -> 'List[_2562.Coupling]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Coupling]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2562.Coupling.TYPE]())

    def all_parts_of_type_coupling_half(self) -> 'List[_2563.CouplingHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CouplingHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2563.CouplingHalf.TYPE]())

    def all_parts_of_type_cvt(self) -> 'List[_2565.CVT]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVT]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2565.CVT.TYPE]())

    def all_parts_of_type_cvt_pulley(self) -> 'List[_2566.CVTPulley]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVTPulley]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2566.CVTPulley.TYPE]())

    def all_parts_of_type_part_to_part_shear_coupling(self) -> 'List[_2567.PartToPartShearCoupling]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.PartToPartShearCoupling]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2567.PartToPartShearCoupling.TYPE]())

    def all_parts_of_type_part_to_part_shear_coupling_half(self) -> 'List[_2568.PartToPartShearCouplingHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2568.PartToPartShearCouplingHalf.TYPE]())

    def all_parts_of_type_pulley(self) -> 'List[_2569.Pulley]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Pulley]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2569.Pulley.TYPE]())

    def all_parts_of_type_rolling_ring(self) -> 'List[_2575.RollingRing]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRing]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2575.RollingRing.TYPE]())

    def all_parts_of_type_rolling_ring_assembly(self) -> 'List[_2576.RollingRingAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRingAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2576.RollingRingAssembly.TYPE]())

    def all_parts_of_type_shaft_hub_connection(self) -> 'List[_2577.ShaftHubConnection]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ShaftHubConnection]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2577.ShaftHubConnection.TYPE]())

    def all_parts_of_type_spring_damper(self) -> 'List[_2579.SpringDamper]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamper]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2579.SpringDamper.TYPE]())

    def all_parts_of_type_spring_damper_half(self) -> 'List[_2580.SpringDamperHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamperHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2580.SpringDamperHalf.TYPE]())

    def all_parts_of_type_synchroniser(self) -> 'List[_2581.Synchroniser]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Synchroniser]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2581.Synchroniser.TYPE]())

    def all_parts_of_type_synchroniser_half(self) -> 'List[_2583.SynchroniserHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2583.SynchroniserHalf.TYPE]())

    def all_parts_of_type_synchroniser_part(self) -> 'List[_2584.SynchroniserPart]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserPart]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2584.SynchroniserPart.TYPE]())

    def all_parts_of_type_synchroniser_sleeve(self) -> 'List[_2585.SynchroniserSleeve]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserSleeve]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2585.SynchroniserSleeve.TYPE]())

    def all_parts_of_type_torque_converter(self) -> 'List[_2586.TorqueConverter]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverter]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2586.TorqueConverter.TYPE]())

    def all_parts_of_type_torque_converter_pump(self) -> 'List[_2587.TorqueConverterPump]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterPump]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2587.TorqueConverterPump.TYPE]())

    def all_parts_of_type_torque_converter_turbine(self) -> 'List[_2589.TorqueConverterTurbine]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterTurbine]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2589.TorqueConverterTurbine.TYPE]())

    def add_assembly(self, name: Optional['str'] = 'Assembly') -> 'Assembly':
        """ 'AddAssembly' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.Assembly
        """

        name = str(name)
        method_result = self.wrapped.AddAssembly(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_axial_clearance_bearing(self, name: 'str', contact_diameter: 'float') -> '_2419.Bearing':
        """ 'AddAxialClearanceBearing' is the original name of this method.

        Args:
            name (str)
            contact_diameter (float)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        name = str(name)
        contact_diameter = float(contact_diameter)
        method_result = self.wrapped.AddAxialClearanceBearing(name if name else '', contact_diameter if contact_diameter else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_bearing(self, name: 'str') -> '_2419.Bearing':
        """ 'AddBearing' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        name = str(name)
        method_result = self.wrapped.AddBearing.Overloads[_STRING](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_bearing_with_name_and_rolling_bearing_type(self, name: 'str', type_: '_1881.RollingBearingType') -> '_2419.Bearing':
        """ 'AddBearing' is the original name of this method.

        Args:
            name (str)
            type_ (mastapy.bearings.RollingBearingType)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        name = str(name)
        type_ = conversion.mp_to_pn_enum(type_, _1881.RollingBearingType.type_())
        method_result = self.wrapped.AddBearing.Overloads[_STRING, _ROLLING_BEARING_TYPE](name if name else '', type_)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_bearing_with_name_rolling_bearing_type_and_designation(self, name: 'str', type_: '_1881.RollingBearingType', designation: 'str') -> '_2419.Bearing':
        """ 'AddBearing' is the original name of this method.

        Args:
            name (str)
            type_ (mastapy.bearings.RollingBearingType)
            designation (str)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        name = str(name)
        type_ = conversion.mp_to_pn_enum(type_, _1881.RollingBearingType.type_())
        designation = str(designation)
        method_result = self.wrapped.AddBearing.Overloads[_STRING, _ROLLING_BEARING_TYPE, _STRING](name if name else '', type_, designation if designation else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_belt_drive_with_options(self, belt_creation_options: Optional['_2550.BeltCreationOptions'] = None) -> '_2555.BeltDrive':
        """ 'AddBeltDrive' is the original name of this method.

        Args:
            belt_creation_options (mastapy.system_model.part_model.creation_options.BeltCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.couplings.BeltDrive
        """

        method_result = self.wrapped.AddBeltDrive.Overloads[_BELT_CREATION_OPTIONS](belt_creation_options.wrapped if belt_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_belt_drive(self, centre_distance: Optional['float'] = 0.1, pulley_a_diameter: Optional['float'] = 0.08, pulley_b_diameter: Optional['float'] = 0.08, name: Optional['str'] = 'Belt Drive') -> '_2555.BeltDrive':
        """ 'AddBeltDrive' is the original name of this method.

        Args:
            centre_distance (float, optional)
            pulley_a_diameter (float, optional)
            pulley_b_diameter (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.BeltDrive
        """

        centre_distance = float(centre_distance)
        pulley_a_diameter = float(pulley_a_diameter)
        pulley_b_diameter = float(pulley_b_diameter)
        name = str(name)
        method_result = self.wrapped.AddBeltDrive.Overloads[_DOUBLE, _DOUBLE, _DOUBLE, _STRING](centre_distance if centre_distance else 0.0, pulley_a_diameter if pulley_a_diameter else 0.0, pulley_b_diameter if pulley_b_diameter else 0.0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_bolted_joint(self, name: Optional['str'] = 'Bolted Joint') -> '_2423.BoltedJoint':
        """ 'AddBoltedJoint' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.BoltedJoint
        """

        name = str(name)
        method_result = self.wrapped.AddBoltedJoint(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cvt(self, name: Optional['str'] = 'CVT') -> '_2565.CVT':
        """ 'AddCVT' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.CVT
        """

        name = str(name)
        method_result = self.wrapped.AddCVT(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_clutch(self, name: Optional['str'] = 'Clutch') -> '_2557.Clutch':
        """ 'AddClutch' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.Clutch
        """

        name = str(name)
        method_result = self.wrapped.AddClutch(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_concept_coupling(self, name: Optional['str'] = 'Concept Coupling') -> '_2560.ConceptCoupling':
        """ 'AddConceptCoupling' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.ConceptCoupling
        """

        name = str(name)
        method_result = self.wrapped.AddConceptCoupling(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cycloidal_assembly_with_options(self, cycloidal_assembly_creation_options: Optional['_2551.CycloidalAssemblyCreationOptions'] = None) -> '_2547.CycloidalAssembly':
        """ 'AddCycloidalAssembly' is the original name of this method.

        Args:
            cycloidal_assembly_creation_options (mastapy.system_model.part_model.creation_options.CycloidalAssemblyCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.cycloidal.CycloidalAssembly
        """

        method_result = self.wrapped.AddCycloidalAssembly.Overloads[_CYCLOIDAL_ASSEMBLY_CREATION_OPTIONS](cycloidal_assembly_creation_options.wrapped if cycloidal_assembly_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cycloidal_assembly(self, number_of_discs: Optional['int'] = 1, number_of_pins: Optional['int'] = 10, name: Optional['str'] = 'Cycloidal Assembly') -> '_2547.CycloidalAssembly':
        """ 'AddCycloidalAssembly' is the original name of this method.

        Args:
            number_of_discs (int, optional)
            number_of_pins (int, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.cycloidal.CycloidalAssembly
        """

        number_of_discs = int(number_of_discs)
        number_of_pins = int(number_of_pins)
        name = str(name)
        method_result = self.wrapped.AddCycloidalAssembly.Overloads[_INT_32, _INT_32, _STRING](number_of_discs if number_of_discs else 0, number_of_pins if number_of_pins else 0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cylindrical_gear_pair_with_options(self, cylindrical_gear_pair_creation_options: Optional['_1140.CylindricalGearPairCreationOptions'] = None) -> '_2505.CylindricalGearSet':
        """ 'AddCylindricalGearPair' is the original name of this method.

        Args:
            cylindrical_gear_pair_creation_options (mastapy.gears.gear_designs.creation_options.CylindricalGearPairCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        """

        method_result = self.wrapped.AddCylindricalGearPair.Overloads[_CYLINDRICAL_GEAR_PAIR_CREATION_OPTIONS](cylindrical_gear_pair_creation_options.wrapped if cylindrical_gear_pair_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cylindrical_gear_pair(self, centre_distance: 'float') -> '_2505.CylindricalGearSet':
        """ 'AddCylindricalGearPair' is the original name of this method.

        Args:
            centre_distance (float)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        """

        centre_distance = float(centre_distance)
        method_result = self.wrapped.AddCylindricalGearPair.Overloads[_DOUBLE](centre_distance if centre_distance else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cylindrical_gear_set_with_options(self, cylindrical_gear_linear_train_creation_options: Optional['_2552.CylindricalGearLinearTrainCreationOptions'] = None) -> '_2505.CylindricalGearSet':
        """ 'AddCylindricalGearSet' is the original name of this method.

        Args:
            cylindrical_gear_linear_train_creation_options (mastapy.system_model.part_model.creation_options.CylindricalGearLinearTrainCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        """

        method_result = self.wrapped.AddCylindricalGearSet.Overloads[_CYLINDRICAL_GEAR_LINEAR_TRAIN_CREATION_OPTIONS](cylindrical_gear_linear_train_creation_options.wrapped if cylindrical_gear_linear_train_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cylindrical_gear_set_extended(self, name: 'str', normal_pressure_angle: 'float', helix_angle: 'float', normal_module: 'float', pinion_hand: '_329.Hand', centre_distances: 'List[float]') -> '_2505.CylindricalGearSet':
        """ 'AddCylindricalGearSet' is the original name of this method.

        Args:
            name (str)
            normal_pressure_angle (float)
            helix_angle (float)
            normal_module (float)
            pinion_hand (mastapy.gears.Hand)
            centre_distances (List[float])

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        """

        name = str(name)
        normal_pressure_angle = float(normal_pressure_angle)
        helix_angle = float(helix_angle)
        normal_module = float(normal_module)
        pinion_hand = conversion.mp_to_pn_enum(pinion_hand, _329.Hand.type_())
        centre_distances = conversion.mp_to_pn_array_float(centre_distances)
        method_result = self.wrapped.AddCylindricalGearSet.Overloads[_STRING, _DOUBLE, _DOUBLE, _DOUBLE, _HAND, _ARRAY[_DOUBLE]](name if name else '', normal_pressure_angle if normal_pressure_angle else 0.0, helix_angle if helix_angle else 0.0, normal_module if normal_module else 0.0, pinion_hand, centre_distances)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_cylindrical_gear_set(self, name: 'str', centre_distances: 'List[float]') -> '_2505.CylindricalGearSet':
        """ 'AddCylindricalGearSet' is the original name of this method.

        Args:
            name (str)
            centre_distances (List[float])

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGearSet
        """

        name = str(name)
        centre_distances = conversion.mp_to_pn_array_float(centre_distances)
        method_result = self.wrapped.AddCylindricalGearSet.Overloads[_STRING, _ARRAY[_DOUBLE]](name if name else '', centre_distances)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_datum(self, name: Optional['str'] = 'Datum') -> '_2428.Datum':
        """ 'AddDatum' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.Datum
        """

        name = str(name)
        method_result = self.wrapped.AddDatum(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_fe_part(self, name: Optional['str'] = 'FE Part') -> '_2433.FEPart':
        """ 'AddFEPart' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.FEPart
        """

        name = str(name)
        method_result = self.wrapped.AddFEPart(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_face_gear_set(self, name: Optional['str'] = 'Face Gear Set') -> '_2508.FaceGearSet':
        """ 'AddFaceGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.FaceGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddFaceGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_hypoid_gear_set(self, name: Optional['str'] = 'Hypoid Gear Set') -> '_2514.HypoidGearSet':
        """ 'AddHypoidGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.HypoidGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddHypoidGearSet.Overloads[_STRING](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_hypoid_gear_set_detailed(self, name: Optional['str'] = 'Hypoid Gear Set', pinion_number_of_teeth: Optional['int'] = 7, wheel_number_of_teeth: Optional['int'] = 41, outer_transverse_module: Optional['float'] = 0.0109756, wheel_face_width: Optional['float'] = 0.072, offset: Optional['float'] = 0.045, average_pressure_angle: Optional['float'] = 0.3926991, design_method: Optional['_1173.AGMAGleasonConicalGearGeometryMethods'] = _1173.AGMAGleasonConicalGearGeometryMethods.GLEASON) -> '_2514.HypoidGearSet':
        """ 'AddHypoidGearSet' is the original name of this method.

        Args:
            name (str, optional)
            pinion_number_of_teeth (int, optional)
            wheel_number_of_teeth (int, optional)
            outer_transverse_module (float, optional)
            wheel_face_width (float, optional)
            offset (float, optional)
            average_pressure_angle (float, optional)
            design_method (mastapy.gears.gear_designs.bevel.AGMAGleasonConicalGearGeometryMethods, optional)

        Returns:
            mastapy.system_model.part_model.gears.HypoidGearSet
        """

        name = str(name)
        pinion_number_of_teeth = int(pinion_number_of_teeth)
        wheel_number_of_teeth = int(wheel_number_of_teeth)
        outer_transverse_module = float(outer_transverse_module)
        wheel_face_width = float(wheel_face_width)
        offset = float(offset)
        average_pressure_angle = float(average_pressure_angle)
        design_method = conversion.mp_to_pn_enum(design_method, _1173.AGMAGleasonConicalGearGeometryMethods.type_())
        method_result = self.wrapped.AddHypoidGearSet.Overloads[_STRING, _INT_32, _INT_32, _DOUBLE, _DOUBLE, _DOUBLE, _DOUBLE, _AGMA_GLEASON_CONICAL_GEAR_GEOMETRY_METHODS](name if name else '', pinion_number_of_teeth if pinion_number_of_teeth else 0, wheel_number_of_teeth if wheel_number_of_teeth else 0, outer_transverse_module if outer_transverse_module else 0.0, wheel_face_width if wheel_face_width else 0.0, offset if offset else 0.0, average_pressure_angle if average_pressure_angle else 0.0, design_method)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_klingelnberg_cyclo_palloid_hypoid_gear_set(self, name: Optional['str'] = 'Klingelnberg Cyclo Palloid Hypoid Gear Set') -> '_2518.KlingelnbergCycloPalloidHypoidGearSet':
        """ 'AddKlingelnbergCycloPalloidHypoidGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddKlingelnbergCycloPalloidHypoidGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, name: Optional['str'] = 'Klingelnberg Cyclo Palloid Spiral Bevel Gear Set') -> '_2520.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """ 'AddKlingelnbergCycloPalloidSpiralBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddKlingelnbergCycloPalloidSpiralBevelGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_linear_bearing(self, name: 'str', width: 'float') -> '_2419.Bearing':
        """ 'AddLinearBearing' is the original name of this method.

        Args:
            name (str)
            width (float)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        name = str(name)
        width = float(width)
        method_result = self.wrapped.AddLinearBearing(name if name else '', width if width else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_mass_disc(self, name: Optional['str'] = 'Mass Disc') -> '_2442.MassDisc':
        """ 'AddMassDisc' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.MassDisc
        """

        name = str(name)
        method_result = self.wrapped.AddMassDisc(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_measurement_component(self, name: Optional['str'] = 'Measurement Component') -> '_2443.MeasurementComponent':
        """ 'AddMeasurementComponent' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.MeasurementComponent
        """

        name = str(name)
        method_result = self.wrapped.AddMeasurementComponent(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_oil_seal(self, name: Optional['str'] = 'Oil Seal') -> '_2446.OilSeal':
        """ 'AddOilSeal' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.OilSeal
        """

        name = str(name)
        method_result = self.wrapped.AddOilSeal(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_planet_carrier_with_options(self, planet_carrier_creation_options: Optional['_2553.PlanetCarrierCreationOptions'] = None) -> '_2449.PlanetCarrier':
        """ 'AddPlanetCarrier' is the original name of this method.

        Args:
            planet_carrier_creation_options (mastapy.system_model.part_model.creation_options.PlanetCarrierCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.PlanetCarrier
        """

        method_result = self.wrapped.AddPlanetCarrier.Overloads[_PLANET_CARRIER_CREATION_OPTIONS](planet_carrier_creation_options.wrapped if planet_carrier_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_planet_carrier(self, number_of_planets: Optional['int'] = 3, diameter: Optional['float'] = 0.05) -> '_2449.PlanetCarrier':
        """ 'AddPlanetCarrier' is the original name of this method.

        Args:
            number_of_planets (int, optional)
            diameter (float, optional)

        Returns:
            mastapy.system_model.part_model.PlanetCarrier
        """

        number_of_planets = int(number_of_planets)
        diameter = float(diameter)
        method_result = self.wrapped.AddPlanetCarrier.Overloads[_INT_32, _DOUBLE](number_of_planets if number_of_planets else 0, diameter if diameter else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_planetary_gear_set(self, name: Optional['str'] = 'Planetary Gear Set') -> '_2521.PlanetaryGearSet':
        """ 'AddPlanetaryGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.PlanetaryGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddPlanetaryGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_point_load(self, name: Optional['str'] = 'Point Load') -> '_2451.PointLoad':
        """ 'AddPointLoad' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.PointLoad
        """

        name = str(name)
        method_result = self.wrapped.AddPointLoad(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_power_load(self, name: Optional['str'] = 'Power Load') -> '_2452.PowerLoad':
        """ 'AddPowerLoad' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.PowerLoad
        """

        name = str(name)
        method_result = self.wrapped.AddPowerLoad(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_rolling_bearing_from_catalogue(self, catalogue: '_1854.BearingCatalog', designation: 'str', name: 'str') -> '_2419.Bearing':
        """ 'AddRollingBearingFromCatalogue' is the original name of this method.

        Args:
            catalogue (mastapy.bearings.BearingCatalog)
            designation (str)
            name (str)

        Returns:
            mastapy.system_model.part_model.Bearing
        """

        catalogue = conversion.mp_to_pn_enum(catalogue, _1854.BearingCatalog.type_())
        designation = str(designation)
        name = str(name)
        method_result = self.wrapped.AddRollingBearingFromCatalogue(catalogue, designation if designation else '', name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_rolling_ring(self, name: Optional['str'] = 'Rolling Ring') -> '_2575.RollingRing':
        """ 'AddRollingRing' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.RollingRing
        """

        name = str(name)
        method_result = self.wrapped.AddRollingRing(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_shaft_with_options(self, shaft_creation_options: '_2554.ShaftCreationOptions') -> '_2462.Shaft':
        """ 'AddShaft' is the original name of this method.

        Args:
            shaft_creation_options (mastapy.system_model.part_model.creation_options.ShaftCreationOptions)

        Returns:
            mastapy.system_model.part_model.shaft_model.Shaft
        """

        method_result = self.wrapped.AddShaft.Overloads[_SHAFT_CREATION_OPTIONS](shaft_creation_options.wrapped if shaft_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_shaft(self, length: Optional['float'] = 0.1, outer_diameter: Optional['float'] = 0.025, bore: Optional['float'] = 0.0, name: Optional['str'] = 'Shaft') -> '_2462.Shaft':
        """ 'AddShaft' is the original name of this method.

        Args:
            length (float, optional)
            outer_diameter (float, optional)
            bore (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.shaft_model.Shaft
        """

        length = float(length)
        outer_diameter = float(outer_diameter)
        bore = float(bore)
        name = str(name)
        method_result = self.wrapped.AddShaft.Overloads[_DOUBLE, _DOUBLE, _DOUBLE, _STRING](length if length else 0.0, outer_diameter if outer_diameter else 0.0, bore if bore else 0.0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_spiral_bevel_differential_gear_set(self, name: Optional['str'] = 'Spiral Bevel Differential Gear Set') -> '_2495.BevelDifferentialGearSet':
        """ 'AddSpiralBevelDifferentialGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddSpiralBevelDifferentialGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_spiral_bevel_gear_set_with_options(self, spiral_bevel_gear_set_creation_options: Optional['_1143.SpiralBevelGearSetCreationOptions'] = None) -> '_2523.SpiralBevelGearSet':
        """ 'AddSpiralBevelGearSet' is the original name of this method.

        Args:
            spiral_bevel_gear_set_creation_options (mastapy.gears.gear_designs.creation_options.SpiralBevelGearSetCreationOptions, optional)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGearSet
        """

        method_result = self.wrapped.AddSpiralBevelGearSet.Overloads[_SPIRAL_BEVEL_GEAR_SET_CREATION_OPTIONS](spiral_bevel_gear_set_creation_options.wrapped if spiral_bevel_gear_set_creation_options else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_spiral_bevel_gear_set(self, name: Optional['str'] = 'Spiral Bevel Gear Set') -> '_2523.SpiralBevelGearSet':
        """ 'AddSpiralBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddSpiralBevelGearSet.Overloads[_STRING](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_spiral_bevel_gear_set_detailed(self, name: Optional['str'] = 'Spiral Bevel Gear Set', outer_transverse_module: Optional['float'] = 0.00635, pressure_angle: Optional['float'] = 0.02, mean_spiral_angle: Optional['float'] = 0.523599, wheel_number_of_teeth: Optional['int'] = 43, pinion_number_of_teeth: Optional['int'] = 14, wheel_face_width: Optional['float'] = 0.02, pinion_face_width: Optional['float'] = 0.02, pinion_face_width_offset: Optional['float'] = 0.0, shaft_angle: Optional['float'] = 1.5708) -> '_2523.SpiralBevelGearSet':
        """ 'AddSpiralBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)
            outer_transverse_module (float, optional)
            pressure_angle (float, optional)
            mean_spiral_angle (float, optional)
            wheel_number_of_teeth (int, optional)
            pinion_number_of_teeth (int, optional)
            wheel_face_width (float, optional)
            pinion_face_width (float, optional)
            pinion_face_width_offset (float, optional)
            shaft_angle (float, optional)

        Returns:
            mastapy.system_model.part_model.gears.SpiralBevelGearSet
        """

        name = str(name)
        outer_transverse_module = float(outer_transverse_module)
        pressure_angle = float(pressure_angle)
        mean_spiral_angle = float(mean_spiral_angle)
        wheel_number_of_teeth = int(wheel_number_of_teeth)
        pinion_number_of_teeth = int(pinion_number_of_teeth)
        wheel_face_width = float(wheel_face_width)
        pinion_face_width = float(pinion_face_width)
        pinion_face_width_offset = float(pinion_face_width_offset)
        shaft_angle = float(shaft_angle)
        method_result = self.wrapped.AddSpiralBevelGearSet.Overloads[_STRING, _DOUBLE, _DOUBLE, _DOUBLE, _INT_32, _INT_32, _DOUBLE, _DOUBLE, _DOUBLE, _DOUBLE](name if name else '', outer_transverse_module if outer_transverse_module else 0.0, pressure_angle if pressure_angle else 0.0, mean_spiral_angle if mean_spiral_angle else 0.0, wheel_number_of_teeth if wheel_number_of_teeth else 0, pinion_number_of_teeth if pinion_number_of_teeth else 0, wheel_face_width if wheel_face_width else 0.0, pinion_face_width if pinion_face_width else 0.0, pinion_face_width_offset if pinion_face_width_offset else 0.0, shaft_angle if shaft_angle else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_spring_damper(self, name: Optional['str'] = 'Spring Damper') -> '_2579.SpringDamper':
        """ 'AddSpringDamper' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.SpringDamper
        """

        name = str(name)
        method_result = self.wrapped.AddSpringDamper(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_straight_bevel_differential_gear_set(self, name: Optional['str'] = 'Straight Bevel Differential Gear Set') -> '_2525.StraightBevelDiffGearSet':
        """ 'AddStraightBevelDifferentialGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelDiffGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddStraightBevelDifferentialGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_straight_bevel_gear_set(self, name: Optional['str'] = 'Straight Bevel Gear Set') -> '_2527.StraightBevelGearSet':
        """ 'AddStraightBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.StraightBevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddStraightBevelGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_synchroniser(self, name: Optional['str'] = 'Synchroniser') -> '_2581.Synchroniser':
        """ 'AddSynchroniser' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.Synchroniser
        """

        name = str(name)
        method_result = self.wrapped.AddSynchroniser(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_torque_converter(self, name: Optional['str'] = 'Torque Converter') -> '_2586.TorqueConverter':
        """ 'AddTorqueConverter' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.couplings.TorqueConverter
        """

        name = str(name)
        method_result = self.wrapped.AddTorqueConverter(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_unbalanced_mass(self, name: Optional['str'] = 'Unbalanced Mass') -> '_2457.UnbalancedMass':
        """ 'AddUnbalancedMass' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.UnbalancedMass
        """

        name = str(name)
        method_result = self.wrapped.AddUnbalancedMass(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_worm_gear_set(self, name: Optional['str'] = 'Worm Gear Set') -> '_2531.WormGearSet':
        """ 'AddWormGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.WormGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddWormGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_zerol_bevel_differential_gear_set(self, name: Optional['str'] = 'Zerol Bevel Differential Gear Set') -> '_2495.BevelDifferentialGearSet':
        """ 'AddZerolBevelDifferentialGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.BevelDifferentialGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddZerolBevelDifferentialGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_zerol_bevel_gear_set(self, name: Optional['str'] = 'Zerol Bevel Gear Set') -> '_2533.ZerolBevelGearSet':
        """ 'AddZerolBevelGearSet' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.gears.ZerolBevelGearSet
        """

        name = str(name)
        method_result = self.wrapped.AddZerolBevelGearSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_shaft_hub_connection(self, name: 'str') -> '_2577.ShaftHubConnection':
        """ 'AddShaftHubConnection' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.part_model.couplings.ShaftHubConnection
        """

        name = str(name)
        method_result = self.wrapped.AddShaftHubConnection(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def import_fe_mesh_from_file(self, file_name: 'str', stiffness_matrix: '_78.NodalMatrix') -> '_2433.FEPart':
        """ 'ImportFEMeshFromFile' is the original name of this method.

        Args:
            file_name (str)
            stiffness_matrix (mastapy.nodal_analysis.NodalMatrix)

        Returns:
            mastapy.system_model.part_model.FEPart
        """

        file_name = str(file_name)
        method_result = self.wrapped.ImportFEMeshFromFile(file_name if file_name else '', stiffness_matrix.wrapped if stiffness_matrix else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'Assembly._Cast_Assembly':
        return self._Cast_Assembly(self)
