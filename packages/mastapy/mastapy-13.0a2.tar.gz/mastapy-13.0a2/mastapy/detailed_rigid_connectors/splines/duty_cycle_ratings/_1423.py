"""_1423.py

SAESplineJointDutyCycleRating
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAE_SPLINE_JOINT_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines.DutyCycleRatings', 'SAESplineJointDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('SAESplineJointDutyCycleRating',)


class SAESplineJointDutyCycleRating(_0.APIBase):
    """SAESplineJointDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _SAE_SPLINE_JOINT_DUTY_CYCLE_RATING

    class _Cast_SAESplineJointDutyCycleRating:
        """Special nested class for casting SAESplineJointDutyCycleRating to subclasses."""

        def __init__(self, parent: 'SAESplineJointDutyCycleRating'):
            self._parent = parent

        @property
        def sae_spline_joint_duty_cycle_rating(self) -> 'SAESplineJointDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SAESplineJointDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fatigue_damage_for_compressive_stress(self) -> 'float':
        """float: 'FatigueDamageForCompressiveStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FatigueDamageForCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_damage_for_equivalent_root_stress(self) -> 'float':
        """float: 'FatigueDamageForEquivalentRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FatigueDamageForEquivalentRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_damage_for_tooth_shear_stress(self) -> 'float':
        """float: 'FatigueDamageForToothShearStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FatigueDamageForToothShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_compressive_stress(self) -> 'float':
        """float: 'SafetyFactorForCompressiveStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_tooth_shear_stress(self) -> 'float':
        """float: 'SafetyFactorForToothShearStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForToothShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_equivalent_root_stress(self) -> 'float':
        """float: 'SafetyFactorForEquivalentRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForEquivalentRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'SAESplineJointDutyCycleRating._Cast_SAESplineJointDutyCycleRating':
        return self._Cast_SAESplineJointDutyCycleRating(self)
