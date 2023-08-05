"""_1716.py

TorqueConverterK
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_K = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'TorqueConverterK')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterK',)


class TorqueConverterK(_1594.MeasurementBase):
    """TorqueConverterK

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_K

    class _Cast_TorqueConverterK:
        """Special nested class for casting TorqueConverterK to subclasses."""

        def __init__(self, parent: 'TorqueConverterK'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def torque_converter_k(self) -> 'TorqueConverterK':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterK.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TorqueConverterK._Cast_TorqueConverterK':
        return self._Cast_TorqueConverterK(self)
