"""_1592.py

EnumUnit
"""
from mastapy.utility.units_and_measurements import _1599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENUM_UNIT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'EnumUnit')


__docformat__ = 'restructuredtext en'
__all__ = ('EnumUnit',)


class EnumUnit(_1599.Unit):
    """EnumUnit

    This is a mastapy class.
    """

    TYPE = _ENUM_UNIT

    class _Cast_EnumUnit:
        """Special nested class for casting EnumUnit to subclasses."""

        def __init__(self, parent: 'EnumUnit'):
            self._parent = parent

        @property
        def unit(self):
            return self._parent._cast(_1599.Unit)

        @property
        def enum_unit(self) -> 'EnumUnit':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EnumUnit.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'EnumUnit._Cast_EnumUnit':
        return self._Cast_EnumUnit(self)
