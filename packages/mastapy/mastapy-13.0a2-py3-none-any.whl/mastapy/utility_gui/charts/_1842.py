"""_1842.py

LegacyChartMathChartDefinition
"""
from mastapy.utility.report import _1737
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEGACY_CHART_MATH_CHART_DEFINITION = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'LegacyChartMathChartDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('LegacyChartMathChartDefinition',)


class LegacyChartMathChartDefinition(_1737.ChartDefinition):
    """LegacyChartMathChartDefinition

    This is a mastapy class.
    """

    TYPE = _LEGACY_CHART_MATH_CHART_DEFINITION

    class _Cast_LegacyChartMathChartDefinition:
        """Special nested class for casting LegacyChartMathChartDefinition to subclasses."""

        def __init__(self, parent: 'LegacyChartMathChartDefinition'):
            self._parent = parent

        @property
        def chart_definition(self):
            return self._parent._cast(_1737.ChartDefinition)

        @property
        def legacy_chart_math_chart_definition(self) -> 'LegacyChartMathChartDefinition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LegacyChartMathChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LegacyChartMathChartDefinition._Cast_LegacyChartMathChartDefinition':
        return self._Cast_LegacyChartMathChartDefinition(self)
