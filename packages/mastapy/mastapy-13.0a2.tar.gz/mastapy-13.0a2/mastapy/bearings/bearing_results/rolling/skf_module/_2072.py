"""_2072.py

GreaseLifeAndRelubricationInterval
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import (
    _2071, _2073, _2074, _2081
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GREASE_LIFE_AND_RELUBRICATION_INTERVAL = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'GreaseLifeAndRelubricationInterval')


__docformat__ = 'restructuredtext en'
__all__ = ('GreaseLifeAndRelubricationInterval',)


class GreaseLifeAndRelubricationInterval(_2081.SKFCalculationResult):
    """GreaseLifeAndRelubricationInterval

    This is a mastapy class.
    """

    TYPE = _GREASE_LIFE_AND_RELUBRICATION_INTERVAL

    class _Cast_GreaseLifeAndRelubricationInterval:
        """Special nested class for casting GreaseLifeAndRelubricationInterval to subclasses."""

        def __init__(self, parent: 'GreaseLifeAndRelubricationInterval'):
            self._parent = parent

        @property
        def skf_calculation_result(self):
            return self._parent._cast(_2081.SKFCalculationResult)

        @property
        def grease_life_and_relubrication_interval(self) -> 'GreaseLifeAndRelubricationInterval':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GreaseLifeAndRelubricationInterval.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def speed_factor(self) -> 'float':
        """float: 'SpeedFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def grease(self) -> '_2071.Grease':
        """Grease: 'Grease' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Grease

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def grease_quantity(self) -> '_2073.GreaseQuantity':
        """GreaseQuantity: 'GreaseQuantity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GreaseQuantity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def initial_fill(self) -> '_2074.InitialFill':
        """InitialFill: 'InitialFill' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InitialFill

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GreaseLifeAndRelubricationInterval._Cast_GreaseLifeAndRelubricationInterval':
        return self._Cast_GreaseLifeAndRelubricationInterval(self)
