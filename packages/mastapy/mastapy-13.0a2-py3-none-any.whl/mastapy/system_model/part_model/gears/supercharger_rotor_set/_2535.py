"""_2535.py

InputPowerInputOptions
"""
from mastapy.utility_gui import _1833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INPUT_POWER_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'InputPowerInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('InputPowerInputOptions',)


class InputPowerInputOptions(_1833.ColumnInputOptions):
    """InputPowerInputOptions

    This is a mastapy class.
    """

    TYPE = _INPUT_POWER_INPUT_OPTIONS

    class _Cast_InputPowerInputOptions:
        """Special nested class for casting InputPowerInputOptions to subclasses."""

        def __init__(self, parent: 'InputPowerInputOptions'):
            self._parent = parent

        @property
        def column_input_options(self):
            return self._parent._cast(_1833.ColumnInputOptions)

        @property
        def input_power_input_options(self) -> 'InputPowerInputOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InputPowerInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'InputPowerInputOptions._Cast_InputPowerInputOptions':
        return self._Cast_InputPowerInputOptions(self)
