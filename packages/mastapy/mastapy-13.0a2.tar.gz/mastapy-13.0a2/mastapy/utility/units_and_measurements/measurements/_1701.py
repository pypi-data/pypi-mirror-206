"""_1701.py

SquareRootOfUnitForcePerUnitArea
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SQUARE_ROOT_OF_UNIT_FORCE_PER_UNIT_AREA = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'SquareRootOfUnitForcePerUnitArea')


__docformat__ = 'restructuredtext en'
__all__ = ('SquareRootOfUnitForcePerUnitArea',)


class SquareRootOfUnitForcePerUnitArea(_1594.MeasurementBase):
    """SquareRootOfUnitForcePerUnitArea

    This is a mastapy class.
    """

    TYPE = _SQUARE_ROOT_OF_UNIT_FORCE_PER_UNIT_AREA

    class _Cast_SquareRootOfUnitForcePerUnitArea:
        """Special nested class for casting SquareRootOfUnitForcePerUnitArea to subclasses."""

        def __init__(self, parent: 'SquareRootOfUnitForcePerUnitArea'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def square_root_of_unit_force_per_unit_area(self) -> 'SquareRootOfUnitForcePerUnitArea':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SquareRootOfUnitForcePerUnitArea.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SquareRootOfUnitForcePerUnitArea._Cast_SquareRootOfUnitForcePerUnitArea':
        return self._Cast_SquareRootOfUnitForcePerUnitArea(self)
