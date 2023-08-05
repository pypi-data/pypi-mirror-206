"""_1629.py

Enum
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENUM = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Enum')


__docformat__ = 'restructuredtext en'
__all__ = ('Enum',)


class Enum(_1594.MeasurementBase):
    """Enum

    This is a mastapy class.
    """

    TYPE = _ENUM

    class _Cast_Enum:
        """Special nested class for casting Enum to subclasses."""

        def __init__(self, parent: 'Enum'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def enum(self) -> 'Enum':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Enum.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Enum._Cast_Enum':
        return self._Cast_Enum(self)
