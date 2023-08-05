"""_2529.py

StraightBevelSunGear
"""
from mastapy.system_model.part_model.gears import _2524
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelSunGear')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelSunGear',)


class StraightBevelSunGear(_2524.StraightBevelDiffGear):
    """StraightBevelSunGear

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR

    class _Cast_StraightBevelSunGear:
        """Special nested class for casting StraightBevelSunGear to subclasses."""

        def __init__(self, parent: 'StraightBevelSunGear'):
            self._parent = parent

        @property
        def straight_bevel_diff_gear(self):
            return self._parent._cast(_2524.StraightBevelDiffGear)

        @property
        def bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2498
            
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
        def straight_bevel_sun_gear(self) -> 'StraightBevelSunGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelSunGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'StraightBevelSunGear._Cast_StraightBevelSunGear':
        return self._Cast_StraightBevelSunGear(self)
