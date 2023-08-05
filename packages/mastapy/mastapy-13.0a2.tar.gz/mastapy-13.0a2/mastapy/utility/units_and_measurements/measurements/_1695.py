"""_1695.py

QuadraticDrag
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_QUADRATIC_DRAG = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'QuadraticDrag')


__docformat__ = 'restructuredtext en'
__all__ = ('QuadraticDrag',)


class QuadraticDrag(_1594.MeasurementBase):
    """QuadraticDrag

    This is a mastapy class.
    """

    TYPE = _QUADRATIC_DRAG

    class _Cast_QuadraticDrag:
        """Special nested class for casting QuadraticDrag to subclasses."""

        def __init__(self, parent: 'QuadraticDrag'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def quadratic_drag(self) -> 'QuadraticDrag':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'QuadraticDrag.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'QuadraticDrag._Cast_QuadraticDrag':
        return self._Cast_QuadraticDrag(self)
