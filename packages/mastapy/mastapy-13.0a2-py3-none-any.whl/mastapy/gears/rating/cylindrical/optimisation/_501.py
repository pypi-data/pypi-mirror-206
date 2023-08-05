"""_501.py

SafetyFactorOptimisationStepResultNumber
"""
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.optimisation import _499
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_OPTIMISATION_STEP_RESULT_NUMBER = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation', 'SafetyFactorOptimisationStepResultNumber')


__docformat__ = 'restructuredtext en'
__all__ = ('SafetyFactorOptimisationStepResultNumber',)


class SafetyFactorOptimisationStepResultNumber(_499.SafetyFactorOptimisationStepResult):
    """SafetyFactorOptimisationStepResultNumber

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_OPTIMISATION_STEP_RESULT_NUMBER

    class _Cast_SafetyFactorOptimisationStepResultNumber:
        """Special nested class for casting SafetyFactorOptimisationStepResultNumber to subclasses."""

        def __init__(self, parent: 'SafetyFactorOptimisationStepResultNumber'):
            self._parent = parent

        @property
        def safety_factor_optimisation_step_result(self):
            return self._parent._cast(_499.SafetyFactorOptimisationStepResult)

        @property
        def safety_factor_optimisation_step_result_number(self) -> 'SafetyFactorOptimisationStepResultNumber':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SafetyFactorOptimisationStepResultNumber.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def value(self) -> 'float':
        """float: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'SafetyFactorOptimisationStepResultNumber._Cast_SafetyFactorOptimisationStepResultNumber':
        return self._Cast_SafetyFactorOptimisationStepResultNumber(self)
