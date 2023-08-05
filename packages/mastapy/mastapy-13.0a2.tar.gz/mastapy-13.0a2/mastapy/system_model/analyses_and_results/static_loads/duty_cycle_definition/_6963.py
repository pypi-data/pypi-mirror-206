"""_6963.py

RampOrSteadyStateInputOptions
"""
from mastapy.utility_gui import _1833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RAMP_OR_STEADY_STATE_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'RampOrSteadyStateInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('RampOrSteadyStateInputOptions',)


class RampOrSteadyStateInputOptions(_1833.ColumnInputOptions):
    """RampOrSteadyStateInputOptions

    This is a mastapy class.
    """

    TYPE = _RAMP_OR_STEADY_STATE_INPUT_OPTIONS

    class _Cast_RampOrSteadyStateInputOptions:
        """Special nested class for casting RampOrSteadyStateInputOptions to subclasses."""

        def __init__(self, parent: 'RampOrSteadyStateInputOptions'):
            self._parent = parent

        @property
        def column_input_options(self):
            return self._parent._cast(_1833.ColumnInputOptions)

        @property
        def ramp_or_steady_state_input_options(self) -> 'RampOrSteadyStateInputOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RampOrSteadyStateInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RampOrSteadyStateInputOptions._Cast_RampOrSteadyStateInputOptions':
        return self._Cast_RampOrSteadyStateInputOptions(self)
