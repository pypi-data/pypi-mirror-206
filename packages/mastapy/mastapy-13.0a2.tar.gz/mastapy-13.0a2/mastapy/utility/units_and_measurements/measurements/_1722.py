"""_1722.py

Viscosity
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VISCOSITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Viscosity')


__docformat__ = 'restructuredtext en'
__all__ = ('Viscosity',)


class Viscosity(_1594.MeasurementBase):
    """Viscosity

    This is a mastapy class.
    """

    TYPE = _VISCOSITY

    class _Cast_Viscosity:
        """Special nested class for casting Viscosity to subclasses."""

        def __init__(self, parent: 'Viscosity'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def viscosity(self) -> 'Viscosity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Viscosity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Viscosity._Cast_Viscosity':
        return self._Cast_Viscosity(self)
