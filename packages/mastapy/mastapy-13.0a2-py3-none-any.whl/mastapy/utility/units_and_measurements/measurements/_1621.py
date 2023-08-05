"""_1621.py

Density
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DENSITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Density')


__docformat__ = 'restructuredtext en'
__all__ = ('Density',)


class Density(_1594.MeasurementBase):
    """Density

    This is a mastapy class.
    """

    TYPE = _DENSITY

    class _Cast_Density:
        """Special nested class for casting Density to subclasses."""

        def __init__(self, parent: 'Density'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def density(self) -> 'Density':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Density.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Density._Cast_Density':
        return self._Cast_Density(self)
