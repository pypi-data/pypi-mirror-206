"""_2069.py

FrictionalMoment
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FRICTIONAL_MOMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'FrictionalMoment')


__docformat__ = 'restructuredtext en'
__all__ = ('FrictionalMoment',)


class FrictionalMoment(_0.APIBase):
    """FrictionalMoment

    This is a mastapy class.
    """

    TYPE = _FRICTIONAL_MOMENT

    class _Cast_FrictionalMoment:
        """Special nested class for casting FrictionalMoment to subclasses."""

        def __init__(self, parent: 'FrictionalMoment'):
            self._parent = parent

        @property
        def frictional_moment(self) -> 'FrictionalMoment':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FrictionalMoment.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def at_start_2030_degrees_c_and_zero_speed(self) -> 'float':
        """float: 'AtStart2030DegreesCAndZeroSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AtStart2030DegreesCAndZeroSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def total(self) -> 'float':
        """float: 'Total' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Total

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'FrictionalMoment._Cast_FrictionalMoment':
        return self._Cast_FrictionalMoment(self)
