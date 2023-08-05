"""_2539.py

RotorSpeedInputOptions
"""
from mastapy.utility_gui import _1833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTOR_SPEED_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'RotorSpeedInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('RotorSpeedInputOptions',)


class RotorSpeedInputOptions(_1833.ColumnInputOptions):
    """RotorSpeedInputOptions

    This is a mastapy class.
    """

    TYPE = _ROTOR_SPEED_INPUT_OPTIONS

    class _Cast_RotorSpeedInputOptions:
        """Special nested class for casting RotorSpeedInputOptions to subclasses."""

        def __init__(self, parent: 'RotorSpeedInputOptions'):
            self._parent = parent

        @property
        def column_input_options(self):
            return self._parent._cast(_1833.ColumnInputOptions)

        @property
        def rotor_speed_input_options(self) -> 'RotorSpeedInputOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RotorSpeedInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RotorSpeedInputOptions._Cast_RotorSpeedInputOptions':
        return self._Cast_RotorSpeedInputOptions(self)
