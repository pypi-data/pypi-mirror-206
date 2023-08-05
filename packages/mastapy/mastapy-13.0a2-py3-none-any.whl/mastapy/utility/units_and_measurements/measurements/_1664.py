"""_1664.py

LinearFlexibility
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_FLEXIBILITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LinearFlexibility')


__docformat__ = 'restructuredtext en'
__all__ = ('LinearFlexibility',)


class LinearFlexibility(_1594.MeasurementBase):
    """LinearFlexibility

    This is a mastapy class.
    """

    TYPE = _LINEAR_FLEXIBILITY

    class _Cast_LinearFlexibility:
        """Special nested class for casting LinearFlexibility to subclasses."""

        def __init__(self, parent: 'LinearFlexibility'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def linear_flexibility(self) -> 'LinearFlexibility':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LinearFlexibility.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LinearFlexibility._Cast_LinearFlexibility':
        return self._Cast_LinearFlexibility(self)
