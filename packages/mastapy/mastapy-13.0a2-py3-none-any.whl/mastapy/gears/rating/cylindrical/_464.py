"""_464.py

CylindricalPlasticGearRatingSettings
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalPlasticGearRatingSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlasticGearRatingSettings',)


class CylindricalPlasticGearRatingSettings(_0.APIBase):
    """CylindricalPlasticGearRatingSettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS

    class _Cast_CylindricalPlasticGearRatingSettings:
        """Special nested class for casting CylindricalPlasticGearRatingSettings to subclasses."""

        def __init__(self, parent: 'CylindricalPlasticGearRatingSettings'):
            self._parent = parent

        @property
        def cylindrical_plastic_gear_rating_settings(self) -> 'CylindricalPlasticGearRatingSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalPlasticGearRatingSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalPlasticGearRatingSettings._Cast_CylindricalPlasticGearRatingSettings':
        return self._Cast_CylindricalPlasticGearRatingSettings(self)
