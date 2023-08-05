"""_1275.py

MotorRotorSideFaceDetail
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOTOR_ROTOR_SIDE_FACE_DETAIL = python_net_import('SMT.MastaAPI.ElectricMachines', 'MotorRotorSideFaceDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('MotorRotorSideFaceDetail',)


class MotorRotorSideFaceDetail(_0.APIBase):
    """MotorRotorSideFaceDetail

    This is a mastapy class.
    """

    TYPE = _MOTOR_ROTOR_SIDE_FACE_DETAIL

    class _Cast_MotorRotorSideFaceDetail:
        """Special nested class for casting MotorRotorSideFaceDetail to subclasses."""

        def __init__(self, parent: 'MotorRotorSideFaceDetail'):
            self._parent = parent

        @property
        def motor_rotor_side_face_detail(self) -> 'MotorRotorSideFaceDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MotorRotorSideFaceDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_air_gap(self) -> 'float':
        """float: 'AxialAirGap' is the original name of this property."""

        temp = self.wrapped.AxialAirGap

        if temp is None:
            return 0.0

        return temp

    @axial_air_gap.setter
    def axial_air_gap(self, value: 'float'):
        self.wrapped.AxialAirGap = float(value) if value else 0.0

    @property
    def inner_radius(self) -> 'float':
        """float: 'InnerRadius' is the original name of this property."""

        temp = self.wrapped.InnerRadius

        if temp is None:
            return 0.0

        return temp

    @inner_radius.setter
    def inner_radius(self, value: 'float'):
        self.wrapped.InnerRadius = float(value) if value else 0.0

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def outer_radius(self) -> 'float':
        """float: 'OuterRadius' is the original name of this property."""

        temp = self.wrapped.OuterRadius

        if temp is None:
            return 0.0

        return temp

    @outer_radius.setter
    def outer_radius(self, value: 'float'):
        self.wrapped.OuterRadius = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'MotorRotorSideFaceDetail._Cast_MotorRotorSideFaceDetail':
        return self._Cast_MotorRotorSideFaceDetail(self)
