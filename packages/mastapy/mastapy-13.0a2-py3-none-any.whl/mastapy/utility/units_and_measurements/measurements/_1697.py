"""_1697.py

Rotatum
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTATUM = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Rotatum')


__docformat__ = 'restructuredtext en'
__all__ = ('Rotatum',)


class Rotatum(_1594.MeasurementBase):
    """Rotatum

    This is a mastapy class.
    """

    TYPE = _ROTATUM

    class _Cast_Rotatum:
        """Special nested class for casting Rotatum to subclasses."""

        def __init__(self, parent: 'Rotatum'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def rotatum(self) -> 'Rotatum':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Rotatum.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Rotatum._Cast_Rotatum':
        return self._Cast_Rotatum(self)
