"""_452.py

CylindricalGearFlankDutyCycleRating
"""
from mastapy.gears.rating import _355
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FLANK_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearFlankDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearFlankDutyCycleRating',)


class CylindricalGearFlankDutyCycleRating(_355.GearFlankRating):
    """CylindricalGearFlankDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FLANK_DUTY_CYCLE_RATING

    class _Cast_CylindricalGearFlankDutyCycleRating:
        """Special nested class for casting CylindricalGearFlankDutyCycleRating to subclasses."""

        def __init__(self, parent: 'CylindricalGearFlankDutyCycleRating'):
            self._parent = parent

        @property
        def gear_flank_rating(self):
            return self._parent._cast(_355.GearFlankRating)

        @property
        def cylindrical_gear_flank_duty_cycle_rating(self) -> 'CylindricalGearFlankDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearFlankDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearFlankDutyCycleRating._Cast_CylindricalGearFlankDutyCycleRating':
        return self._Cast_CylindricalGearFlankDutyCycleRating(self)
