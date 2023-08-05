"""_502.py

SafetyFactorOptimisationStepResultShortLength
"""
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.optimisation import _499
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_OPTIMISATION_STEP_RESULT_SHORT_LENGTH = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation', 'SafetyFactorOptimisationStepResultShortLength')


__docformat__ = 'restructuredtext en'
__all__ = ('SafetyFactorOptimisationStepResultShortLength',)


class SafetyFactorOptimisationStepResultShortLength(_499.SafetyFactorOptimisationStepResult):
    """SafetyFactorOptimisationStepResultShortLength

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_OPTIMISATION_STEP_RESULT_SHORT_LENGTH

    class _Cast_SafetyFactorOptimisationStepResultShortLength:
        """Special nested class for casting SafetyFactorOptimisationStepResultShortLength to subclasses."""

        def __init__(self, parent: 'SafetyFactorOptimisationStepResultShortLength'):
            self._parent = parent

        @property
        def safety_factor_optimisation_step_result(self):
            return self._parent._cast(_499.SafetyFactorOptimisationStepResult)

        @property
        def safety_factor_optimisation_step_result_short_length(self) -> 'SafetyFactorOptimisationStepResultShortLength':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SafetyFactorOptimisationStepResultShortLength.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'SafetyFactorOptimisationStepResultShortLength._Cast_SafetyFactorOptimisationStepResultShortLength':
        return self._Cast_SafetyFactorOptimisationStepResultShortLength(self)
