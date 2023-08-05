"""_499.py

SafetyFactorOptimisationStepResult
"""
from mastapy.gears.rating import _364
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_OPTIMISATION_STEP_RESULT = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation', 'SafetyFactorOptimisationStepResult')


__docformat__ = 'restructuredtext en'
__all__ = ('SafetyFactorOptimisationStepResult',)


class SafetyFactorOptimisationStepResult(_0.APIBase):
    """SafetyFactorOptimisationStepResult

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_OPTIMISATION_STEP_RESULT

    class _Cast_SafetyFactorOptimisationStepResult:
        """Special nested class for casting SafetyFactorOptimisationStepResult to subclasses."""

        def __init__(self, parent: 'SafetyFactorOptimisationStepResult'):
            self._parent = parent

        @property
        def safety_factor_optimisation_step_result_angle(self):
            from mastapy.gears.rating.cylindrical.optimisation import _500
            
            return self._parent._cast(_500.SafetyFactorOptimisationStepResultAngle)

        @property
        def safety_factor_optimisation_step_result_number(self):
            from mastapy.gears.rating.cylindrical.optimisation import _501
            
            return self._parent._cast(_501.SafetyFactorOptimisationStepResultNumber)

        @property
        def safety_factor_optimisation_step_result_short_length(self):
            from mastapy.gears.rating.cylindrical.optimisation import _502
            
            return self._parent._cast(_502.SafetyFactorOptimisationStepResultShortLength)

        @property
        def safety_factor_optimisation_step_result(self) -> 'SafetyFactorOptimisationStepResult':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SafetyFactorOptimisationStepResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def normalised_safety_factors(self) -> '_364.SafetyFactorResults':
        """SafetyFactorResults: 'NormalisedSafetyFactors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalisedSafetyFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def safety_factors(self) -> '_364.SafetyFactorResults':
        """SafetyFactorResults: 'SafetyFactors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SafetyFactorOptimisationStepResult._Cast_SafetyFactorOptimisationStepResult':
        return self._Cast_SafetyFactorOptimisationStepResult(self)
