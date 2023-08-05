"""_2212.py

ConicalGearOptimizationStep
"""
from mastapy.system_model.optimization import _2219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_OPTIMIZATION_STEP = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'ConicalGearOptimizationStep')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearOptimizationStep',)


class ConicalGearOptimizationStep(_2219.OptimizationStep):
    """ConicalGearOptimizationStep

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_OPTIMIZATION_STEP

    class _Cast_ConicalGearOptimizationStep:
        """Special nested class for casting ConicalGearOptimizationStep to subclasses."""

        def __init__(self, parent: 'ConicalGearOptimizationStep'):
            self._parent = parent

        @property
        def optimization_step(self):
            return self._parent._cast(_2219.OptimizationStep)

        @property
        def conical_gear_optimization_step(self) -> 'ConicalGearOptimizationStep':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearOptimizationStep.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearOptimizationStep._Cast_ConicalGearOptimizationStep':
        return self._Cast_ConicalGearOptimizationStep(self)
