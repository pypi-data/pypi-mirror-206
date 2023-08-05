"""_927.py

ParetoOptimiserChartInformation
"""
from mastapy.gears.gear_set_pareto_optimiser import _899, _906
from mastapy.gears.rating import _351
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISER_CHART_INFORMATION = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ParetoOptimiserChartInformation')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoOptimiserChartInformation',)


class ParetoOptimiserChartInformation(_899.ChartInfoBase['_351.AbstractGearSetRating', '_906.GearSetOptimiserCandidate']):
    """ParetoOptimiserChartInformation

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISER_CHART_INFORMATION

    class _Cast_ParetoOptimiserChartInformation:
        """Special nested class for casting ParetoOptimiserChartInformation to subclasses."""

        def __init__(self, parent: 'ParetoOptimiserChartInformation'):
            self._parent = parent

        @property
        def chart_info_base(self):
            return self._parent._cast(_899.ChartInfoBase)

        @property
        def pareto_optimiser_chart_information(self) -> 'ParetoOptimiserChartInformation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoOptimiserChartInformation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ParetoOptimiserChartInformation._Cast_ParetoOptimiserChartInformation':
        return self._Cast_ParetoOptimiserChartInformation(self)
