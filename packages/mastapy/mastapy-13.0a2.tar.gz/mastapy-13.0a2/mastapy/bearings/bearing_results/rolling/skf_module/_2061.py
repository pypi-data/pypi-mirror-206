"""_2061.py

AdjustedSpeed
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2062, _2081
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADJUSTED_SPEED = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'AdjustedSpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('AdjustedSpeed',)


class AdjustedSpeed(_2081.SKFCalculationResult):
    """AdjustedSpeed

    This is a mastapy class.
    """

    TYPE = _ADJUSTED_SPEED

    class _Cast_AdjustedSpeed:
        """Special nested class for casting AdjustedSpeed to subclasses."""

        def __init__(self, parent: 'AdjustedSpeed'):
            self._parent = parent

        @property
        def skf_calculation_result(self):
            return self._parent._cast(_2081.SKFCalculationResult)

        @property
        def adjusted_speed(self) -> 'AdjustedSpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AdjustedSpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjusted_reference_speed(self) -> 'float':
        """float: 'AdjustedReferenceSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustedReferenceSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def adjustment_factors(self) -> '_2062.AdjustmentFactors':
        """AdjustmentFactors: 'AdjustmentFactors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustmentFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AdjustedSpeed._Cast_AdjustedSpeed':
        return self._Cast_AdjustedSpeed(self)
