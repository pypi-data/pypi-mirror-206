"""_2519.py

KlingelnbergCycloPalloidSpiralBevelGear
"""
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _968
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGear')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGear',)


class KlingelnbergCycloPalloidSpiralBevelGear(_2515.KlingelnbergCycloPalloidConicalGear):
    """KlingelnbergCycloPalloidSpiralBevelGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGear:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGear to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelGear'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear(self):
            return self._parent._cast(_2515.KlingelnbergCycloPalloidConicalGear)

        @property
        def conical_gear(self):
            from mastapy.system_model.part_model.gears import _2502
            
            return self._parent._cast(_2502.ConicalGear)

        @property
        def gear(self):
            from mastapy.system_model.part_model.gears import _2509
            
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
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> 'KlingelnbergCycloPalloidSpiralBevelGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_design(self) -> '_968.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_968.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearDesign: 'KlingelnbergCycloPalloidSpiralBevelGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGear(self)
