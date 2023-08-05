"""_5496.py

DynamicTorqueResultAtTime
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5493
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_TORQUE_RESULT_AT_TIME = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Reporting', 'DynamicTorqueResultAtTime')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicTorqueResultAtTime',)


class DynamicTorqueResultAtTime(_5493.AbstractMeasuredDynamicResponseAtTime):
    """DynamicTorqueResultAtTime

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_TORQUE_RESULT_AT_TIME

    class _Cast_DynamicTorqueResultAtTime:
        """Special nested class for casting DynamicTorqueResultAtTime to subclasses."""

        def __init__(self, parent: 'DynamicTorqueResultAtTime'):
            self._parent = parent

        @property
        def abstract_measured_dynamic_response_at_time(self):
            return self._parent._cast(_5493.AbstractMeasuredDynamicResponseAtTime)

        @property
        def dynamic_torque_result_at_time(self) -> 'DynamicTorqueResultAtTime':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicTorqueResultAtTime.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_dynamic_torque(self) -> 'float':
        """float: 'AbsoluteDynamicTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AbsoluteDynamicTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_torque(self) -> 'float':
        """float: 'DynamicTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_torque(self) -> 'float':
        """float: 'MeanTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self) -> 'float':
        """float: 'Torque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'DynamicTorqueResultAtTime._Cast_DynamicTorqueResultAtTime':
        return self._Cast_DynamicTorqueResultAtTime(self)
