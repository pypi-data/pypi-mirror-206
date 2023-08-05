"""_6853.py

ForceAndTorqueScalingFactor
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_AND_TORQUE_SCALING_FACTOR = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ForceAndTorqueScalingFactor')


__docformat__ = 'restructuredtext en'
__all__ = ('ForceAndTorqueScalingFactor',)


class ForceAndTorqueScalingFactor(_0.APIBase):
    """ForceAndTorqueScalingFactor

    This is a mastapy class.
    """

    TYPE = _FORCE_AND_TORQUE_SCALING_FACTOR

    class _Cast_ForceAndTorqueScalingFactor:
        """Special nested class for casting ForceAndTorqueScalingFactor to subclasses."""

        def __init__(self, parent: 'ForceAndTorqueScalingFactor'):
            self._parent = parent

        @property
        def force_and_torque_scaling_factor(self) -> 'ForceAndTorqueScalingFactor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ForceAndTorqueScalingFactor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force_scaling_factor(self) -> 'float':
        """float: 'ForceScalingFactor' is the original name of this property."""

        temp = self.wrapped.ForceScalingFactor

        if temp is None:
            return 0.0

        return temp

    @force_scaling_factor.setter
    def force_scaling_factor(self, value: 'float'):
        self.wrapped.ForceScalingFactor = float(value) if value else 0.0

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
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_scaling_factor(self) -> 'float':
        """float: 'TorqueScalingFactor' is the original name of this property."""

        temp = self.wrapped.TorqueScalingFactor

        if temp is None:
            return 0.0

        return temp

    @torque_scaling_factor.setter
    def torque_scaling_factor(self, value: 'float'):
        self.wrapped.TorqueScalingFactor = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ForceAndTorqueScalingFactor._Cast_ForceAndTorqueScalingFactor':
        return self._Cast_ForceAndTorqueScalingFactor(self)
