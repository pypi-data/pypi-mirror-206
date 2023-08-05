"""_1660.py

LengthVeryShortPerLengthShort
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_VERY_SHORT_PER_LENGTH_SHORT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LengthVeryShortPerLengthShort')


__docformat__ = 'restructuredtext en'
__all__ = ('LengthVeryShortPerLengthShort',)


class LengthVeryShortPerLengthShort(_1594.MeasurementBase):
    """LengthVeryShortPerLengthShort

    This is a mastapy class.
    """

    TYPE = _LENGTH_VERY_SHORT_PER_LENGTH_SHORT

    class _Cast_LengthVeryShortPerLengthShort:
        """Special nested class for casting LengthVeryShortPerLengthShort to subclasses."""

        def __init__(self, parent: 'LengthVeryShortPerLengthShort'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def length_very_short_per_length_short(self) -> 'LengthVeryShortPerLengthShort':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LengthVeryShortPerLengthShort.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LengthVeryShortPerLengthShort._Cast_LengthVeryShortPerLengthShort':
        return self._Cast_LengthVeryShortPerLengthShort(self)
