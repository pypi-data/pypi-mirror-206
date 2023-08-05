"""_2502.py

ConicalGear
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.part_model.gears import _2510, _2509
from mastapy.gears.gear_designs.conical import _1148
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGear')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGear',)


class ConicalGear(_2509.Gear):
    """ConicalGear

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR

    class _Cast_ConicalGear:
        """Special nested class for casting ConicalGear to subclasses."""

        def __init__(self, parent: 'ConicalGear'):
            self._parent = parent

        @property
        def gear(self):
            return self._parent._cast(_2509.Gear)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2444
            
            return self._parent._cast(_2444.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2424
            
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
        def zerol_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2532
            
            return self._parent._cast(_2532.ZerolBevelGear)

        @property
        def conical_gear(self) -> 'ConicalGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @property
    def orientation(self) -> '_2510.GearOrientations':
        """GearOrientations: 'Orientation' is the original name of this property."""

        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _2510.GearOrientations)
        return constructor.new_from_mastapy_type(_2510.GearOrientations)(value) if value is not None else None

    @orientation.setter
    def orientation(self, value: '_2510.GearOrientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _2510.GearOrientations.type_())
        self.wrapped.Orientation = value

    @property
    def active_gear_design(self) -> '_1148.ConicalGearDesign':
        """ConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_design(self) -> '_1148.ConicalGearDesign':
        """ConicalGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGear._Cast_ConicalGear':
        return self._Cast_ConicalGear(self)
