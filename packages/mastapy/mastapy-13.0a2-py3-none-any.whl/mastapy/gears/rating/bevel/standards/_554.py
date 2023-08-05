"""_554.py

GleasonSpiralBevelGearSingleFlankRating
"""
from mastapy._internal import constructor
from mastapy.gears.rating.bevel.standards import _556
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GLEASON_SPIRAL_BEVEL_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Bevel.Standards', 'GleasonSpiralBevelGearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GleasonSpiralBevelGearSingleFlankRating',)


class GleasonSpiralBevelGearSingleFlankRating(_556.SpiralBevelGearSingleFlankRating):
    """GleasonSpiralBevelGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _GLEASON_SPIRAL_BEVEL_GEAR_SINGLE_FLANK_RATING

    class _Cast_GleasonSpiralBevelGearSingleFlankRating:
        """Special nested class for casting GleasonSpiralBevelGearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'GleasonSpiralBevelGearSingleFlankRating'):
            self._parent = parent

        @property
        def spiral_bevel_gear_single_flank_rating(self):
            return self._parent._cast(_556.SpiralBevelGearSingleFlankRating)

        @property
        def conical_gear_single_flank_rating(self):
            from mastapy.gears.rating.conical import _538
            
            return self._parent._cast(_538.ConicalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(self):
            from mastapy.gears.rating import _360
            
            return self._parent._cast(_360.GearSingleFlankRating)

        @property
        def gleason_spiral_bevel_gear_single_flank_rating(self) -> 'GleasonSpiralBevelGearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GleasonSpiralBevelGearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_for_fatigue(self) -> 'float':
        """float: 'BendingSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_bending_stress(self) -> 'float':
        """float: 'CalculatedBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_contact_stress(self) -> 'float':
        """float: 'CalculatedContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_scoring_index(self) -> 'float':
        """float: 'CalculatedScoringIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedScoringIndex

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_fatigue(self) -> 'float':
        """float: 'ContactSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_blank_temperature(self) -> 'float':
        """float: 'GearBlankTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBlankTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def hardness_ratio_factor(self) -> 'float':
        """float: 'HardnessRatioFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HardnessRatioFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def working_bending_stress(self) -> 'float':
        """float: 'WorkingBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def working_contact_stress(self) -> 'float':
        """float: 'WorkingContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def working_scoring_index(self) -> 'float':
        """float: 'WorkingScoringIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingScoringIndex

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'GleasonSpiralBevelGearSingleFlankRating._Cast_GleasonSpiralBevelGearSingleFlankRating':
        return self._Cast_GleasonSpiralBevelGearSingleFlankRating(self)
