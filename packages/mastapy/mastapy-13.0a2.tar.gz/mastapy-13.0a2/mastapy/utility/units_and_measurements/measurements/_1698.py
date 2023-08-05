"""_1698.py

SafetyFactor
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'SafetyFactor')


__docformat__ = 'restructuredtext en'
__all__ = ('SafetyFactor',)


class SafetyFactor(_1594.MeasurementBase):
    """SafetyFactor

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR

    class _Cast_SafetyFactor:
        """Special nested class for casting SafetyFactor to subclasses."""

        def __init__(self, parent: 'SafetyFactor'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def safety_factor(self) -> 'SafetyFactor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SafetyFactor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SafetyFactor._Cast_SafetyFactor':
        return self._Cast_SafetyFactor(self)
