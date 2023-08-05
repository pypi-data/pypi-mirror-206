"""_1598.py

TimeUnit
"""
from mastapy.utility.units_and_measurements import _1599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_UNIT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'TimeUnit')


__docformat__ = 'restructuredtext en'
__all__ = ('TimeUnit',)


class TimeUnit(_1599.Unit):
    """TimeUnit

    This is a mastapy class.
    """

    TYPE = _TIME_UNIT

    class _Cast_TimeUnit:
        """Special nested class for casting TimeUnit to subclasses."""

        def __init__(self, parent: 'TimeUnit'):
            self._parent = parent

        @property
        def unit(self):
            return self._parent._cast(_1599.Unit)

        @property
        def time_unit(self) -> 'TimeUnit':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TimeUnit.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TimeUnit._Cast_TimeUnit':
        return self._Cast_TimeUnit(self)
