"""_6958.py

LoadCaseNameOptions
"""
from mastapy.utility_gui import _1833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOAD_CASE_NAME_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'LoadCaseNameOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadCaseNameOptions',)


class LoadCaseNameOptions(_1833.ColumnInputOptions):
    """LoadCaseNameOptions

    This is a mastapy class.
    """

    TYPE = _LOAD_CASE_NAME_OPTIONS

    class _Cast_LoadCaseNameOptions:
        """Special nested class for casting LoadCaseNameOptions to subclasses."""

        def __init__(self, parent: 'LoadCaseNameOptions'):
            self._parent = parent

        @property
        def column_input_options(self):
            return self._parent._cast(_1833.ColumnInputOptions)

        @property
        def load_case_name_options(self) -> 'LoadCaseNameOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadCaseNameOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadCaseNameOptions._Cast_LoadCaseNameOptions':
        return self._Cast_LoadCaseNameOptions(self)
