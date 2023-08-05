"""_6957.py

GearRatioInputOptions
"""
from mastapy._internal import constructor
from mastapy.utility_gui import _1833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_RATIO_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'GearRatioInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('GearRatioInputOptions',)


class GearRatioInputOptions(_1833.ColumnInputOptions):
    """GearRatioInputOptions

    This is a mastapy class.
    """

    TYPE = _GEAR_RATIO_INPUT_OPTIONS

    class _Cast_GearRatioInputOptions:
        """Special nested class for casting GearRatioInputOptions to subclasses."""

        def __init__(self, parent: 'GearRatioInputOptions'):
            self._parent = parent

        @property
        def column_input_options(self):
            return self._parent._cast(_1833.ColumnInputOptions)

        @property
        def gear_ratio_input_options(self) -> 'GearRatioInputOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearRatioInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_gear_ratio_column(self) -> 'bool':
        """bool: 'HasGearRatioColumn' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasGearRatioColumn

        if temp is None:
            return False

        return temp

    @property
    def tolerance(self) -> 'float':
        """float: 'Tolerance' is the original name of this property."""

        temp = self.wrapped.Tolerance

        if temp is None:
            return 0.0

        return temp

    @tolerance.setter
    def tolerance(self, value: 'float'):
        self.wrapped.Tolerance = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'GearRatioInputOptions._Cast_GearRatioInputOptions':
        return self._Cast_GearRatioInputOptions(self)
