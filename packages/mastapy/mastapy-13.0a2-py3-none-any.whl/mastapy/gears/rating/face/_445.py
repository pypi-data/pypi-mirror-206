"""_445.py

FaceGearSetDutyCycleRating
"""
from mastapy.gears.rating import _358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Face', 'FaceGearSetDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetDutyCycleRating',)


class FaceGearSetDutyCycleRating(_358.GearSetDutyCycleRating):
    """FaceGearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_DUTY_CYCLE_RATING

    class _Cast_FaceGearSetDutyCycleRating:
        """Special nested class for casting FaceGearSetDutyCycleRating to subclasses."""

        def __init__(self, parent: 'FaceGearSetDutyCycleRating'):
            self._parent = parent

        @property
        def gear_set_duty_cycle_rating(self):
            return self._parent._cast(_358.GearSetDutyCycleRating)

        @property
        def abstract_gear_set_rating(self):
            from mastapy.gears.rating import _351
            
            return self._parent._cast(_351.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def face_gear_set_duty_cycle_rating(self) -> 'FaceGearSetDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearSetDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FaceGearSetDutyCycleRating._Cast_FaceGearSetDutyCycleRating':
        return self._Cast_FaceGearSetDutyCycleRating(self)
