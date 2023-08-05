"""_1689.py

PressurePerUnitTime
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRESSURE_PER_UNIT_TIME = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'PressurePerUnitTime')


__docformat__ = 'restructuredtext en'
__all__ = ('PressurePerUnitTime',)


class PressurePerUnitTime(_1594.MeasurementBase):
    """PressurePerUnitTime

    This is a mastapy class.
    """

    TYPE = _PRESSURE_PER_UNIT_TIME

    class _Cast_PressurePerUnitTime:
        """Special nested class for casting PressurePerUnitTime to subclasses."""

        def __init__(self, parent: 'PressurePerUnitTime'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def pressure_per_unit_time(self) -> 'PressurePerUnitTime':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PressurePerUnitTime.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PressurePerUnitTime._Cast_PressurePerUnitTime':
        return self._Cast_PressurePerUnitTime(self)
