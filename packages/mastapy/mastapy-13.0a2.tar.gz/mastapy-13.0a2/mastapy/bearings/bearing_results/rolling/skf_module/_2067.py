"""_2067.py

FrequencyOfOverRolling
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FREQUENCY_OF_OVER_ROLLING = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'FrequencyOfOverRolling')


__docformat__ = 'restructuredtext en'
__all__ = ('FrequencyOfOverRolling',)


class FrequencyOfOverRolling(_0.APIBase):
    """FrequencyOfOverRolling

    This is a mastapy class.
    """

    TYPE = _FREQUENCY_OF_OVER_ROLLING

    class _Cast_FrequencyOfOverRolling:
        """Special nested class for casting FrequencyOfOverRolling to subclasses."""

        def __init__(self, parent: 'FrequencyOfOverRolling'):
            self._parent = parent

        @property
        def frequency_of_over_rolling(self) -> 'FrequencyOfOverRolling':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FrequencyOfOverRolling.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def point_on_inner_ring(self) -> 'float':
        """float: 'PointOnInnerRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointOnInnerRing

        if temp is None:
            return 0.0

        return temp

    @property
    def point_on_outer_ring(self) -> 'float':
        """float: 'PointOnOuterRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointOnOuterRing

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_element(self) -> 'float':
        """float: 'RollingElement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingElement

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'FrequencyOfOverRolling._Cast_FrequencyOfOverRolling':
        return self._Cast_FrequencyOfOverRolling(self)
