"""_6956.py

ForceInputOptions
"""
from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6961
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'ForceInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('ForceInputOptions',)


class ForceInputOptions(_6961.PointLoadInputOptions):
    """ForceInputOptions

    This is a mastapy class.
    """

    TYPE = _FORCE_INPUT_OPTIONS

    class _Cast_ForceInputOptions:
        """Special nested class for casting ForceInputOptions to subclasses."""

        def __init__(self, parent: 'ForceInputOptions'):
            self._parent = parent

        @property
        def point_load_input_options(self):
            return self._parent._cast(_6961.PointLoadInputOptions)

        @property
        def column_input_options(self):
            from mastapy.utility_gui import _1833
            
            return self._parent._cast(_1833.ColumnInputOptions)

        @property
        def force_input_options(self) -> 'ForceInputOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ForceInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ForceInputOptions._Cast_ForceInputOptions':
        return self._Cast_ForceInputOptions(self)
