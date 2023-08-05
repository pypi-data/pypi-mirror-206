"""_1658.py

LengthVeryLong
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_VERY_LONG = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LengthVeryLong')


__docformat__ = 'restructuredtext en'
__all__ = ('LengthVeryLong',)


class LengthVeryLong(_1594.MeasurementBase):
    """LengthVeryLong

    This is a mastapy class.
    """

    TYPE = _LENGTH_VERY_LONG

    class _Cast_LengthVeryLong:
        """Special nested class for casting LengthVeryLong to subclasses."""

        def __init__(self, parent: 'LengthVeryLong'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def length_very_long(self) -> 'LengthVeryLong':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LengthVeryLong.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LengthVeryLong._Cast_LengthVeryLong':
        return self._Cast_LengthVeryLong(self)
