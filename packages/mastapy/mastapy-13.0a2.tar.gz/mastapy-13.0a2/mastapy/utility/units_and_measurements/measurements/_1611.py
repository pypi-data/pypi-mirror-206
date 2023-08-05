"""_1611.py

Area
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AREA = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Area')


__docformat__ = 'restructuredtext en'
__all__ = ('Area',)


class Area(_1594.MeasurementBase):
    """Area

    This is a mastapy class.
    """

    TYPE = _AREA

    class _Cast_Area:
        """Special nested class for casting Area to subclasses."""

        def __init__(self, parent: 'Area'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def area(self) -> 'Area':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Area.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Area._Cast_Area':
        return self._Cast_Area(self)
