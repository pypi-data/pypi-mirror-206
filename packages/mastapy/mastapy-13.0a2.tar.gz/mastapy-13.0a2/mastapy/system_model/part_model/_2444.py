"""_2444.py

MountableComponent
"""
from typing import Optional

from mastapy._internal import constructor
from mastapy.system_model.part_model import _2415, _2425, _2424
from mastapy.system_model.connections_and_sockets import _2253, _2257, _2250
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MountableComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponent',)


class MountableComponent(_2424.Component):
    """MountableComponent

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT

    class _Cast_MountableComponent:
        """Special nested class for casting MountableComponent to subclasses."""

        def __init__(self, parent: 'MountableComponent'):
            self._parent = parent

        @property
        def component(self):
            return self._parent._cast(_2424.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def bearing(self):
            from mastapy.system_model.part_model import _2419
            
            return self._parent._cast(_2419.Bearing)

        @property
        def connector(self):
            from mastapy.system_model.part_model import _2427
            
            return self._parent._cast(_2427.Connector)

        @property
        def mass_disc(self):
            from mastapy.system_model.part_model import _2442
            
            return self._parent._cast(_2442.MassDisc)

        @property
        def measurement_component(self):
            from mastapy.system_model.part_model import _2443
            
            return self._parent._cast(_2443.MeasurementComponent)

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
        def unbalanced_mass(self):
            from mastapy.system_model.part_model import _2457
            
            return self._parent._cast(_2457.UnbalancedMass)

        @property
        def virtual_component(self):
            from mastapy.system_model.part_model import _2459
            
            return self._parent._cast(_2459.VirtualComponent)

        @property
        def agma_gleason_conical_gear(self):
            from mastapy.system_model.part_model.gears import _2492
            
            return self._parent._cast(_2492.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(self):
            from mastapy.system_model.part_model.gears import _2494
            
            return self._parent._cast(_2494.BevelDifferentialGear)

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
        def concept_gear(self):
            from mastapy.system_model.part_model.gears import _2500
            
            return self._parent._cast(_2500.ConceptGear)

        @property
        def conical_gear(self):
            from mastapy.system_model.part_model.gears import _2502
            
            return self._parent._cast(_2502.ConicalGear)

        @property
        def cylindrical_gear(self):
            from mastapy.system_model.part_model.gears import _2504
            
            return self._parent._cast(_2504.CylindricalGear)

        @property
        def cylindrical_planet_gear(self):
            from mastapy.system_model.part_model.gears import _2506
            
            return self._parent._cast(_2506.CylindricalPlanetGear)

        @property
        def face_gear(self):
            from mastapy.system_model.part_model.gears import _2507
            
            return self._parent._cast(_2507.FaceGear)

        @property
        def gear(self):
            from mastapy.system_model.part_model.gears import _2509
            
            return self._parent._cast(_2509.Gear)

        @property
        def hypoid_gear(self):
            from mastapy.system_model.part_model.gears import _2513
            
            return self._parent._cast(_2513.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(self):
            from mastapy.system_model.part_model.gears import _2515
            
            return self._parent._cast(_2515.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(self):
            from mastapy.system_model.part_model.gears import _2517
            
            return self._parent._cast(_2517.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2519
            
            return self._parent._cast(_2519.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2522
            
            return self._parent._cast(_2522.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(self):
            from mastapy.system_model.part_model.gears import _2524
            
            return self._parent._cast(_2524.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2526
            
            return self._parent._cast(_2526.StraightBevelGear)

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
        def zerol_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2532
            
            return self._parent._cast(_2532.ZerolBevelGear)

        @property
        def ring_pins(self):
            from mastapy.system_model.part_model.cycloidal import _2549
            
            return self._parent._cast(_2549.RingPins)

        @property
        def clutch_half(self):
            from mastapy.system_model.part_model.couplings import _2558
            
            return self._parent._cast(_2558.ClutchHalf)

        @property
        def concept_coupling_half(self):
            from mastapy.system_model.part_model.couplings import _2561
            
            return self._parent._cast(_2561.ConceptCouplingHalf)

        @property
        def coupling_half(self):
            from mastapy.system_model.part_model.couplings import _2563
            
            return self._parent._cast(_2563.CouplingHalf)

        @property
        def cvt_pulley(self):
            from mastapy.system_model.part_model.couplings import _2566
            
            return self._parent._cast(_2566.CVTPulley)

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
        def shaft_hub_connection(self):
            from mastapy.system_model.part_model.couplings import _2577
            
            return self._parent._cast(_2577.ShaftHubConnection)

        @property
        def spring_damper_half(self):
            from mastapy.system_model.part_model.couplings import _2580
            
            return self._parent._cast(_2580.SpringDamperHalf)

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
        def torque_converter_pump(self):
            from mastapy.system_model.part_model.couplings import _2587
            
            return self._parent._cast(_2587.TorqueConverterPump)

        @property
        def torque_converter_turbine(self):
            from mastapy.system_model.part_model.couplings import _2589
            
            return self._parent._cast(_2589.TorqueConverterTurbine)

        @property
        def mountable_component(self) -> 'MountableComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotation_about_axis(self) -> 'float':
        """float: 'RotationAboutAxis' is the original name of this property."""

        temp = self.wrapped.RotationAboutAxis

        if temp is None:
            return 0.0

        return temp

    @rotation_about_axis.setter
    def rotation_about_axis(self, value: 'float'):
        self.wrapped.RotationAboutAxis = float(value) if value else 0.0

    @property
    def inner_component(self) -> '_2415.AbstractShaft':
        """AbstractShaft: 'InnerComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection(self) -> '_2253.Connection':
        """Connection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket(self) -> '_2257.CylindricalSocket':
        """CylindricalSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def is_mounted(self) -> 'bool':
        """bool: 'IsMounted' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsMounted

        if temp is None:
            return False

        return temp

    def mount_on(self, shaft: '_2415.AbstractShaft', offset: Optional['float'] = float('nan')) -> '_2250.CoaxialConnection':
        """ 'MountOn' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.connections_and_sockets.CoaxialConnection
        """

        offset = float(offset)
        method_result = self.wrapped.MountOn(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def try_mount_on(self, shaft: '_2415.AbstractShaft', offset: Optional['float'] = float('nan')) -> '_2425.ComponentsConnectedResult':
        """ 'TryMountOn' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        offset = float(offset)
        method_result = self.wrapped.TryMountOn(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'MountableComponent._Cast_MountableComponent':
        return self._Cast_MountableComponent(self)
