"""_1509.py

MultipleFourierSeriesInterpolator
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.math_utility import _1501
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTIPLE_FOURIER_SERIES_INTERPOLATOR = python_net_import('SMT.MastaAPI.MathUtility', 'MultipleFourierSeriesInterpolator')


__docformat__ = 'restructuredtext en'
__all__ = ('MultipleFourierSeriesInterpolator',)


class MultipleFourierSeriesInterpolator(_0.APIBase):
    """MultipleFourierSeriesInterpolator

    This is a mastapy class.
    """

    TYPE = _MULTIPLE_FOURIER_SERIES_INTERPOLATOR

    class _Cast_MultipleFourierSeriesInterpolator:
        """Special nested class for casting MultipleFourierSeriesInterpolator to subclasses."""

        def __init__(self, parent: 'MultipleFourierSeriesInterpolator'):
            self._parent = parent

        @property
        def multiple_fourier_series_interpolator(self) -> 'MultipleFourierSeriesInterpolator':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MultipleFourierSeriesInterpolator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x_values_where_data_has_been_specified(self) -> 'List[float]':
        """List[float]: 'XValuesWhereDataHasBeenSpecified' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.XValuesWhereDataHasBeenSpecified

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    def fourier_series_for(self, x_value: 'float') -> '_1501.FourierSeries':
        """ 'FourierSeriesFor' is the original name of this method.

        Args:
            x_value (float)

        Returns:
            mastapy.math_utility.FourierSeries
        """

        x_value = float(x_value)
        method_result = self.wrapped.FourierSeriesFor(x_value if x_value else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def remove_fourier_series_at(self, x_value: 'float'):
        """ 'RemoveFourierSeriesAt' is the original name of this method.

        Args:
            x_value (float)
        """

        x_value = float(x_value)
        self.wrapped.RemoveFourierSeriesAt(x_value if x_value else 0.0)

    @property
    def cast_to(self) -> 'MultipleFourierSeriesInterpolator._Cast_MultipleFourierSeriesInterpolator':
        return self._Cast_MultipleFourierSeriesInterpolator(self)
