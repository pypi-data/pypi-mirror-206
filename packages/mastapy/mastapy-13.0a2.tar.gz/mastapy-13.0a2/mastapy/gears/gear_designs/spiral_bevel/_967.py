"""_967.py

SpiralBevelMeshedGearDesign
"""
from mastapy._math.vector_2d import Vector2D
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1177
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_MESHED_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.SpiralBevel', 'SpiralBevelMeshedGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelMeshedGearDesign',)


class SpiralBevelMeshedGearDesign(_1177.BevelMeshedGearDesign):
    """SpiralBevelMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_MESHED_GEAR_DESIGN

    class _Cast_SpiralBevelMeshedGearDesign:
        """Special nested class for casting SpiralBevelMeshedGearDesign to subclasses."""

        def __init__(self, parent: 'SpiralBevelMeshedGearDesign'):
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
        def spiral_bevel_meshed_gear_design(self) -> 'SpiralBevelMeshedGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelMeshedGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def tip_point_at_mean_section(self) -> 'Vector2D':
        """Vector2D: 'TipPointAtMeanSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipPointAtMeanSection

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def tip_thickness_at_mean_section(self) -> 'float':
        """float: 'TipThicknessAtMeanSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipThicknessAtMeanSection

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'SpiralBevelMeshedGearDesign._Cast_SpiralBevelMeshedGearDesign':
        return self._Cast_SpiralBevelMeshedGearDesign(self)
