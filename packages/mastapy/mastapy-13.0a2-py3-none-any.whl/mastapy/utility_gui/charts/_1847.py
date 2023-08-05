"""_1847.py

ScatterChartDefinition
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.utility_gui.charts import _1852
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCATTER_CHART_DEFINITION = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'ScatterChartDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('ScatterChartDefinition',)


class ScatterChartDefinition(_1852.TwoDChartDefinition):
    """ScatterChartDefinition

    This is a mastapy class.
    """

    TYPE = _SCATTER_CHART_DEFINITION

    class _Cast_ScatterChartDefinition:
        """Special nested class for casting ScatterChartDefinition to subclasses."""

        def __init__(self, parent: 'ScatterChartDefinition'):
            self._parent = parent

        @property
        def two_d_chart_definition(self):
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
        def bubble_chart_definition(self):
            from mastapy.utility_gui.charts import _1838
            
            return self._parent._cast(_1838.BubbleChartDefinition)

        @property
        def scatter_chart_definition(self) -> 'ScatterChartDefinition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ScatterChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x_values(self) -> 'List[float]':
        """List[float]: 'XValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.XValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def y_values(self) -> 'List[float]':
        """List[float]: 'YValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.YValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def z_axis_title(self) -> 'str':
        """str: 'ZAxisTitle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZAxisTitle

        if temp is None:
            return ''

        return temp

    @property
    def z_values(self) -> 'List[float]':
        """List[float]: 'ZValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def cast_to(self) -> 'ScatterChartDefinition._Cast_ScatterChartDefinition':
        return self._Cast_ScatterChartDefinition(self)
