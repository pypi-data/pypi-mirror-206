"""_1696.py

RescaledMeasurement
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESCALED_MEASUREMENT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'RescaledMeasurement')


__docformat__ = 'restructuredtext en'
__all__ = ('RescaledMeasurement',)


class RescaledMeasurement(_1594.MeasurementBase):
    """RescaledMeasurement

    This is a mastapy class.
    """

    TYPE = _RESCALED_MEASUREMENT

    class _Cast_RescaledMeasurement:
        """Special nested class for casting RescaledMeasurement to subclasses."""

        def __init__(self, parent: 'RescaledMeasurement'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def rescaled_measurement(self) -> 'RescaledMeasurement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RescaledMeasurement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RescaledMeasurement._Cast_RescaledMeasurement':
        return self._Cast_RescaledMeasurement(self)
