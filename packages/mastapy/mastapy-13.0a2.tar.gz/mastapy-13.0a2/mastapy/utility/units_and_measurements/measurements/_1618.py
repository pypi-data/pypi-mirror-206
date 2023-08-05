"""_1618.py

DamageRate
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DAMAGE_RATE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'DamageRate')


__docformat__ = 'restructuredtext en'
__all__ = ('DamageRate',)


class DamageRate(_1594.MeasurementBase):
    """DamageRate

    This is a mastapy class.
    """

    TYPE = _DAMAGE_RATE

    class _Cast_DamageRate:
        """Special nested class for casting DamageRate to subclasses."""

        def __init__(self, parent: 'DamageRate'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def damage_rate(self) -> 'DamageRate':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DamageRate.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DamageRate._Cast_DamageRate':
        return self._Cast_DamageRate(self)
