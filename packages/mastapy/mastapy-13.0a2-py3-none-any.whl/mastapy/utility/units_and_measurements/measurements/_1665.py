"""_1665.py

LinearStiffness
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_STIFFNESS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LinearStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('LinearStiffness',)


class LinearStiffness(_1594.MeasurementBase):
    """LinearStiffness

    This is a mastapy class.
    """

    TYPE = _LINEAR_STIFFNESS

    class _Cast_LinearStiffness:
        """Special nested class for casting LinearStiffness to subclasses."""

        def __init__(self, parent: 'LinearStiffness'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def linear_stiffness(self) -> 'LinearStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LinearStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LinearStiffness._Cast_LinearStiffness':
        return self._Cast_LinearStiffness(self)
