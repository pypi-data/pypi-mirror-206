"""_355.py

GearFlankRating
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearFlankRating',)


class GearFlankRating(_0.APIBase):
    """GearFlankRating

    This is a mastapy class.
    """

    TYPE = _GEAR_FLANK_RATING

    class _Cast_GearFlankRating:
        """Special nested class for casting GearFlankRating to subclasses."""

        def __init__(self, parent: 'GearFlankRating'):
            self._parent = parent

        @property
        def cylindrical_gear_flank_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _452
            
            return self._parent._cast(_452.CylindricalGearFlankDutyCycleRating)

        @property
        def cylindrical_gear_flank_rating(self):
            from mastapy.gears.rating.cylindrical import _453
            
            return self._parent._cast(_453.CylindricalGearFlankRating)

        @property
        def gear_flank_rating(self) -> 'GearFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearFlankRating.TYPE'):
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
    def bending_safety_factor_for_static(self) -> 'float':
        """float: 'BendingSafetyFactorForStatic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingSafetyFactorForStatic

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
    def contact_safety_factor_for_static(self) -> 'float':
        """float: 'ContactSafetyFactorForStatic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles(self) -> 'float':
        """float: 'Cycles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cycles

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_bending(self) -> 'float':
        """float: 'DamageBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageBending

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_contact(self) -> 'float':
        """float: 'DamageContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageContact

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_bending_stress(self) -> 'float':
        """float: 'MaximumBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_stress(self) -> 'float':
        """float: 'MaximumContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_static_bending_stress(self) -> 'float':
        """float: 'MaximumStaticBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumStaticBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_static_contact_stress(self) -> 'float':
        """float: 'MaximumStaticContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumStaticContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_bending(self) -> 'float':
        """float: 'ReliabilityBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReliabilityBending

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_contact(self) -> 'float':
        """float: 'ReliabilityContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReliabilityContact

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'GearFlankRating._Cast_GearFlankRating':
        return self._Cast_GearFlankRating(self)
