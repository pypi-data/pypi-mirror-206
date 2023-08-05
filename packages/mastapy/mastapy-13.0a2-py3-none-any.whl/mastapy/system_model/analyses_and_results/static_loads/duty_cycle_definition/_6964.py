"""_6964.py

SpeedInputOptions
"""
from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6962
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPEED_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'SpeedInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('SpeedInputOptions',)


class SpeedInputOptions(_6962.PowerLoadInputOptions):
    """SpeedInputOptions

    This is a mastapy class.
    """

    TYPE = _SPEED_INPUT_OPTIONS

    class _Cast_SpeedInputOptions:
        """Special nested class for casting SpeedInputOptions to subclasses."""

        def __init__(self, parent: 'SpeedInputOptions'):
            self._parent = parent

        @property
        def power_load_input_options(self):
            return self._parent._cast(_6962.PowerLoadInputOptions)

        @property
        def column_input_options(self):
            from mastapy.utility_gui import _1833
            
            return self._parent._cast(_1833.ColumnInputOptions)

        @property
        def speed_input_options(self) -> 'SpeedInputOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpeedInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SpeedInputOptions._Cast_SpeedInputOptions':
        return self._Cast_SpeedInputOptions(self)
