"""_1726.py

WearCoefficient
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WEAR_COEFFICIENT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'WearCoefficient')


__docformat__ = 'restructuredtext en'
__all__ = ('WearCoefficient',)


class WearCoefficient(_1594.MeasurementBase):
    """WearCoefficient

    This is a mastapy class.
    """

    TYPE = _WEAR_COEFFICIENT

    class _Cast_WearCoefficient:
        """Special nested class for casting WearCoefficient to subclasses."""

        def __init__(self, parent: 'WearCoefficient'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def wear_coefficient(self) -> 'WearCoefficient':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WearCoefficient.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'WearCoefficient._Cast_WearCoefficient':
        return self._Cast_WearCoefficient(self)
