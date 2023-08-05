"""_2448.py

Part
"""
from typing import List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.math_utility import _1506
from mastapy.system_model.connections_and_sockets import _2253
from mastapy.system_model.part_model import _2413
from mastapy.system_model.import_export import _2223
from mastapy.system_model import _2188
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Part')


__docformat__ = 'restructuredtext en'
__all__ = ('Part',)


class Part(_2188.DesignEntity):
    """Part

    This is a mastapy class.
    """

    TYPE = _PART

    class _Cast_Part:
        """Special nested class for casting Part to subclasses."""

        def __init__(self, parent: 'Part'):
            self._parent = parent

        @property
        def design_entity(self):
            return self._parent._cast(_2188.DesignEntity)

        @property
        def assembly(self):
            return self._parent._cast(_2413.Assembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2414
            
            return self._parent._cast(_2414.AbstractAssembly)

        @property
        def abstract_shaft(self):
            from mastapy.system_model.part_model import _2415
            
            return self._parent._cast(_2415.AbstractShaft)

        @property
        def abstract_shaft_or_housing(self):
            from mastapy.system_model.part_model import _2416
            
            return self._parent._cast(_2416.AbstractShaftOrHousing)

        @property
        def bearing(self):
            from mastapy.system_model.part_model import _2419
            
            return self._parent._cast(_2419.Bearing)

        @property
        def bolt(self):
            from mastapy.system_model.part_model import _2422
            
            return self._parent._cast(_2422.Bolt)

        @property
        def bolted_joint(self):
            from mastapy.system_model.part_model import _2423
            
            return self._parent._cast(_2423.BoltedJoint)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2424
            
            return self._parent._cast(_2424.Component)

        @property
        def connector(self):
            from mastapy.system_model.part_model import _2427
            
            return self._parent._cast(_2427.Connector)

        @property
        def datum(self):
            from mastapy.system_model.part_model import _2428
            
            return self._parent._cast(_2428.Datum)

        @property
        def external_cad_model(self):
            from mastapy.system_model.part_model import _2432
            
            return self._parent._cast(_2432.ExternalCADModel)

        @property
        def fe_part(self):
            from mastapy.system_model.part_model import _2433
            
            return self._parent._cast(_2433.FEPart)

        @property
        def flexible_pin_assembly(self):
            from mastapy.system_model.part_model import _2434
            
            return self._parent._cast(_2434.FlexiblePinAssembly)

        @property
        def guide_dxf_model(self):
            from mastapy.system_model.part_model import _2435
            
            return self._parent._cast(_2435.GuideDxfModel)

        @property
        def mass_disc(self):
            from mastapy.system_model.part_model import _2442
            
            return self._parent._cast(_2442.MassDisc)

        @property
        def measurement_component(self):
            from mastapy.system_model.part_model import _2443
            
            return self._parent._cast(_2443.MeasurementComponent)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2444
            
            return self._parent._cast(_2444.MountableComponent)

        @property
        def oil_seal(self):
            from mastapy.system_model.part_model import _2446
            
            return self._parent._cast(_2446.OilSeal)

        @property
        def planet_carrier(self):
            from mastapy.system_model.part_model import _2449
            
            return self._parent._cast(_2449.PlanetCarrier)

        @property
        def point_load(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.PointLoad)

        @property
        def power_load(self):
            from mastapy.system_model.part_model import _2452
            
            return self._parent._cast(_2452.PowerLoad)

        @property
        def root_assembly(self):
            from mastapy.system_model.part_model import _2454
            
            return self._parent._cast(_2454.RootAssembly)

        @property
        def specialised_assembly(self):
            from mastapy.system_model.part_model import _2456
            
            return self._parent._cast(_2456.SpecialisedAssembly)

        @property
        def unbalanced_mass(self):
            from mastapy.system_model.part_model import _2457
            
            return self._parent._cast(_2457.UnbalancedMass)

        @property
        def virtual_component(self):
            from mastapy.system_model.part_model import _2459
            
            return self._parent._cast(_2459.VirtualComponent)

        @property
        def shaft(self):
            from mastapy.system_model.part_model.shaft_model import _2462
            
            return self._parent._cast(_2462.Shaft)

        @property
        def agma_gleason_conical_gear(self):
            from mastapy.system_model.part_model.gears import _2492
            
            return self._parent._cast(_2492.AGMAGleasonConicalGear)

        @property
        def agma_gleason_conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2493
            
            return self._parent._cast(_2493.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear(self):
            from mastapy.system_model.part_model.gears import _2494
            
            return self._parent._cast(_2494.BevelDifferentialGear)

        @property
        def bevel_differential_gear_set(self):
            from mastapy.system_model.part_model.gears import _2495
            
            return self._parent._cast(_2495.BevelDifferentialGearSet)

        @property
        def bevel_differential_planet_gear(self):
            from mastapy.system_model.part_model.gears import _2496
            
            return self._parent._cast(_2496.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(self):
            from mastapy.system_model.part_model.gears import _2497
            
            return self._parent._cast(_2497.BevelDifferentialSunGear)

        @property
        def bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2498
            
            return self._parent._cast(_2498.BevelGear)

        @property
        def bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2499
            
            return self._parent._cast(_2499.BevelGearSet)

        @property
        def concept_gear(self):
            from mastapy.system_model.part_model.gears import _2500
            
            return self._parent._cast(_2500.ConceptGear)

        @property
        def concept_gear_set(self):
            from mastapy.system_model.part_model.gears import _2501
            
            return self._parent._cast(_2501.ConceptGearSet)

        @property
        def conical_gear(self):
            from mastapy.system_model.part_model.gears import _2502
            
            return self._parent._cast(_2502.ConicalGear)

        @property
        def conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2503
            
            return self._parent._cast(_2503.ConicalGearSet)

        @property
        def cylindrical_gear(self):
            from mastapy.system_model.part_model.gears import _2504
            
            return self._parent._cast(_2504.CylindricalGear)

        @property
        def cylindrical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2505
            
            return self._parent._cast(_2505.CylindricalGearSet)

        @property
        def cylindrical_planet_gear(self):
            from mastapy.system_model.part_model.gears import _2506
            
            return self._parent._cast(_2506.CylindricalPlanetGear)

        @property
        def face_gear(self):
            from mastapy.system_model.part_model.gears import _2507
            
            return self._parent._cast(_2507.FaceGear)

        @property
        def face_gear_set(self):
            from mastapy.system_model.part_model.gears import _2508
            
            return self._parent._cast(_2508.FaceGearSet)

        @property
        def gear(self):
            from mastapy.system_model.part_model.gears import _2509
            
            return self._parent._cast(_2509.Gear)

        @property
        def gear_set(self):
            from mastapy.system_model.part_model.gears import _2511
            
            return self._parent._cast(_2511.GearSet)

        @property
        def hypoid_gear(self):
            from mastapy.system_model.part_model.gears import _2513
            
            return self._parent._cast(_2513.HypoidGear)

        @property
        def hypoid_gear_set(self):
            from mastapy.system_model.part_model.gears import _2514
            
            return self._parent._cast(_2514.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(self):
            from mastapy.system_model.part_model.gears import _2515
            
            return self._parent._cast(_2515.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2516
            
            return self._parent._cast(_2516.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(self):
            from mastapy.system_model.part_model.gears import _2517
            
            return self._parent._cast(_2517.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(self):
            from mastapy.system_model.part_model.gears import _2518
            
            return self._parent._cast(_2518.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2519
            
            return self._parent._cast(_2519.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2520
            
            return self._parent._cast(_2520.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(self):
            from mastapy.system_model.part_model.gears import _2521
            
            return self._parent._cast(_2521.PlanetaryGearSet)

        @property
        def spiral_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2522
            
            return self._parent._cast(_2522.SpiralBevelGear)

        @property
        def spiral_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2523
            
            return self._parent._cast(_2523.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear(self):
            from mastapy.system_model.part_model.gears import _2524
            
            return self._parent._cast(_2524.StraightBevelDiffGear)

        @property
        def straight_bevel_diff_gear_set(self):
            from mastapy.system_model.part_model.gears import _2525
            
            return self._parent._cast(_2525.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2526
            
            return self._parent._cast(_2526.StraightBevelGear)

        @property
        def straight_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2527
            
            return self._parent._cast(_2527.StraightBevelGearSet)

        @property
        def straight_bevel_planet_gear(self):
            from mastapy.system_model.part_model.gears import _2528
            
            return self._parent._cast(_2528.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(self):
            from mastapy.system_model.part_model.gears import _2529
            
            return self._parent._cast(_2529.StraightBevelSunGear)

        @property
        def worm_gear(self):
            from mastapy.system_model.part_model.gears import _2530
            
            return self._parent._cast(_2530.WormGear)

        @property
        def worm_gear_set(self):
            from mastapy.system_model.part_model.gears import _2531
            
            return self._parent._cast(_2531.WormGearSet)

        @property
        def zerol_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2532
            
            return self._parent._cast(_2532.ZerolBevelGear)

        @property
        def zerol_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2533
            
            return self._parent._cast(_2533.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(self):
            from mastapy.system_model.part_model.cycloidal import _2547
            
            return self._parent._cast(_2547.CycloidalAssembly)

        @property
        def cycloidal_disc(self):
            from mastapy.system_model.part_model.cycloidal import _2548
            
            return self._parent._cast(_2548.CycloidalDisc)

        @property
        def ring_pins(self):
            from mastapy.system_model.part_model.cycloidal import _2549
            
            return self._parent._cast(_2549.RingPins)

        @property
        def belt_drive(self):
            from mastapy.system_model.part_model.couplings import _2555
            
            return self._parent._cast(_2555.BeltDrive)

        @property
        def clutch(self):
            from mastapy.system_model.part_model.couplings import _2557
            
            return self._parent._cast(_2557.Clutch)

        @property
        def clutch_half(self):
            from mastapy.system_model.part_model.couplings import _2558
            
            return self._parent._cast(_2558.ClutchHalf)

        @property
        def concept_coupling(self):
            from mastapy.system_model.part_model.couplings import _2560
            
            return self._parent._cast(_2560.ConceptCoupling)

        @property
        def concept_coupling_half(self):
            from mastapy.system_model.part_model.couplings import _2561
            
            return self._parent._cast(_2561.ConceptCouplingHalf)

        @property
        def coupling(self):
            from mastapy.system_model.part_model.couplings import _2562
            
            return self._parent._cast(_2562.Coupling)

        @property
        def coupling_half(self):
            from mastapy.system_model.part_model.couplings import _2563
            
            return self._parent._cast(_2563.CouplingHalf)

        @property
        def cvt(self):
            from mastapy.system_model.part_model.couplings import _2565
            
            return self._parent._cast(_2565.CVT)

        @property
        def cvt_pulley(self):
            from mastapy.system_model.part_model.couplings import _2566
            
            return self._parent._cast(_2566.CVTPulley)

        @property
        def part_to_part_shear_coupling(self):
            from mastapy.system_model.part_model.couplings import _2567
            
            return self._parent._cast(_2567.PartToPartShearCoupling)

        @property
        def part_to_part_shear_coupling_half(self):
            from mastapy.system_model.part_model.couplings import _2568
            
            return self._parent._cast(_2568.PartToPartShearCouplingHalf)

        @property
        def pulley(self):
            from mastapy.system_model.part_model.couplings import _2569
            
            return self._parent._cast(_2569.Pulley)

        @property
        def rolling_ring(self):
            from mastapy.system_model.part_model.couplings import _2575
            
            return self._parent._cast(_2575.RollingRing)

        @property
        def rolling_ring_assembly(self):
            from mastapy.system_model.part_model.couplings import _2576
            
            return self._parent._cast(_2576.RollingRingAssembly)

        @property
        def shaft_hub_connection(self):
            from mastapy.system_model.part_model.couplings import _2577
            
            return self._parent._cast(_2577.ShaftHubConnection)

        @property
        def spring_damper(self):
            from mastapy.system_model.part_model.couplings import _2579
            
            return self._parent._cast(_2579.SpringDamper)

        @property
        def spring_damper_half(self):
            from mastapy.system_model.part_model.couplings import _2580
            
            return self._parent._cast(_2580.SpringDamperHalf)

        @property
        def synchroniser(self):
            from mastapy.system_model.part_model.couplings import _2581
            
            return self._parent._cast(_2581.Synchroniser)

        @property
        def synchroniser_half(self):
            from mastapy.system_model.part_model.couplings import _2583
            
            return self._parent._cast(_2583.SynchroniserHalf)

        @property
        def synchroniser_part(self):
            from mastapy.system_model.part_model.couplings import _2584
            
            return self._parent._cast(_2584.SynchroniserPart)

        @property
        def synchroniser_sleeve(self):
            from mastapy.system_model.part_model.couplings import _2585
            
            return self._parent._cast(_2585.SynchroniserSleeve)

        @property
        def torque_converter(self):
            from mastapy.system_model.part_model.couplings import _2586
            
            return self._parent._cast(_2586.TorqueConverter)

        @property
        def torque_converter_pump(self):
            from mastapy.system_model.part_model.couplings import _2587
            
            return self._parent._cast(_2587.TorqueConverterPump)

        @property
        def torque_converter_turbine(self):
            from mastapy.system_model.part_model.couplings import _2589
            
            return self._parent._cast(_2589.TorqueConverterTurbine)

        @property
        def part(self) -> 'Part':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Part.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing(self) -> 'Image':
        """Image: 'TwoDDrawing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TwoDDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def three_d_isometric_view(self) -> 'Image':
        """Image: 'ThreeDIsometricView' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThreeDIsometricView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def three_d_view(self) -> 'Image':
        """Image: 'ThreeDView' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThreeDView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_into_the_screen(self) -> 'Image':
        """Image: 'ThreeDViewOrientatedInXyPlaneWithZAxisPointingIntoTheScreen' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThreeDViewOrientatedInXyPlaneWithZAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_out_of_the_screen(self) -> 'Image':
        """Image: 'ThreeDViewOrientatedInXyPlaneWithZAxisPointingOutOfTheScreen' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThreeDViewOrientatedInXyPlaneWithZAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_into_the_screen(self) -> 'Image':
        """Image: 'ThreeDViewOrientatedInXzPlaneWithYAxisPointingIntoTheScreen' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThreeDViewOrientatedInXzPlaneWithYAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_out_of_the_screen(self) -> 'Image':
        """Image: 'ThreeDViewOrientatedInXzPlaneWithYAxisPointingOutOfTheScreen' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThreeDViewOrientatedInXzPlaneWithYAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_into_the_screen(self) -> 'Image':
        """Image: 'ThreeDViewOrientatedInYzPlaneWithXAxisPointingIntoTheScreen' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThreeDViewOrientatedInYzPlaneWithXAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_out_of_the_screen(self) -> 'Image':
        """Image: 'ThreeDViewOrientatedInYzPlaneWithXAxisPointingOutOfTheScreen' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThreeDViewOrientatedInYzPlaneWithXAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def drawing_number(self) -> 'str':
        """str: 'DrawingNumber' is the original name of this property."""

        temp = self.wrapped.DrawingNumber

        if temp is None:
            return ''

        return temp

    @drawing_number.setter
    def drawing_number(self, value: 'str'):
        self.wrapped.DrawingNumber = str(value) if value else ''

    @property
    def editable_name(self) -> 'str':
        """str: 'EditableName' is the original name of this property."""

        temp = self.wrapped.EditableName

        if temp is None:
            return ''

        return temp

    @editable_name.setter
    def editable_name(self, value: 'str'):
        self.wrapped.EditableName = str(value) if value else ''

    @property
    def mass(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Mass' is the original name of this property."""

        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @mass.setter
    def mass(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Mass = value

    @property
    def unique_name(self) -> 'str':
        """str: 'UniqueName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UniqueName

        if temp is None:
            return ''

        return temp

    @property
    def mass_properties_from_design(self) -> '_1506.MassProperties':
        """MassProperties: 'MassPropertiesFromDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassPropertiesFromDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mass_properties_from_design_including_planetary_duplicates(self) -> '_1506.MassProperties':
        """MassProperties: 'MassPropertiesFromDesignIncludingPlanetaryDuplicates' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassPropertiesFromDesignIncludingPlanetaryDuplicates

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connections(self) -> 'List[_2253.Connection]':
        """List[Connection]: 'Connections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def local_connections(self) -> 'List[_2253.Connection]':
        """List[Connection]: 'LocalConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LocalConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def connections_to(self, part: 'Part') -> 'List[_2253.Connection]':
        """ 'ConnectionsTo' is the original name of this method.

        Args:
            part (mastapy.system_model.part_model.Part)

        Returns:
            List[mastapy.system_model.connections_and_sockets.Connection]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionsTo(part.wrapped if part else None))

    def copy_to(self, container: '_2413.Assembly') -> 'Part':
        """ 'CopyTo' is the original name of this method.

        Args:
            container (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.part_model.Part
        """

        method_result = self.wrapped.CopyTo(container.wrapped if container else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_geometry_export_options(self) -> '_2223.GeometryExportOptions':
        """ 'CreateGeometryExportOptions' is the original name of this method.

        Returns:
            mastapy.system_model.import_export.GeometryExportOptions
        """

        method_result = self.wrapped.CreateGeometryExportOptions()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def delete_connections(self):
        """ 'DeleteConnections' is the original name of this method."""

        self.wrapped.DeleteConnections()

    @property
    def cast_to(self) -> 'Part._Cast_Part':
        return self._Cast_Part(self)
