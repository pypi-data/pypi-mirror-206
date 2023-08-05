"""_897.py

BarForPareto
"""
from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy.math_utility.optimisation import _1539
from mastapy.gears.analysis import _1211
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BAR_FOR_PARETO = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'BarForPareto')


__docformat__ = 'restructuredtext en'
__all__ = ('BarForPareto',)


TAnalysis = TypeVar('TAnalysis', bound='_1211.AbstractGearSetAnalysis')
TCandidate = TypeVar('TCandidate')


class BarForPareto(_1539.ParetoOptimisationStrategyBars, Generic[TAnalysis, TCandidate]):
    """BarForPareto

    This is a mastapy class.

    Generic Types:
        TAnalysis
        TCandidate
    """

    TYPE = _BAR_FOR_PARETO

    class _Cast_BarForPareto:
        """Special nested class for casting BarForPareto to subclasses."""

        def __init__(self, parent: 'BarForPareto'):
            self._parent = parent

        @property
        def pareto_optimisation_strategy_bars(self):
            return self._parent._cast(_1539.ParetoOptimisationStrategyBars)

        @property
        def bar_for_pareto(self) -> 'BarForPareto':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BarForPareto.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def remove_bar(self):
        """ 'RemoveBar' is the original name of this method."""

        self.wrapped.RemoveBar()

    @property
    def cast_to(self) -> 'BarForPareto._Cast_BarForPareto':
        return self._Cast_BarForPareto(self)
