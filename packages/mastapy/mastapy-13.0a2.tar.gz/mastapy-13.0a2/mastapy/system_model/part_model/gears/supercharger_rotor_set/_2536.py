"""_2536.py

PressureRatioInputOptions
"""
from mastapy._internal import constructor
from mastapy.utility_gui import _1833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRESSURE_RATIO_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'PressureRatioInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('PressureRatioInputOptions',)


class PressureRatioInputOptions(_1833.ColumnInputOptions):
    """PressureRatioInputOptions

    This is a mastapy class.
    """

    TYPE = _PRESSURE_RATIO_INPUT_OPTIONS

    class _Cast_PressureRatioInputOptions:
        """Special nested class for casting PressureRatioInputOptions to subclasses."""

        def __init__(self, parent: 'PressureRatioInputOptions'):
            self._parent = parent

        @property
        def column_input_options(self):
            return self._parent._cast(_1833.ColumnInputOptions)

        @property
        def pressure_ratio_input_options(self) -> 'PressureRatioInputOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PressureRatioInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def reference_pressure(self) -> 'float':
        """float: 'ReferencePressure' is the original name of this property."""

        temp = self.wrapped.ReferencePressure

        if temp is None:
            return 0.0

        return temp

    @reference_pressure.setter
    def reference_pressure(self, value: 'float'):
        self.wrapped.ReferencePressure = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'PressureRatioInputOptions._Cast_PressureRatioInputOptions':
        return self._Cast_PressureRatioInputOptions(self)
