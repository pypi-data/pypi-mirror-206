"""_1662.py

LinearAngularStiffnessCrossTerm
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_ANGULAR_STIFFNESS_CROSS_TERM = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LinearAngularStiffnessCrossTerm')


__docformat__ = 'restructuredtext en'
__all__ = ('LinearAngularStiffnessCrossTerm',)


class LinearAngularStiffnessCrossTerm(_1594.MeasurementBase):
    """LinearAngularStiffnessCrossTerm

    This is a mastapy class.
    """

    TYPE = _LINEAR_ANGULAR_STIFFNESS_CROSS_TERM

    class _Cast_LinearAngularStiffnessCrossTerm:
        """Special nested class for casting LinearAngularStiffnessCrossTerm to subclasses."""

        def __init__(self, parent: 'LinearAngularStiffnessCrossTerm'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def linear_angular_stiffness_cross_term(self) -> 'LinearAngularStiffnessCrossTerm':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LinearAngularStiffnessCrossTerm.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LinearAngularStiffnessCrossTerm._Cast_LinearAngularStiffnessCrossTerm':
        return self._Cast_LinearAngularStiffnessCrossTerm(self)
