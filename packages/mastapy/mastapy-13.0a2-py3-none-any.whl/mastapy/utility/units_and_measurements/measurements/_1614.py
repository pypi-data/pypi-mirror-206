"""_1614.py

CurrentDensity
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CURRENT_DENSITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'CurrentDensity')


__docformat__ = 'restructuredtext en'
__all__ = ('CurrentDensity',)


class CurrentDensity(_1594.MeasurementBase):
    """CurrentDensity

    This is a mastapy class.
    """

    TYPE = _CURRENT_DENSITY

    class _Cast_CurrentDensity:
        """Special nested class for casting CurrentDensity to subclasses."""

        def __init__(self, parent: 'CurrentDensity'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def current_density(self) -> 'CurrentDensity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CurrentDensity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CurrentDensity._Cast_CurrentDensity':
        return self._Cast_CurrentDensity(self)
