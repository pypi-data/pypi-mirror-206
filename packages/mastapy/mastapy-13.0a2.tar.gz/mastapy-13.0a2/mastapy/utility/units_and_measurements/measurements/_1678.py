"""_1678.py

Percentage
"""
from mastapy.utility.units_and_measurements.measurements import _1635
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERCENTAGE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Percentage')


__docformat__ = 'restructuredtext en'
__all__ = ('Percentage',)


class Percentage(_1635.FractionMeasurementBase):
    """Percentage

    This is a mastapy class.
    """

    TYPE = _PERCENTAGE

    class _Cast_Percentage:
        """Special nested class for casting Percentage to subclasses."""

        def __init__(self, parent: 'Percentage'):
            self._parent = parent

        @property
        def fraction_measurement_base(self):
            return self._parent._cast(_1635.FractionMeasurementBase)

        @property
        def measurement_base(self):
            from mastapy.utility.units_and_measurements import _1594
            
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def percentage(self) -> 'Percentage':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Percentage.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Percentage._Cast_Percentage':
        return self._Cast_Percentage(self)
