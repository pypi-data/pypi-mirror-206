"""_1649.py

InverseShortLength
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INVERSE_SHORT_LENGTH = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'InverseShortLength')


__docformat__ = 'restructuredtext en'
__all__ = ('InverseShortLength',)


class InverseShortLength(_1594.MeasurementBase):
    """InverseShortLength

    This is a mastapy class.
    """

    TYPE = _INVERSE_SHORT_LENGTH

    class _Cast_InverseShortLength:
        """Special nested class for casting InverseShortLength to subclasses."""

        def __init__(self, parent: 'InverseShortLength'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def inverse_short_length(self) -> 'InverseShortLength':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InverseShortLength.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'InverseShortLength._Cast_InverseShortLength':
        return self._Cast_InverseShortLength(self)
