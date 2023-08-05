"""_2220.py

OptimizationStrategy
"""
from typing import TypeVar, Generic

from mastapy.system_model.optimization import _2221, _2219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_STRATEGY = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'OptimizationStrategy')


__docformat__ = 'restructuredtext en'
__all__ = ('OptimizationStrategy',)


TStep = TypeVar('TStep', bound='_2219.OptimizationStep')


class OptimizationStrategy(_2221.OptimizationStrategyBase, Generic[TStep]):
    """OptimizationStrategy

    This is a mastapy class.

    Generic Types:
        TStep
    """

    TYPE = _OPTIMIZATION_STRATEGY

    class _Cast_OptimizationStrategy:
        """Special nested class for casting OptimizationStrategy to subclasses."""

        def __init__(self, parent: 'OptimizationStrategy'):
            self._parent = parent

        @property
        def optimization_strategy_base(self):
            return self._parent._cast(_2221.OptimizationStrategyBase)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def conical_gear_optimisation_strategy(self):
            from mastapy.system_model.optimization import _2211
            
            return self._parent._cast(_2211.ConicalGearOptimisationStrategy)

        @property
        def cylindrical_gear_optimisation_strategy(self):
            from mastapy.system_model.optimization import _2214
            
            return self._parent._cast(_2214.CylindricalGearOptimisationStrategy)

        @property
        def optimization_strategy(self) -> 'OptimizationStrategy':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OptimizationStrategy.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'OptimizationStrategy._Cast_OptimizationStrategy':
        return self._Cast_OptimizationStrategy(self)
