"""_1624.py

ElectricCurrent
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_CURRENT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'ElectricCurrent')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricCurrent',)


class ElectricCurrent(_1594.MeasurementBase):
    """ElectricCurrent

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_CURRENT

    class _Cast_ElectricCurrent:
        """Special nested class for casting ElectricCurrent to subclasses."""

        def __init__(self, parent: 'ElectricCurrent'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def electric_current(self) -> 'ElectricCurrent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricCurrent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricCurrent._Cast_ElectricCurrent':
        return self._Cast_ElectricCurrent(self)
