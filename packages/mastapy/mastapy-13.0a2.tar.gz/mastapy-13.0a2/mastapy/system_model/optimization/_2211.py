"""_2211.py

ConicalGearOptimisationStrategy
"""
from mastapy.system_model.optimization import _2220, _2212
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_OPTIMISATION_STRATEGY = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'ConicalGearOptimisationStrategy')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearOptimisationStrategy',)


class ConicalGearOptimisationStrategy(_2220.OptimizationStrategy['_2212.ConicalGearOptimizationStep']):
    """ConicalGearOptimisationStrategy

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_OPTIMISATION_STRATEGY

    class _Cast_ConicalGearOptimisationStrategy:
        """Special nested class for casting ConicalGearOptimisationStrategy to subclasses."""

        def __init__(self, parent: 'ConicalGearOptimisationStrategy'):
            self._parent = parent

        @property
        def optimization_strategy(self):
            return self._parent._cast(_2220.OptimizationStrategy)

        @property
        def optimization_strategy_base(self):
            from mastapy.system_model.optimization import _2221
            
            return self._parent._cast(_2221.OptimizationStrategyBase)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def conical_gear_optimisation_strategy(self) -> 'ConicalGearOptimisationStrategy':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearOptimisationStrategy.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearOptimisationStrategy._Cast_ConicalGearOptimisationStrategy':
        return self._Cast_ConicalGearOptimisationStrategy(self)
