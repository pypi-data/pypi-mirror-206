"""_1852.py

TwoDChartDefinition
"""
from typing import List

from mastapy.utility_gui.charts import _1839, _1848, _1844
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TWO_D_CHART_DEFINITION = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'TwoDChartDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('TwoDChartDefinition',)


class TwoDChartDefinition(_1844.NDChartDefinition):
    """TwoDChartDefinition

    This is a mastapy class.
    """

    TYPE = _TWO_D_CHART_DEFINITION

    class _Cast_TwoDChartDefinition:
        """Special nested class for casting TwoDChartDefinition to subclasses."""

        def __init__(self, parent: 'TwoDChartDefinition'):
            self._parent = parent

        @property
        def nd_chart_definition(self):
            return self._parent._cast(_1844.NDChartDefinition)

        @property
        def chart_definition(self):
            from mastapy.utility.report import _1737
            
            return self._parent._cast(_1737.ChartDefinition)

        @property
        def bubble_chart_definition(self):
            from mastapy.utility_gui.charts import _1838
            
            return self._parent._cast(_1838.BubbleChartDefinition)

        @property
        def parallel_coordinates_chart_definition(self):
            from mastapy.utility_gui.charts import _1845
            
            return self._parent._cast(_1845.ParallelCoordinatesChartDefinition)

        @property
        def scatter_chart_definition(self):
            from mastapy.utility_gui.charts import _1847
            
            return self._parent._cast(_1847.ScatterChartDefinition)

        @property
        def two_d_chart_definition(self) -> 'TwoDChartDefinition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TwoDChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def const_lines(self) -> 'List[_1839.ConstantLine]':
        """List[ConstantLine]: 'ConstLines' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConstLines

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def series_list(self) -> 'List[_1848.Series2D]':
        """List[Series2D]: 'SeriesList' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeriesList

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'TwoDChartDefinition._Cast_TwoDChartDefinition':
        return self._Cast_TwoDChartDefinition(self)
