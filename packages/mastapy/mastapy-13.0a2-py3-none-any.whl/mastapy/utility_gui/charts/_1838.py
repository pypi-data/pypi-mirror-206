"""_1838.py

BubbleChartDefinition
"""
from mastapy.utility_gui.charts import _1847
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BUBBLE_CHART_DEFINITION = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'BubbleChartDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('BubbleChartDefinition',)


class BubbleChartDefinition(_1847.ScatterChartDefinition):
    """BubbleChartDefinition

    This is a mastapy class.
    """

    TYPE = _BUBBLE_CHART_DEFINITION

    class _Cast_BubbleChartDefinition:
        """Special nested class for casting BubbleChartDefinition to subclasses."""

        def __init__(self, parent: 'BubbleChartDefinition'):
            self._parent = parent

        @property
        def scatter_chart_definition(self):
            return self._parent._cast(_1847.ScatterChartDefinition)

        @property
        def two_d_chart_definition(self):
            from mastapy.utility_gui.charts import _1852
            
            return self._parent._cast(_1852.TwoDChartDefinition)

        @property
        def nd_chart_definition(self):
            from mastapy.utility_gui.charts import _1844
            
            return self._parent._cast(_1844.NDChartDefinition)

        @property
        def chart_definition(self):
            from mastapy.utility.report import _1737
            
            return self._parent._cast(_1737.ChartDefinition)

        @property
        def bubble_chart_definition(self) -> 'BubbleChartDefinition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BubbleChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BubbleChartDefinition._Cast_BubbleChartDefinition':
        return self._Cast_BubbleChartDefinition(self)
