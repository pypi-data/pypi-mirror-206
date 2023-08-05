"""_2222.py

OptimizationStrategyDatabase
"""
from mastapy.utility.databases import _1815
from mastapy.system_model.optimization import _2214
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'OptimizationStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('OptimizationStrategyDatabase',)


class OptimizationStrategyDatabase(_1815.NamedDatabase['_2214.CylindricalGearOptimisationStrategy']):
    """OptimizationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _OPTIMIZATION_STRATEGY_DATABASE

    class _Cast_OptimizationStrategyDatabase:
        """Special nested class for casting OptimizationStrategyDatabase to subclasses."""

        def __init__(self, parent: 'OptimizationStrategyDatabase'):
            self._parent = parent

        @property
        def named_database(self):
            return self._parent._cast(_1815.NamedDatabase)

        @property
        def sql_database(self):
            from mastapy.utility.databases import _1818, _1817
            
            return self._parent._cast(_1818.SQLDatabase)

        @property
        def database(self):
            from mastapy.utility.databases import _1811, _1817
            
            return self._parent._cast(_1811.Database)

        @property
        def optimization_strategy_database(self) -> 'OptimizationStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OptimizationStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'OptimizationStrategyDatabase._Cast_OptimizationStrategyDatabase':
        return self._Cast_OptimizationStrategyDatabase(self)
