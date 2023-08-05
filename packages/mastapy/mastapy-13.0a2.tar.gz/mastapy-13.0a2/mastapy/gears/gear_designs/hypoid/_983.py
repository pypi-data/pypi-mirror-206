"""_983.py

HypoidMeshedGearDesign
"""
from mastapy.gears.gear_designs.agma_gleason_conical import _1190
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_MESHED_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Hypoid', 'HypoidMeshedGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidMeshedGearDesign',)


class HypoidMeshedGearDesign(_1190.AGMAGleasonConicalMeshedGearDesign):
    """HypoidMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _HYPOID_MESHED_GEAR_DESIGN

    class _Cast_HypoidMeshedGearDesign:
        """Special nested class for casting HypoidMeshedGearDesign to subclasses."""

        def __init__(self, parent: 'HypoidMeshedGearDesign'):
            self._parent = parent

        @property
        def agma_gleason_conical_meshed_gear_design(self):
            return self._parent._cast(_1190.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(self):
            from mastapy.gears.gear_designs.conical import _1153
            
            return self._parent._cast(_1153.ConicalMeshedGearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def hypoid_meshed_gear_design(self) -> 'HypoidMeshedGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidMeshedGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HypoidMeshedGearDesign._Cast_HypoidMeshedGearDesign':
        return self._Cast_HypoidMeshedGearDesign(self)
