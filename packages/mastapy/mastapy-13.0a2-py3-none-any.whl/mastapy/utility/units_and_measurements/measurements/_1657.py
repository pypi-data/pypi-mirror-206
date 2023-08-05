"""_1657.py

LengthToTheFourth
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_TO_THE_FOURTH = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LengthToTheFourth')


__docformat__ = 'restructuredtext en'
__all__ = ('LengthToTheFourth',)


class LengthToTheFourth(_1594.MeasurementBase):
    """LengthToTheFourth

    This is a mastapy class.
    """

    TYPE = _LENGTH_TO_THE_FOURTH

    class _Cast_LengthToTheFourth:
        """Special nested class for casting LengthToTheFourth to subclasses."""

        def __init__(self, parent: 'LengthToTheFourth'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def length_to_the_fourth(self) -> 'LengthToTheFourth':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LengthToTheFourth.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LengthToTheFourth._Cast_LengthToTheFourth':
        return self._Cast_LengthToTheFourth(self)
