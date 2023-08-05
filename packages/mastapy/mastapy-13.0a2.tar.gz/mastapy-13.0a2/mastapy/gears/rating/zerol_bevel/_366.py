"""_366.py

ZerolBevelGearRating
"""
from mastapy.gears.gear_designs.zerol_bevel import _947
from mastapy._internal import constructor
from mastapy.gears.rating.bevel import _550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.ZerolBevel', 'ZerolBevelGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearRating',)


class ZerolBevelGearRating(_550.BevelGearRating):
    """ZerolBevelGearRating

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_RATING

    class _Cast_ZerolBevelGearRating:
        """Special nested class for casting ZerolBevelGearRating to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearRating'):
            self._parent = parent

        @property
        def bevel_gear_rating(self):
            return self._parent._cast(_550.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _561
            
            return self._parent._cast(_561.AGMAGleasonConicalGearRating)

        @property
        def conical_gear_rating(self):
            from mastapy.gears.rating.conical import _535
            
            return self._parent._cast(_535.ConicalGearRating)

        @property
        def gear_rating(self):
            from mastapy.gears.rating import _357
            
            return self._parent._cast(_357.GearRating)

        @property
        def abstract_gear_rating(self):
            from mastapy.gears.rating import _350
            
            return self._parent._cast(_350.AbstractGearRating)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(self) -> 'ZerolBevelGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def zerol_bevel_gear(self) -> '_947.ZerolBevelGearDesign':
        """ZerolBevelGearDesign: 'ZerolBevelGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ZerolBevelGearRating._Cast_ZerolBevelGearRating':
        return self._Cast_ZerolBevelGearRating(self)
