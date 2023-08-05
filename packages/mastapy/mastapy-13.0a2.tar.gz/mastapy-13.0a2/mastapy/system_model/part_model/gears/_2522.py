"""_2522.py

SpiralBevelGear
"""
from mastapy.gears.gear_designs.spiral_bevel import _964
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2498
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'SpiralBevelGear')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGear',)


class SpiralBevelGear(_2498.BevelGear):
    """SpiralBevelGear

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR

    class _Cast_SpiralBevelGear:
        """Special nested class for casting SpiralBevelGear to subclasses."""

        def __init__(self, parent: 'SpiralBevelGear'):
            self._parent = parent

        @property
        def bevel_gear(self):
            return self._parent._cast(_2498.BevelGear)

        @property
        def agma_gleason_conical_gear(self):
            from mastapy.system_model.part_model.gears import _2492
            
            return self._parent._cast(_2492.AGMAGleasonConicalGear)

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
        def spiral_bevel_gear(self) -> 'SpiralBevelGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_design(self) -> '_964.SpiralBevelGearDesign':
        """SpiralBevelGearDesign: 'BevelGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spiral_bevel_gear_design(self) -> '_964.SpiralBevelGearDesign':
        """SpiralBevelGearDesign: 'SpiralBevelGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SpiralBevelGear._Cast_SpiralBevelGear':
        return self._Cast_SpiralBevelGear(self)
