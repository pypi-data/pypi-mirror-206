"""_1619.py

DataSize
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_SIZE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'DataSize')


__docformat__ = 'restructuredtext en'
__all__ = ('DataSize',)


class DataSize(_1594.MeasurementBase):
    """DataSize

    This is a mastapy class.
    """

    TYPE = _DATA_SIZE

    class _Cast_DataSize:
        """Special nested class for casting DataSize to subclasses."""

        def __init__(self, parent: 'DataSize'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def data_size(self) -> 'DataSize':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DataSize.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DataSize._Cast_DataSize':
        return self._Cast_DataSize(self)
