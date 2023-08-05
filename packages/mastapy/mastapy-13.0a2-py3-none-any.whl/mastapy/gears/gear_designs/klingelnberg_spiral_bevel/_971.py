"""_971.py

KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
"""
from mastapy.gears.gear_designs.klingelnberg_conical import _979
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_MESHED_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.KlingelnbergSpiralBevel', 'KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign',)


class KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign(_979.KlingelnbergConicalMeshedGearDesign):
    """KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_MESHED_GEAR_DESIGN

    class _Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign'):
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
        def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gear_design(self) -> 'KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign(self)
