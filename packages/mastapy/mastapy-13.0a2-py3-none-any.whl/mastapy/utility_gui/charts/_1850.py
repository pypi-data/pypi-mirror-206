"""_1850.py

ThreeDChartDefinition
"""
from typing import List

from mastapy.utility.report import _1732
from mastapy._internal import constructor, conversion
from mastapy.math_utility import _1477
from mastapy.utility_gui.charts import _1846, _1844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THREE_D_CHART_DEFINITION = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'ThreeDChartDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('ThreeDChartDefinition',)


class ThreeDChartDefinition(_1844.NDChartDefinition):
    """ThreeDChartDefinition

    This is a mastapy class.
    """

    TYPE = _THREE_D_CHART_DEFINITION

    class _Cast_ThreeDChartDefinition:
        """Special nested class for casting ThreeDChartDefinition to subclasses."""

        def __init__(self, parent: 'ThreeDChartDefinition'):
            self._parent = parent

        @property
        def nd_chart_definition(self):
            return self._parent._cast(_1844.NDChartDefinition)

        @property
        def chart_definition(self):
            from mastapy.utility.report import _1737
            
            return self._parent._cast(_1737.ChartDefinition)

        @property
        def three_d_chart_definition(self) -> 'ThreeDChartDefinition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ThreeDChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def z_axis(self) -> '_1732.AxisSettings':
        """AxisSettings: 'ZAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZAxis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def x_axis_range(self) -> '_1477.Range':
        """Range: 'XAxisRange' is the original name of this property."""

        temp = self.wrapped.XAxisRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @x_axis_range.setter
    def x_axis_range(self, value: '_1477.Range'):
        value = value.wrapped if value else None
        self.wrapped.XAxisRange = value

    @property
    def y_axis_range(self) -> '_1477.Range':
        """Range: 'YAxisRange' is the original name of this property."""

        temp = self.wrapped.YAxisRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @y_axis_range.setter
    def y_axis_range(self, value: '_1477.Range'):
        value = value.wrapped if value else None
        self.wrapped.YAxisRange = value

    @property
    def z_axis_range(self) -> '_1477.Range':
        """Range: 'ZAxisRange' is the original name of this property."""

        temp = self.wrapped.ZAxisRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @z_axis_range.setter
    def z_axis_range(self, value: '_1477.Range'):
        value = value.wrapped if value else None
        self.wrapped.ZAxisRange = value

    def data_points_for_surfaces(self) -> 'List[_1846.PointsForSurface]':
        """ 'DataPointsForSurfaces' is the original name of this method.

        Returns:
            List[mastapy.utility_gui.charts.PointsForSurface]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.DataPointsForSurfaces())

    @property
    def cast_to(self) -> 'ThreeDChartDefinition._Cast_ThreeDChartDefinition':
        return self._Cast_ThreeDChartDefinition(self)
