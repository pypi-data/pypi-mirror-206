"""_1438.py

InterferenceFitDutyCycleRating
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_FIT_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits.DutyCycleRatings', 'InterferenceFitDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('InterferenceFitDutyCycleRating',)


class InterferenceFitDutyCycleRating(_0.APIBase):
    """InterferenceFitDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_FIT_DUTY_CYCLE_RATING

    class _Cast_InterferenceFitDutyCycleRating:
        """Special nested class for casting InterferenceFitDutyCycleRating to subclasses."""

        def __init__(self, parent: 'InterferenceFitDutyCycleRating'):
            self._parent = parent

        @property
        def interference_fit_duty_cycle_rating(self) -> 'InterferenceFitDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterferenceFitDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def safety_factor_for_axial_force(self) -> 'float':
        """float: 'SafetyFactorForAxialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_torque(self) -> 'float':
        """float: 'SafetyFactorForTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'InterferenceFitDutyCycleRating._Cast_InterferenceFitDutyCycleRating':
        return self._Cast_InterferenceFitDutyCycleRating(self)
