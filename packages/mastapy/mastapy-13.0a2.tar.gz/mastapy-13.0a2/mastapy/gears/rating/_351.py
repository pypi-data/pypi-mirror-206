"""_351.py

AbstractGearSetRating
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears import _324
from mastapy.gears.rating import _349, _350
from mastapy.gears.analysis import _1211
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'AbstractGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractGearSetRating',)


class AbstractGearSetRating(_1211.AbstractGearSetAnalysis):
    """AbstractGearSetRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_SET_RATING

    class _Cast_AbstractGearSetRating:
        """Special nested class for casting AbstractGearSetRating to subclasses."""

        def __init__(self, parent: 'AbstractGearSetRating'):
            self._parent = parent

        @property
        def abstract_gear_set_analysis(self):
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating import _358
            
            return self._parent._cast(_358.GearSetDutyCycleRating)

        @property
        def gear_set_rating(self):
            from mastapy.gears.rating import _359
            
            return self._parent._cast(_359.GearSetRating)

        @property
        def zerol_bevel_gear_set_rating(self):
            from mastapy.gears.rating.zerol_bevel import _367
            
            return self._parent._cast(_367.ZerolBevelGearSetRating)

        @property
        def worm_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.worm import _371
            
            return self._parent._cast(_371.WormGearSetDutyCycleRating)

        @property
        def worm_gear_set_rating(self):
            from mastapy.gears.rating.worm import _372
            
            return self._parent._cast(_372.WormGearSetRating)

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
        def face_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.face import _445
            
            return self._parent._cast(_445.FaceGearSetDutyCycleRating)

        @property
        def face_gear_set_rating(self):
            from mastapy.gears.rating.face import _446
            
            return self._parent._cast(_446.FaceGearSetRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _459
            
            return self._parent._cast(_459.CylindricalGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_rating(self):
            from mastapy.gears.rating.cylindrical import _460
            
            return self._parent._cast(_460.CylindricalGearSetRating)

        @property
        def conical_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.conical import _536
            
            return self._parent._cast(_536.ConicalGearSetDutyCycleRating)

        @property
        def conical_gear_set_rating(self):
            from mastapy.gears.rating.conical import _537
            
            return self._parent._cast(_537.ConicalGearSetRating)

        @property
        def concept_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.concept import _547
            
            return self._parent._cast(_547.ConceptGearSetDutyCycleRating)

        @property
        def concept_gear_set_rating(self):
            from mastapy.gears.rating.concept import _548
            
            return self._parent._cast(_548.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(self):
            from mastapy.gears.rating.bevel import _551
            
            return self._parent._cast(_551.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _562
            
            return self._parent._cast(_562.AGMAGleasonConicalGearSetRating)

        @property
        def abstract_gear_set_rating(self) -> 'AbstractGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractGearSetRating.TYPE'):
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
    def normalized_safety_factor_for_fatigue_and_static(self) -> 'float':
        """float: 'NormalizedSafetyFactorForFatigueAndStatic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalizedSafetyFactorForFatigueAndStatic

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
    def transmission_properties_gears(self) -> '_324.GearSetDesignGroup':
        """GearSetDesignGroup: 'TransmissionPropertiesGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransmissionPropertiesGears

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_mesh_ratings(self) -> 'List[_349.AbstractGearMeshRating]':
        """List[AbstractGearMeshRating]: 'GearMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_ratings(self) -> 'List[_350.AbstractGearRating]':
        """List[AbstractGearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractGearSetRating._Cast_AbstractGearSetRating':
        return self._Cast_AbstractGearSetRating(self)
