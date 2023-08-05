"""_1775.py

SimpleChartDefinition
"""
from mastapy.utility.report import _1737
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SIMPLE_CHART_DEFINITION = python_net_import('SMT.MastaAPI.Utility.Report', 'SimpleChartDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('SimpleChartDefinition',)


class SimpleChartDefinition(_1737.ChartDefinition):
    """SimpleChartDefinition

    This is a mastapy class.
    """

    TYPE = _SIMPLE_CHART_DEFINITION

    class _Cast_SimpleChartDefinition:
        """Special nested class for casting SimpleChartDefinition to subclasses."""

        def __init__(self, parent: 'SimpleChartDefinition'):
            self._parent = parent

        @property
        def chart_definition(self):
            return self._parent._cast(_1737.ChartDefinition)

        @property
        def simple_chart_definition(self) -> 'SimpleChartDefinition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SimpleChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SimpleChartDefinition._Cast_SimpleChartDefinition':
        return self._Cast_SimpleChartDefinition(self)
