"""_1712.py

TimeShort
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_SHORT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'TimeShort')


__docformat__ = 'restructuredtext en'
__all__ = ('TimeShort',)


class TimeShort(_1594.MeasurementBase):
    """TimeShort

    This is a mastapy class.
    """

    TYPE = _TIME_SHORT

    class _Cast_TimeShort:
        """Special nested class for casting TimeShort to subclasses."""

        def __init__(self, parent: 'TimeShort'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def time_short(self) -> 'TimeShort':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TimeShort.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TimeShort._Cast_TimeShort':
        return self._Cast_TimeShort(self)
