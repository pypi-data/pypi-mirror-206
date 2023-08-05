"""_2221.py

OptimizationStrategyBase
"""
from mastapy.utility.databases import _1816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_STRATEGY_BASE = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'OptimizationStrategyBase')


__docformat__ = 'restructuredtext en'
__all__ = ('OptimizationStrategyBase',)


class OptimizationStrategyBase(_1816.NamedDatabaseItem):
    """OptimizationStrategyBase

    This is a mastapy class.
    """

    TYPE = _OPTIMIZATION_STRATEGY_BASE

    class _Cast_OptimizationStrategyBase:
        """Special nested class for casting OptimizationStrategyBase to subclasses."""

        def __init__(self, parent: 'OptimizationStrategyBase'):
            self._parent = parent

        @property
        def named_database_item(self):
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
        def optimization_strategy(self):
            from mastapy.system_model.optimization import _2220
            
            return self._parent._cast(_2220.OptimizationStrategy)

        @property
        def optimization_strategy_base(self) -> 'OptimizationStrategyBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OptimizationStrategyBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'OptimizationStrategyBase._Cast_OptimizationStrategyBase':
        return self._Cast_OptimizationStrategyBase(self)
