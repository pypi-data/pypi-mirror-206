"""_1538.py

ParetoOptimisationStrategy
"""
from typing import List

from mastapy.math_utility.optimisation import _1540, _1536, _1537
from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_STRATEGY = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'ParetoOptimisationStrategy')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoOptimisationStrategy',)


class ParetoOptimisationStrategy(_1816.NamedDatabaseItem):
    """ParetoOptimisationStrategy

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_STRATEGY

    class _Cast_ParetoOptimisationStrategy:
        """Special nested class for casting ParetoOptimisationStrategy to subclasses."""

        def __init__(self, parent: 'ParetoOptimisationStrategy'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def pareto_optimisation_strategy(self) -> 'ParetoOptimisationStrategy':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoOptimisationStrategy.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def charts(self) -> 'List[_1540.ParetoOptimisationStrategyChartInformation]':
        """List[ParetoOptimisationStrategyChartInformation]: 'Charts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Charts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def inputs(self) -> 'List[_1536.ParetoOptimisationInput]':
        """List[ParetoOptimisationInput]: 'Inputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Inputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def outputs(self) -> 'List[_1537.ParetoOptimisationOutput]':
        """List[ParetoOptimisationOutput]: 'Outputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Outputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_chart(self):
        """ 'AddChart' is the original name of this method."""

        self.wrapped.AddChart()

    @property
    def cast_to(self) -> 'ParetoOptimisationStrategy._Cast_ParetoOptimisationStrategy':
        return self._Cast_ParetoOptimisationStrategy(self)
