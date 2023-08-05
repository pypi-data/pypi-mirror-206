"""_2188.py

DesignEntity
"""
from typing import List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model import _2185
from mastapy.utility.model_validation import _1783, _1782
from mastapy.utility.scripting import _1730
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY = python_net_import('SMT.MastaAPI.SystemModel', 'DesignEntity')


__docformat__ = 'restructuredtext en'
__all__ = ('DesignEntity',)


class DesignEntity(_0.APIBase):
    """DesignEntity

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY

    class _Cast_DesignEntity:
        """Special nested class for casting DesignEntity to subclasses."""

        def __init__(self, parent: 'DesignEntity'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2246
            
            return self._parent._cast(_2246.AbstractShaftToMountableComponentConnection)

        @property
        def belt_connection(self):
            from mastapy.system_model.connections_and_sockets import _2249
            
            return self._parent._cast(_2249.BeltConnection)

        @property
        def coaxial_connection(self):
            from mastapy.system_model.connections_and_sockets import _2250
            
            return self._parent._cast(_2250.CoaxialConnection)

        @property
        def connection(self):
            from mastapy.system_model.connections_and_sockets import _2253
            
            return self._parent._cast(_2253.Connection)

        @property
        def cvt_belt_connection(self):
            from mastapy.system_model.connections_and_sockets import _2254
            
            return self._parent._cast(_2254.CVTBeltConnection)

        @property
        def inter_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2262
            
            return self._parent._cast(_2262.InterMountableComponentConnection)

        @property
        def planetary_connection(self):
            from mastapy.system_model.connections_and_sockets import _2268
            
            return self._parent._cast(_2268.PlanetaryConnection)

        @property
        def rolling_ring_connection(self):
            from mastapy.system_model.connections_and_sockets import _2273
            
            return self._parent._cast(_2273.RollingRingConnection)

        @property
        def shaft_to_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2276
            
            return self._parent._cast(_2276.ShaftToMountableComponentConnection)

        @property
        def agma_gleason_conical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2280
            
            return self._parent._cast(_2280.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2282
            
            return self._parent._cast(_2282.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2284
            
            return self._parent._cast(_2284.BevelGearMesh)

        @property
        def concept_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2286
            
            return self._parent._cast(_2286.ConceptGearMesh)

        @property
        def conical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2288
            
            return self._parent._cast(_2288.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2290
            
            return self._parent._cast(_2290.CylindricalGearMesh)

        @property
        def face_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2292
            
            return self._parent._cast(_2292.FaceGearMesh)

        @property
        def gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2294
            
            return self._parent._cast(_2294.GearMesh)

        @property
        def hypoid_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2296
            
            return self._parent._cast(_2296.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2299
            
            return self._parent._cast(_2299.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2300
            
            return self._parent._cast(_2300.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2301
            
            return self._parent._cast(_2301.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2304
            
            return self._parent._cast(_2304.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2306
            
            return self._parent._cast(_2306.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2308
            
            return self._parent._cast(_2308.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2310
            
            return self._parent._cast(_2310.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2312
            
            return self._parent._cast(_2312.ZerolBevelGearMesh)

        @property
        def cycloidal_disc_central_bearing_connection(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2316
            
            return self._parent._cast(_2316.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2319
            
            return self._parent._cast(_2319.CycloidalDiscPlanetaryBearingConnection)

        @property
        def ring_pins_to_disc_connection(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2322
            
            return self._parent._cast(_2322.RingPinsToDiscConnection)

        @property
        def clutch_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2323
            
            return self._parent._cast(_2323.ClutchConnection)

        @property
        def concept_coupling_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2325
            
            return self._parent._cast(_2325.ConceptCouplingConnection)

        @property
        def coupling_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2327
            
            return self._parent._cast(_2327.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2329
            
            return self._parent._cast(_2329.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2331
            
            return self._parent._cast(_2331.SpringDamperConnection)

        @property
        def torque_converter_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2333
            
            return self._parent._cast(_2333.TorqueConverterConnection)

        @property
        def assembly(self):
            from mastapy.system_model.part_model import _2413
            
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
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

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
        def design_entity(self) -> 'DesignEntity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DesignEntity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self) -> 'str':
        """str: 'Comment' is the original name of this property."""

        temp = self.wrapped.Comment

        if temp is None:
            return ''

        return temp

    @comment.setter
    def comment(self, value: 'str'):
        self.wrapped.Comment = str(value) if value else ''

    @property
    def id(self) -> 'str':
        """str: 'ID' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ID

        if temp is None:
            return ''

        return temp

    @property
    def icon(self) -> 'Image':
        """Image: 'Icon' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Icon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def small_icon(self) -> 'Image':
        """Image: 'SmallIcon' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallIcon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

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
    def design_properties(self) -> '_2185.Design':
        """Design: 'DesignProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def all_design_entities(self) -> 'List[DesignEntity]':
        """List[DesignEntity]: 'AllDesignEntities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllDesignEntities

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def all_status_errors(self) -> 'List[_1783.StatusItem]':
        """List[StatusItem]: 'AllStatusErrors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def status(self) -> '_1782.Status':
        """Status: 'Status' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def user_specified_data(self) -> '_1730.UserSpecifiedData':
        """UserSpecifiedData: 'UserSpecifiedData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def delete(self):
        """ 'Delete' is the original name of this method."""

        self.wrapped.Delete()

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'DesignEntity._Cast_DesignEntity':
        return self._Cast_DesignEntity(self)
