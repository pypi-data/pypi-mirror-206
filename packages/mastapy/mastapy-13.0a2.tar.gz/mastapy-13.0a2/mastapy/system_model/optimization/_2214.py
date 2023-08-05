"""_2214.py

CylindricalGearOptimisationStrategy
"""
from mastapy.system_model.optimization import _2220, _2215
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_OPTIMISATION_STRATEGY = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'CylindricalGearOptimisationStrategy')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearOptimisationStrategy',)


class CylindricalGearOptimisationStrategy(_2220.OptimizationStrategy['_2215.CylindricalGearOptimizationStep']):
    """CylindricalGearOptimisationStrategy

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_OPTIMISATION_STRATEGY

    class _Cast_CylindricalGearOptimisationStrategy:
        """Special nested class for casting CylindricalGearOptimisationStrategy to subclasses."""

        def __init__(self, parent: 'CylindricalGearOptimisationStrategy'):
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
        def cylindrical_gear_optimisation_strategy(self) -> 'CylindricalGearOptimisationStrategy':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearOptimisationStrategy.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearOptimisationStrategy._Cast_CylindricalGearOptimisationStrategy':
        return self._Cast_CylindricalGearOptimisationStrategy(self)
