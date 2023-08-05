"""_1653.py

LengthLong
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_LONG = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LengthLong')


__docformat__ = 'restructuredtext en'
__all__ = ('LengthLong',)


class LengthLong(_1594.MeasurementBase):
    """LengthLong

    This is a mastapy class.
    """

    TYPE = _LENGTH_LONG

    class _Cast_LengthLong:
        """Special nested class for casting LengthLong to subclasses."""

        def __init__(self, parent: 'LengthLong'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def length_long(self) -> 'LengthLong':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LengthLong.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LengthLong._Cast_LengthLong':
        return self._Cast_LengthLong(self)
