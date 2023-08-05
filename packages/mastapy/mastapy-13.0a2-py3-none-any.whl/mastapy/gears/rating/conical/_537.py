"""_537.py

ConicalGearSetRating
"""
from mastapy.gears.gear_designs import _938
from mastapy._internal import constructor
from mastapy.gears.rating import _359
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetRating',)


class ConicalGearSetRating(_359.GearSetRating):
    """ConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_RATING

    class _Cast_ConicalGearSetRating:
        """Special nested class for casting ConicalGearSetRating to subclasses."""

        def __init__(self, parent: 'ConicalGearSetRating'):
            self._parent = parent

        @property
        def gear_set_rating(self):
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
        def straight_bevel_diff_gear_set_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _396
            
            return self._parent._cast(_396.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(self):
            from mastapy.gears.rating.spiral_bevel import _400
            
            return self._parent._cast(_400.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _403
            
            return self._parent._cast(_403.KlingelnbergCycloPalloidSpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _406
            
            return self._parent._cast(_406.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_conical import _409
            
            return self._parent._cast(_409.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(self):
            from mastapy.gears.rating.hypoid import _436
            
            return self._parent._cast(_436.HypoidGearSetRating)

        @property
        def bevel_gear_set_rating(self):
            from mastapy.gears.rating.bevel import _551
            
            return self._parent._cast(_551.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _562
            
            return self._parent._cast(_562.AGMAGleasonConicalGearSetRating)

        @property
        def conical_gear_set_rating(self) -> 'ConicalGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating_settings(self) -> '_938.BevelHypoidGearRatingSettingsItem':
        """BevelHypoidGearRatingSettingsItem: 'RatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearSetRating._Cast_ConicalGearSetRating':
        return self._Cast_ConicalGearSetRating(self)
