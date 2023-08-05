"""_543.py

ConceptGearDutyCycleRating
"""
from mastapy.gears.rating import _355, _354
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Concept', 'ConceptGearDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearDutyCycleRating',)


class ConceptGearDutyCycleRating(_354.GearDutyCycleRating):
    """ConceptGearDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_DUTY_CYCLE_RATING

    class _Cast_ConceptGearDutyCycleRating:
        """Special nested class for casting ConceptGearDutyCycleRating to subclasses."""

        def __init__(self, parent: 'ConceptGearDutyCycleRating'):
            self._parent = parent

        @property
        def gear_duty_cycle_rating(self):
            return self._parent._cast(_354.GearDutyCycleRating)

        @property
        def abstract_gear_rating(self):
            from mastapy.gears.rating import _350
            
            return self._parent._cast(_350.AbstractGearRating)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def concept_gear_duty_cycle_rating(self) -> 'ConceptGearDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank_rating(self) -> '_355.GearFlankRating':
        """GearFlankRating: 'LeftFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank_rating(self) -> '_355.GearFlankRating':
        """GearFlankRating: 'RightFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConceptGearDutyCycleRating._Cast_ConceptGearDutyCycleRating':
        return self._Cast_ConceptGearDutyCycleRating(self)
