"""_1711.py

Time
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Time')


__docformat__ = 'restructuredtext en'
__all__ = ('Time',)


class Time(_1594.MeasurementBase):
    """Time

    This is a mastapy class.
    """

    TYPE = _TIME

    class _Cast_Time:
        """Special nested class for casting Time to subclasses."""

        def __init__(self, parent: 'Time'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def time(self) -> 'Time':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Time.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Time._Cast_Time':
        return self._Cast_Time(self)
