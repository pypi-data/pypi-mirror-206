"""_1645.py

Impulse
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_IMPULSE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Impulse')


__docformat__ = 'restructuredtext en'
__all__ = ('Impulse',)


class Impulse(_1594.MeasurementBase):
    """Impulse

    This is a mastapy class.
    """

    TYPE = _IMPULSE

    class _Cast_Impulse:
        """Special nested class for casting Impulse to subclasses."""

        def __init__(self, parent: 'Impulse'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def impulse(self) -> 'Impulse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Impulse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Impulse._Cast_Impulse':
        return self._Cast_Impulse(self)
