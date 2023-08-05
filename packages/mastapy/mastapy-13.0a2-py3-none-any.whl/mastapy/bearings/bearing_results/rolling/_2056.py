"""_2056.py

RollingBearingSpeedResults
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_BEARING_SPEED_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'RollingBearingSpeedResults')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingBearingSpeedResults',)


class RollingBearingSpeedResults(_0.APIBase):
    """RollingBearingSpeedResults

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING_SPEED_RESULTS

    class _Cast_RollingBearingSpeedResults:
        """Special nested class for casting RollingBearingSpeedResults to subclasses."""

        def __init__(self, parent: 'RollingBearingSpeedResults'):
            self._parent = parent

        @property
        def rolling_bearing_speed_results(self) -> 'RollingBearingSpeedResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingBearingSpeedResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_element_passing_order(self) -> 'float':
        """float: 'AbsoluteElementPassingOrder' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AbsoluteElementPassingOrder

        if temp is None:
            return 0.0

        return temp

    @property
    def element_spin_order(self) -> 'float':
        """float: 'ElementSpinOrder' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementSpinOrder

        if temp is None:
            return 0.0

        return temp

    @property
    def fundamental_train_order(self) -> 'float':
        """float: 'FundamentalTrainOrder' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FundamentalTrainOrder

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_race_element_passing_order(self) -> 'float':
        """float: 'InnerRaceElementPassingOrder' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRaceElementPassingOrder

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_race_element_passing_order(self) -> 'float':
        """float: 'OuterRaceElementPassingOrder' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRaceElementPassingOrder

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'RollingBearingSpeedResults._Cast_RollingBearingSpeedResults':
        return self._Cast_RollingBearingSpeedResults(self)
