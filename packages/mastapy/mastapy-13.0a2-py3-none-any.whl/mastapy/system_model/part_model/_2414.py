"""_2414.py

AbstractAssembly
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2424, _2448
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractAssembly')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssembly',)


class AbstractAssembly(_2448.Part):
    """AbstractAssembly

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY

    class _Cast_AbstractAssembly:
        """Special nested class for casting AbstractAssembly to subclasses."""

        def __init__(self, parent: 'AbstractAssembly'):
            self._parent = parent

        @property
        def part(self):
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def assembly(self):
            from mastapy.system_model.part_model import _2413
            
            return self._parent._cast(_2413.Assembly)

        @property
        def bolted_joint(self):
            from mastapy.system_model.part_model import _2423
            
            return self._parent._cast(_2423.BoltedJoint)

        @property
        def flexible_pin_assembly(self):
            from mastapy.system_model.part_model import _2434
            
            return self._parent._cast(_2434.FlexiblePinAssembly)

        @property
        def root_assembly(self):
            from mastapy.system_model.part_model import _2454
            
            return self._parent._cast(_2454.RootAssembly)

        @property
        def specialised_assembly(self):
            from mastapy.system_model.part_model import _2456
            
            return self._parent._cast(_2456.SpecialisedAssembly)

        @property
        def agma_gleason_conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2493
            
            return self._parent._cast(_2493.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear_set(self):
            from mastapy.system_model.part_model.gears import _2495
            
            return self._parent._cast(_2495.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2499
            
            return self._parent._cast(_2499.BevelGearSet)

        @property
        def concept_gear_set(self):
            from mastapy.system_model.part_model.gears import _2501
            
            return self._parent._cast(_2501.ConceptGearSet)

        @property
        def conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2503
            
            return self._parent._cast(_2503.ConicalGearSet)

        @property
        def cylindrical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2505
            
            return self._parent._cast(_2505.CylindricalGearSet)

        @property
        def face_gear_set(self):
            from mastapy.system_model.part_model.gears import _2508
            
            return self._parent._cast(_2508.FaceGearSet)

        @property
        def gear_set(self):
            from mastapy.system_model.part_model.gears import _2511
            
            return self._parent._cast(_2511.GearSet)

        @property
        def hypoid_gear_set(self):
            from mastapy.system_model.part_model.gears import _2514
            
            return self._parent._cast(_2514.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2516
            
            return self._parent._cast(_2516.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(self):
            from mastapy.system_model.part_model.gears import _2518
            
            return self._parent._cast(_2518.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2520
            
            return self._parent._cast(_2520.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(self):
            from mastapy.system_model.part_model.gears import _2521
            
            return self._parent._cast(_2521.PlanetaryGearSet)

        @property
        def spiral_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2523
            
            return self._parent._cast(_2523.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(self):
            from mastapy.system_model.part_model.gears import _2525
            
            return self._parent._cast(_2525.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2527
            
            return self._parent._cast(_2527.StraightBevelGearSet)

        @property
        def worm_gear_set(self):
            from mastapy.system_model.part_model.gears import _2531
            
            return self._parent._cast(_2531.WormGearSet)

        @property
        def zerol_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2533
            
            return self._parent._cast(_2533.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(self):
            from mastapy.system_model.part_model.cycloidal import _2547
            
            return self._parent._cast(_2547.CycloidalAssembly)

        @property
        def belt_drive(self):
            from mastapy.system_model.part_model.couplings import _2555
            
            return self._parent._cast(_2555.BeltDrive)

        @property
        def clutch(self):
            from mastapy.system_model.part_model.couplings import _2557
            
            return self._parent._cast(_2557.Clutch)

        @property
        def concept_coupling(self):
            from mastapy.system_model.part_model.couplings import _2560
            
            return self._parent._cast(_2560.ConceptCoupling)

        @property
        def coupling(self):
            from mastapy.system_model.part_model.couplings import _2562
            
            return self._parent._cast(_2562.Coupling)

        @property
        def cvt(self):
            from mastapy.system_model.part_model.couplings import _2565
            
            return self._parent._cast(_2565.CVT)

        @property
        def part_to_part_shear_coupling(self):
            from mastapy.system_model.part_model.couplings import _2567
            
            return self._parent._cast(_2567.PartToPartShearCoupling)

        @property
        def rolling_ring_assembly(self):
            from mastapy.system_model.part_model.couplings import _2576
            
            return self._parent._cast(_2576.RollingRingAssembly)

        @property
        def spring_damper(self):
            from mastapy.system_model.part_model.couplings import _2579
            
            return self._parent._cast(_2579.SpringDamper)

        @property
        def synchroniser(self):
            from mastapy.system_model.part_model.couplings import _2581
            
            return self._parent._cast(_2581.Synchroniser)

        @property
        def torque_converter(self):
            from mastapy.system_model.part_model.couplings import _2586
            
            return self._parent._cast(_2586.TorqueConverter)

        @property
        def abstract_assembly(self) -> 'AbstractAssembly':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssembly.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mass_of_assembly(self) -> 'float':
        """float: 'MassOfAssembly' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassOfAssembly

        if temp is None:
            return 0.0

        return temp

    @property
    def components_with_unknown_mass_properties(self) -> 'List[_2424.Component]':
        """List[Component]: 'ComponentsWithUnknownMassProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentsWithUnknownMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def components_with_zero_mass_properties(self) -> 'List[_2424.Component]':
        """List[Component]: 'ComponentsWithZeroMassProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentsWithZeroMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractAssembly._Cast_AbstractAssembly':
        return self._Cast_AbstractAssembly(self)
