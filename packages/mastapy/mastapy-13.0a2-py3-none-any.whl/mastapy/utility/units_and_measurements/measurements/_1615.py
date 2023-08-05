"""_1615.py

CurrentPerLength
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CURRENT_PER_LENGTH = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'CurrentPerLength')


__docformat__ = 'restructuredtext en'
__all__ = ('CurrentPerLength',)


class CurrentPerLength(_1594.MeasurementBase):
    """CurrentPerLength

    This is a mastapy class.
    """

    TYPE = _CURRENT_PER_LENGTH

    class _Cast_CurrentPerLength:
        """Special nested class for casting CurrentPerLength to subclasses."""

        def __init__(self, parent: 'CurrentPerLength'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def current_per_length(self) -> 'CurrentPerLength':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CurrentPerLength.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CurrentPerLength._Cast_CurrentPerLength':
        return self._Cast_CurrentPerLength(self)
