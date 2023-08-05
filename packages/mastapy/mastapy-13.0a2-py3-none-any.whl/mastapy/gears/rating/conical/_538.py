"""_538.py

ConicalGearSingleFlankRating
"""
from mastapy.gears.rating import _360
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalGearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSingleFlankRating',)


class ConicalGearSingleFlankRating(_360.GearSingleFlankRating):
    """ConicalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SINGLE_FLANK_RATING

    class _Cast_ConicalGearSingleFlankRating:
        """Special nested class for casting ConicalGearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'ConicalGearSingleFlankRating'):
            self._parent = parent

        @property
        def gear_single_flank_rating(self):
            return self._parent._cast(_360.GearSingleFlankRating)

        @property
        def iso10300_single_flank_rating(self):
            from mastapy.gears.rating.iso_10300 import _425
            
            return self._parent._cast(_425.ISO10300SingleFlankRating)

        @property
        def iso10300_single_flank_rating_bevel_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _426
            
            return self._parent._cast(_426.ISO10300SingleFlankRatingBevelMethodB2)

        @property
        def iso10300_single_flank_rating_hypoid_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _427
            
            return self._parent._cast(_427.ISO10300SingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_single_flank_rating_method_b1(self):
            from mastapy.gears.rating.iso_10300 import _428
            
            return self._parent._cast(_428.ISO10300SingleFlankRatingMethodB1)

        @property
        def iso10300_single_flank_rating_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _429
            
            return self._parent._cast(_429.ISO10300SingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_gear_single_flank_rating(self):
            from mastapy.gears.rating.hypoid.standards import _438
            
            return self._parent._cast(_438.GleasonHypoidGearSingleFlankRating)

        @property
        def agma_spiral_bevel_gear_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _552
            
            return self._parent._cast(_552.AGMASpiralBevelGearSingleFlankRating)

        @property
        def gleason_spiral_bevel_gear_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _554
            
            return self._parent._cast(_554.GleasonSpiralBevelGearSingleFlankRating)

        @property
        def spiral_bevel_gear_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _556
            
            return self._parent._cast(_556.SpiralBevelGearSingleFlankRating)

        @property
        def conical_gear_single_flank_rating(self) -> 'ConicalGearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating':
        return self._Cast_ConicalGearSingleFlankRating(self)
