"""_350.py

AbstractGearRating
"""
from mastapy._internal import constructor
from mastapy.gears.analysis import _1209
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'AbstractGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractGearRating',)


class AbstractGearRating(_1209.AbstractGearAnalysis):
    """AbstractGearRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_RATING

    class _Cast_AbstractGearRating:
        """Special nested class for casting AbstractGearRating to subclasses."""

        def __init__(self, parent: 'AbstractGearRating'):
            self._parent = parent

        @property
        def abstract_gear_analysis(self):
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def gear_duty_cycle_rating(self):
            from mastapy.gears.rating import _354
            
            return self._parent._cast(_354.GearDutyCycleRating)

        @property
        def gear_rating(self):
            from mastapy.gears.rating import _357
            
            return self._parent._cast(_357.GearRating)

        @property
        def zerol_bevel_gear_rating(self):
            from mastapy.gears.rating.zerol_bevel import _366
            
            return self._parent._cast(_366.ZerolBevelGearRating)

        @property
        def worm_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.worm import _368
            
            return self._parent._cast(_368.WormGearDutyCycleRating)

        @property
        def worm_gear_rating(self):
            from mastapy.gears.rating.worm import _370
            
            return self._parent._cast(_370.WormGearRating)

        @property
        def straight_bevel_gear_rating(self):
            from mastapy.gears.rating.straight_bevel import _392
            
            return self._parent._cast(_392.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _395
            
            return self._parent._cast(_395.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(self):
            from mastapy.gears.rating.spiral_bevel import _399
            
            return self._parent._cast(_399.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _402
            
            return self._parent._cast(_402.KlingelnbergCycloPalloidSpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _405
            
            return self._parent._cast(_405.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(self):
            from mastapy.gears.rating.klingelnberg_conical import _408
            
            return self._parent._cast(_408.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(self):
            from mastapy.gears.rating.hypoid import _435
            
            return self._parent._cast(_435.HypoidGearRating)

        @property
        def face_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.face import _441
            
            return self._parent._cast(_441.FaceGearDutyCycleRating)

        @property
        def face_gear_rating(self):
            from mastapy.gears.rating.face import _444
            
            return self._parent._cast(_444.FaceGearRating)

        @property
        def cylindrical_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _451
            
            return self._parent._cast(_451.CylindricalGearDutyCycleRating)

        @property
        def cylindrical_gear_rating(self):
            from mastapy.gears.rating.cylindrical import _456
            
            return self._parent._cast(_456.CylindricalGearRating)

        @property
        def conical_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.conical import _533
            
            return self._parent._cast(_533.ConicalGearDutyCycleRating)

        @property
        def conical_gear_rating(self):
            from mastapy.gears.rating.conical import _535
            
            return self._parent._cast(_535.ConicalGearRating)

        @property
        def concept_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.concept import _543
            
            return self._parent._cast(_543.ConceptGearDutyCycleRating)

        @property
        def concept_gear_rating(self):
            from mastapy.gears.rating.concept import _546
            
            return self._parent._cast(_546.ConceptGearRating)

        @property
        def bevel_gear_rating(self):
            from mastapy.gears.rating.bevel import _550
            
            return self._parent._cast(_550.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _561
            
            return self._parent._cast(_561.AGMAGleasonConicalGearRating)

        @property
        def abstract_gear_rating(self) -> 'AbstractGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractGearRating.TYPE'):
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
    def cycles_to_fail(self) -> 'float':
        """float: 'CyclesToFail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CyclesToFail

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail_bending(self) -> 'float':
        """float: 'CyclesToFailBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CyclesToFailBending

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail_contact(self) -> 'float':
        """float: 'CyclesToFailContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CyclesToFailContact

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
    def gear_reliability_bending(self) -> 'float':
        """float: 'GearReliabilityBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearReliabilityBending

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_reliability_contact(self) -> 'float':
        """float: 'GearReliabilityContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearReliabilityContact

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_bending_safety_factor_for_fatigue(self) -> 'float':
        """float: 'NormalizedBendingSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalizedBendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_bending_safety_factor_for_static(self) -> 'float':
        """float: 'NormalizedBendingSafetyFactorForStatic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalizedBendingSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_contact_safety_factor_for_fatigue(self) -> 'float':
        """float: 'NormalizedContactSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalizedContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_contact_safety_factor_for_static(self) -> 'float':
        """float: 'NormalizedContactSafetyFactorForStatic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalizedContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_fatigue(self) -> 'float':
        """float: 'NormalizedSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalizedSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_static(self) -> 'float':
        """float: 'NormalizedSafetyFactorForStatic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalizedSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail(self) -> 'float':
        """float: 'TimeToFail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeToFail

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail_bending(self) -> 'float':
        """float: 'TimeToFailBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeToFailBending

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail_contact(self) -> 'float':
        """float: 'TimeToFailContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeToFailContact

        if temp is None:
            return 0.0

        return temp

    @property
    def total_gear_reliability(self) -> 'float':
        """float: 'TotalGearReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalGearReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'AbstractGearRating._Cast_AbstractGearRating':
        return self._Cast_AbstractGearRating(self)
