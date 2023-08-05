"""_1625.py

Energy
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENERGY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Energy')


__docformat__ = 'restructuredtext en'
__all__ = ('Energy',)


class Energy(_1594.MeasurementBase):
    """Energy

    This is a mastapy class.
    """

    TYPE = _ENERGY

    class _Cast_Energy:
        """Special nested class for casting Energy to subclasses."""

        def __init__(self, parent: 'Energy'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def energy(self) -> 'Energy':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Energy.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Energy._Cast_Energy':
        return self._Cast_Energy(self)
