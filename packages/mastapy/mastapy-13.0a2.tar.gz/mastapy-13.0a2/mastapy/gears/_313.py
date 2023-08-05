"""_313.py

BevelHypoidGearRatingSettings
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_RATING_SETTINGS = python_net_import('SMT.MastaAPI.Gears', 'BevelHypoidGearRatingSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelHypoidGearRatingSettings',)


class BevelHypoidGearRatingSettings(_0.APIBase):
    """BevelHypoidGearRatingSettings

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_RATING_SETTINGS

    class _Cast_BevelHypoidGearRatingSettings:
        """Special nested class for casting BevelHypoidGearRatingSettings to subclasses."""

        def __init__(self, parent: 'BevelHypoidGearRatingSettings'):
            self._parent = parent

        @property
        def bevel_hypoid_gear_rating_settings(self) -> 'BevelHypoidGearRatingSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelHypoidGearRatingSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelHypoidGearRatingSettings._Cast_BevelHypoidGearRatingSettings':
        return self._Cast_BevelHypoidGearRatingSettings(self)
