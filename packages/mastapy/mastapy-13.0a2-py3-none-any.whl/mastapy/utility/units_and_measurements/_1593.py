"""_1593.py

InverseUnit
"""
from mastapy.utility.units_and_measurements import _1599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INVERSE_UNIT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'InverseUnit')


__docformat__ = 'restructuredtext en'
__all__ = ('InverseUnit',)


class InverseUnit(_1599.Unit):
    """InverseUnit

    This is a mastapy class.
    """

    TYPE = _INVERSE_UNIT

    class _Cast_InverseUnit:
        """Special nested class for casting InverseUnit to subclasses."""

        def __init__(self, parent: 'InverseUnit'):
            self._parent = parent

        @property
        def unit(self):
            return self._parent._cast(_1599.Unit)

        @property
        def inverse_unit(self) -> 'InverseUnit':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InverseUnit.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'InverseUnit._Cast_InverseUnit':
        return self._Cast_InverseUnit(self)
