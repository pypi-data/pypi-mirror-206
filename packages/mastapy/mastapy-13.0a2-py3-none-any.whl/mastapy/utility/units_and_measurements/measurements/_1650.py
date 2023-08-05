"""_1650.py

InverseShortTime
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INVERSE_SHORT_TIME = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'InverseShortTime')


__docformat__ = 'restructuredtext en'
__all__ = ('InverseShortTime',)


class InverseShortTime(_1594.MeasurementBase):
    """InverseShortTime

    This is a mastapy class.
    """

    TYPE = _INVERSE_SHORT_TIME

    class _Cast_InverseShortTime:
        """Special nested class for casting InverseShortTime to subclasses."""

        def __init__(self, parent: 'InverseShortTime'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def inverse_short_time(self) -> 'InverseShortTime':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InverseShortTime.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'InverseShortTime._Cast_InverseShortTime':
        return self._Cast_InverseShortTime(self)
