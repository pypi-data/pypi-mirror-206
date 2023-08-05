"""_1680.py

PowerPerSmallArea
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_PER_SMALL_AREA = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'PowerPerSmallArea')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerPerSmallArea',)


class PowerPerSmallArea(_1594.MeasurementBase):
    """PowerPerSmallArea

    This is a mastapy class.
    """

    TYPE = _POWER_PER_SMALL_AREA

    class _Cast_PowerPerSmallArea:
        """Special nested class for casting PowerPerSmallArea to subclasses."""

        def __init__(self, parent: 'PowerPerSmallArea'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def power_per_small_area(self) -> 'PowerPerSmallArea':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PowerPerSmallArea.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PowerPerSmallArea._Cast_PowerPerSmallArea':
        return self._Cast_PowerPerSmallArea(self)
