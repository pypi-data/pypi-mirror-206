"""_2538.py

RotorSetMeasuredPoint
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTOR_SET_MEASURED_POINT = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'RotorSetMeasuredPoint')


__docformat__ = 'restructuredtext en'
__all__ = ('RotorSetMeasuredPoint',)


class RotorSetMeasuredPoint(_0.APIBase):
    """RotorSetMeasuredPoint

    This is a mastapy class.
    """

    TYPE = _ROTOR_SET_MEASURED_POINT

    class _Cast_RotorSetMeasuredPoint:
        """Special nested class for casting RotorSetMeasuredPoint to subclasses."""

        def __init__(self, parent: 'RotorSetMeasuredPoint'):
            self._parent = parent

        @property
        def rotor_set_measured_point(self) -> 'RotorSetMeasuredPoint':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RotorSetMeasuredPoint.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def boost_pressure(self) -> 'float':
        """float: 'BoostPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoostPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def input_power(self) -> 'float':
        """float: 'InputPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InputPower

        if temp is None:
            return 0.0

        return temp

    @property
    def rotor_speed(self) -> 'float':
        """float: 'RotorSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'RotorSetMeasuredPoint._Cast_RotorSetMeasuredPoint':
        return self._Cast_RotorSetMeasuredPoint(self)
