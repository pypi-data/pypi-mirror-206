"""_1851.py

ThreeDVectorChartDefinition
"""
from mastapy.utility_gui.charts import _1844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THREE_D_VECTOR_CHART_DEFINITION = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'ThreeDVectorChartDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('ThreeDVectorChartDefinition',)


class ThreeDVectorChartDefinition(_1844.NDChartDefinition):
    """ThreeDVectorChartDefinition

    This is a mastapy class.
    """

    TYPE = _THREE_D_VECTOR_CHART_DEFINITION

    class _Cast_ThreeDVectorChartDefinition:
        """Special nested class for casting ThreeDVectorChartDefinition to subclasses."""

        def __init__(self, parent: 'ThreeDVectorChartDefinition'):
            self._parent = parent

        @property
        def nd_chart_definition(self):
            return self._parent._cast(_1844.NDChartDefinition)

        @property
        def chart_definition(self):
            from mastapy.utility.report import _1737
            
            return self._parent._cast(_1737.ChartDefinition)

        @property
        def three_d_vector_chart_definition(self) -> 'ThreeDVectorChartDefinition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ThreeDVectorChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ThreeDVectorChartDefinition._Cast_ThreeDVectorChartDefinition':
        return self._Cast_ThreeDVectorChartDefinition(self)
