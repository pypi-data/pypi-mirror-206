"""_959.py

StraightBevelMeshedGearDesign
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.bevel import _1177
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_MESHED_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.StraightBevel', 'StraightBevelMeshedGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelMeshedGearDesign',)


class StraightBevelMeshedGearDesign(_1177.BevelMeshedGearDesign):
    """StraightBevelMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_MESHED_GEAR_DESIGN

    class _Cast_StraightBevelMeshedGearDesign:
        """Special nested class for casting StraightBevelMeshedGearDesign to subclasses."""

        def __init__(self, parent: 'StraightBevelMeshedGearDesign'):
            self._parent = parent

        @property
        def bevel_meshed_gear_design(self):
            return self._parent._cast(_1177.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1190
            
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
        def straight_bevel_meshed_gear_design(self) -> 'StraightBevelMeshedGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelMeshedGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometry_factor_j(self) -> 'float':
        """float: 'GeometryFactorJ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryFactorJ

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_factor(self) -> 'float':
        """float: 'StrengthFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrengthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'StraightBevelMeshedGearDesign._Cast_StraightBevelMeshedGearDesign':
        return self._Cast_StraightBevelMeshedGearDesign(self)
