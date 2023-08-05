"""_639.py

GearPointCalculationError
"""
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _637
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_POINT_CALCULATION_ERROR = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving', 'GearPointCalculationError')


__docformat__ = 'restructuredtext en'
__all__ = ('GearPointCalculationError',)


class GearPointCalculationError(_637.CalculationError):
    """GearPointCalculationError

    This is a mastapy class.
    """

    TYPE = _GEAR_POINT_CALCULATION_ERROR

    class _Cast_GearPointCalculationError:
        """Special nested class for casting GearPointCalculationError to subclasses."""

        def __init__(self, parent: 'GearPointCalculationError'):
            self._parent = parent

        @property
        def calculation_error(self):
            return self._parent._cast(_637.CalculationError)

        @property
        def gear_point_calculation_error(self) -> 'GearPointCalculationError':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearPointCalculationError.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearPointCalculationError._Cast_GearPointCalculationError':
        return self._Cast_GearPointCalculationError(self)
