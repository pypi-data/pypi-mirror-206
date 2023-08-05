"""_2515.py

KlingelnbergCycloPalloidConicalGear
"""
from mastapy.system_model.part_model.gears import _2502
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidConicalGear')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGear',)


class KlingelnbergCycloPalloidConicalGear(_2502.ConicalGear):
    """KlingelnbergCycloPalloidConicalGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR

    class _Cast_KlingelnbergCycloPalloidConicalGear:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGear to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGear'):
            self._parent = parent

        @property
        def conical_gear(self):
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
        def klingelnberg_cyclo_palloid_hypoid_gear(self):
            from mastapy.system_model.part_model.gears import _2517
            
            return self._parent._cast(_2517.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2519
            
            return self._parent._cast(_2519.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(self) -> 'KlingelnbergCycloPalloidConicalGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear':
        return self._Cast_KlingelnbergCycloPalloidConicalGear(self)
