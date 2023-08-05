"""_562.py

AGMAGleasonConicalGearSetRating
"""
from mastapy.gears.rating.conical import _537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.AGMAGleasonConical', 'AGMAGleasonConicalGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearSetRating',)


class AGMAGleasonConicalGearSetRating(_537.ConicalGearSetRating):
    """AGMAGleasonConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_RATING

    class _Cast_AGMAGleasonConicalGearSetRating:
        """Special nested class for casting AGMAGleasonConicalGearSetRating to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearSetRating'):
            self._parent = parent

        @property
        def conical_gear_set_rating(self):
            return self._parent._cast(_537.ConicalGearSetRating)

        @property
        def gear_set_rating(self):
            from mastapy.gears.rating import _359
            
            return self._parent._cast(_359.GearSetRating)

        @property
        def abstract_gear_set_rating(self):
            from mastapy.gears.rating import _351
            
            return self._parent._cast(_351.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def zerol_bevel_gear_set_rating(self):
            from mastapy.gears.rating.zerol_bevel import _367
            
            return self._parent._cast(_367.ZerolBevelGearSetRating)

        @property
        def straight_bevel_gear_set_rating(self):
            from mastapy.gears.rating.straight_bevel import _393
            
            return self._parent._cast(_393.StraightBevelGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(self):
            from mastapy.gears.rating.spiral_bevel import _400
            
            return self._parent._cast(_400.SpiralBevelGearSetRating)

        @property
        def hypoid_gear_set_rating(self):
            from mastapy.gears.rating.hypoid import _436
            
            return self._parent._cast(_436.HypoidGearSetRating)

        @property
        def bevel_gear_set_rating(self):
            from mastapy.gears.rating.bevel import _551
            
            return self._parent._cast(_551.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(self) -> 'AGMAGleasonConicalGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating':
        return self._Cast_AGMAGleasonConicalGearSetRating(self)
