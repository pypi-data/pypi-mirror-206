"""_1601.py

Acceleration
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACCELERATION = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Acceleration')


__docformat__ = 'restructuredtext en'
__all__ = ('Acceleration',)


class Acceleration(_1594.MeasurementBase):
    """Acceleration

    This is a mastapy class.
    """

    TYPE = _ACCELERATION

    class _Cast_Acceleration:
        """Special nested class for casting Acceleration to subclasses."""

        def __init__(self, parent: 'Acceleration'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def acceleration(self) -> 'Acceleration':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Acceleration.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Acceleration._Cast_Acceleration':
        return self._Cast_Acceleration(self)
