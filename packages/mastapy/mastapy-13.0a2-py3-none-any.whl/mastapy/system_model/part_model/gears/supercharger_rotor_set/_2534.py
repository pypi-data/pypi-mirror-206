"""_2534.py

BoostPressureInputOptions
"""
from mastapy.utility_gui import _1833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOOST_PRESSURE_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'BoostPressureInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('BoostPressureInputOptions',)


class BoostPressureInputOptions(_1833.ColumnInputOptions):
    """BoostPressureInputOptions

    This is a mastapy class.
    """

    TYPE = _BOOST_PRESSURE_INPUT_OPTIONS

    class _Cast_BoostPressureInputOptions:
        """Special nested class for casting BoostPressureInputOptions to subclasses."""

        def __init__(self, parent: 'BoostPressureInputOptions'):
            self._parent = parent

        @property
        def column_input_options(self):
            return self._parent._cast(_1833.ColumnInputOptions)

        @property
        def boost_pressure_input_options(self) -> 'BoostPressureInputOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoostPressureInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BoostPressureInputOptions._Cast_BoostPressureInputOptions':
        return self._Cast_BoostPressureInputOptions(self)
