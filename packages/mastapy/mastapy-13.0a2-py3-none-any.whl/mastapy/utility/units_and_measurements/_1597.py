"""_1597.py

SafetyFactorUnit
"""
from mastapy.utility.units_and_measurements import _1599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_UNIT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'SafetyFactorUnit')


__docformat__ = 'restructuredtext en'
__all__ = ('SafetyFactorUnit',)


class SafetyFactorUnit(_1599.Unit):
    """SafetyFactorUnit

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_UNIT

    class _Cast_SafetyFactorUnit:
        """Special nested class for casting SafetyFactorUnit to subclasses."""

        def __init__(self, parent: 'SafetyFactorUnit'):
            self._parent = parent

        @property
        def unit(self):
            return self._parent._cast(_1599.Unit)

        @property
        def safety_factor_unit(self) -> 'SafetyFactorUnit':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SafetyFactorUnit.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SafetyFactorUnit._Cast_SafetyFactorUnit':
        return self._Cast_SafetyFactorUnit(self)
