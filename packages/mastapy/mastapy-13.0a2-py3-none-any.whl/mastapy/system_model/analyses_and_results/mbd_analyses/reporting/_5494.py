"""_5494.py

DynamicForceResultAtTime
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5493
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_RESULT_AT_TIME = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Reporting', 'DynamicForceResultAtTime')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicForceResultAtTime',)


class DynamicForceResultAtTime(_5493.AbstractMeasuredDynamicResponseAtTime):
    """DynamicForceResultAtTime

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCE_RESULT_AT_TIME

    class _Cast_DynamicForceResultAtTime:
        """Special nested class for casting DynamicForceResultAtTime to subclasses."""

        def __init__(self, parent: 'DynamicForceResultAtTime'):
            self._parent = parent

        @property
        def abstract_measured_dynamic_response_at_time(self):
            return self._parent._cast(_5493.AbstractMeasuredDynamicResponseAtTime)

        @property
        def dynamic_force_result_at_time(self) -> 'DynamicForceResultAtTime':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicForceResultAtTime.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_dynamic_force(self) -> 'float':
        """float: 'AbsoluteDynamicForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AbsoluteDynamicForce

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_force(self) -> 'float':
        """float: 'DynamicForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicForce

        if temp is None:
            return 0.0

        return temp

    @property
    def force(self) -> 'float':
        """float: 'Force' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Force

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_force(self) -> 'float':
        """float: 'MeanForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanForce

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'DynamicForceResultAtTime._Cast_DynamicForceResultAtTime':
        return self._Cast_DynamicForceResultAtTime(self)
