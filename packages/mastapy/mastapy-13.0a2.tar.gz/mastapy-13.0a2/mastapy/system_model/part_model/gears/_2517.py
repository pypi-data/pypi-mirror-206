"""_2517.py

KlingelnbergCycloPalloidHypoidGear
"""
from mastapy.gears.gear_designs.klingelnberg_hypoid import _972
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidHypoidGear')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGear',)


class KlingelnbergCycloPalloidHypoidGear(_2515.KlingelnbergCycloPalloidConicalGear):
    """KlingelnbergCycloPalloidHypoidGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR

    class _Cast_KlingelnbergCycloPalloidHypoidGear:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGear to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGear'):
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
        def klingelnberg_cyclo_palloid_hypoid_gear(self) -> 'KlingelnbergCycloPalloidHypoidGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_design(self) -> '_972.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_972.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'KlingelnbergCycloPalloidHypoidGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGear._Cast_KlingelnbergCycloPalloidHypoidGear':
        return self._Cast_KlingelnbergCycloPalloidHypoidGear(self)
