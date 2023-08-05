"""_1422.py

GBT17855SplineJointDutyCycleRating
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GBT17855_SPLINE_JOINT_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines.DutyCycleRatings', 'GBT17855SplineJointDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GBT17855SplineJointDutyCycleRating',)


class GBT17855SplineJointDutyCycleRating(_0.APIBase):
    """GBT17855SplineJointDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _GBT17855_SPLINE_JOINT_DUTY_CYCLE_RATING

    class _Cast_GBT17855SplineJointDutyCycleRating:
        """Special nested class for casting GBT17855SplineJointDutyCycleRating to subclasses."""

        def __init__(self, parent: 'GBT17855SplineJointDutyCycleRating'):
            self._parent = parent

        @property
        def gbt17855_spline_joint_duty_cycle_rating(self) -> 'GBT17855SplineJointDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GBT17855SplineJointDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def safety_factor_for_equivalent_stress(self) -> 'float':
        """float: 'SafetyFactorForEquivalentStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForEquivalentStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_root_bending_stress(self) -> 'float':
        """float: 'SafetyFactorForRootBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForRootBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_tooth_shearing_stress(self) -> 'float':
        """float: 'SafetyFactorForToothShearingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForToothShearingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_wearing_stress(self) -> 'float':
        """float: 'SafetyFactorForWearingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForWearingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'GBT17855SplineJointDutyCycleRating._Cast_GBT17855SplineJointDutyCycleRating':
        return self._Cast_GBT17855SplineJointDutyCycleRating(self)
