"""_975.py

KlingelnbergCycloPalloidHypoidMeshedGearDesign
"""
from mastapy.gears.gear_designs.klingelnberg_conical import _979
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_MESHED_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.KlingelnbergHypoid', 'KlingelnbergCycloPalloidHypoidMeshedGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidMeshedGearDesign',)


class KlingelnbergCycloPalloidHypoidMeshedGearDesign(_979.KlingelnbergConicalMeshedGearDesign):
    """KlingelnbergCycloPalloidHypoidMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_MESHED_GEAR_DESIGN

    class _Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidMeshedGearDesign to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidMeshedGearDesign'):
            self._parent = parent

        @property
        def klingelnberg_conical_meshed_gear_design(self):
            return self._parent._cast(_979.KlingelnbergConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(self):
            from mastapy.gears.gear_designs.conical import _1153
            
            return self._parent._cast(_1153.ConicalMeshedGearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(self) -> 'KlingelnbergCycloPalloidHypoidMeshedGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidMeshedGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidMeshedGearDesign._Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign':
        return self._Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign(self)
