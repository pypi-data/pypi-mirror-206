"""_1591.py

DegreesMinutesSeconds
"""
from mastapy.utility.units_and_measurements import _1599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DEGREES_MINUTES_SECONDS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'DegreesMinutesSeconds')


__docformat__ = 'restructuredtext en'
__all__ = ('DegreesMinutesSeconds',)


class DegreesMinutesSeconds(_1599.Unit):
    """DegreesMinutesSeconds

    This is a mastapy class.
    """

    TYPE = _DEGREES_MINUTES_SECONDS

    class _Cast_DegreesMinutesSeconds:
        """Special nested class for casting DegreesMinutesSeconds to subclasses."""

        def __init__(self, parent: 'DegreesMinutesSeconds'):
            self._parent = parent

        @property
        def unit(self):
            return self._parent._cast(_1599.Unit)

        @property
        def degrees_minutes_seconds(self) -> 'DegreesMinutesSeconds':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DegreesMinutesSeconds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DegreesMinutesSeconds._Cast_DegreesMinutesSeconds':
        return self._Cast_DegreesMinutesSeconds(self)
