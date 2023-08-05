"""_1673.py

MassPerUnitTime
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_PER_UNIT_TIME = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MassPerUnitTime')


__docformat__ = 'restructuredtext en'
__all__ = ('MassPerUnitTime',)


class MassPerUnitTime(_1594.MeasurementBase):
    """MassPerUnitTime

    This is a mastapy class.
    """

    TYPE = _MASS_PER_UNIT_TIME

    class _Cast_MassPerUnitTime:
        """Special nested class for casting MassPerUnitTime to subclasses."""

        def __init__(self, parent: 'MassPerUnitTime'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def mass_per_unit_time(self) -> 'MassPerUnitTime':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MassPerUnitTime.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MassPerUnitTime._Cast_MassPerUnitTime':
        return self._Cast_MassPerUnitTime(self)
