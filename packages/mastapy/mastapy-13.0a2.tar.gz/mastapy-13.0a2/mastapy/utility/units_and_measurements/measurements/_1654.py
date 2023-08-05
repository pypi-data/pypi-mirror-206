"""_1654.py

LengthMedium
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_MEDIUM = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LengthMedium')


__docformat__ = 'restructuredtext en'
__all__ = ('LengthMedium',)


class LengthMedium(_1594.MeasurementBase):
    """LengthMedium

    This is a mastapy class.
    """

    TYPE = _LENGTH_MEDIUM

    class _Cast_LengthMedium:
        """Special nested class for casting LengthMedium to subclasses."""

        def __init__(self, parent: 'LengthMedium'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def length_medium(self) -> 'LengthMedium':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LengthMedium.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LengthMedium._Cast_LengthMedium':
        return self._Cast_LengthMedium(self)
