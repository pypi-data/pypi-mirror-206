"""_100.py

BackwardEulerTransientSolver
"""
from mastapy.nodal_analysis.system_solvers import _110
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BACKWARD_EULER_TRANSIENT_SOLVER = python_net_import('SMT.MastaAPI.NodalAnalysis.SystemSolvers', 'BackwardEulerTransientSolver')


__docformat__ = 'restructuredtext en'
__all__ = ('BackwardEulerTransientSolver',)


class BackwardEulerTransientSolver(_110.SimpleVelocityBasedStepHalvingTransientSolver):
    """BackwardEulerTransientSolver

    This is a mastapy class.
    """

    TYPE = _BACKWARD_EULER_TRANSIENT_SOLVER

    class _Cast_BackwardEulerTransientSolver:
        """Special nested class for casting BackwardEulerTransientSolver to subclasses."""

        def __init__(self, parent: 'BackwardEulerTransientSolver'):
            self._parent = parent

        @property
        def simple_velocity_based_step_halving_transient_solver(self):
            return self._parent._cast(_110.SimpleVelocityBasedStepHalvingTransientSolver)

        @property
        def step_halving_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _115
            
            return self._parent._cast(_115.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _103
            
            return self._parent._cast(_103.InternalTransientSolver)

        @property
        def transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _117
            
            return self._parent._cast(_117.TransientSolver)

        @property
        def dynamic_solver(self):
            from mastapy.nodal_analysis.system_solvers import _102
            
            return self._parent._cast(_102.DynamicSolver)

        @property
        def stiffness_solver(self):
            from mastapy.nodal_analysis.system_solvers import _116
            
            return self._parent._cast(_116.StiffnessSolver)

        @property
        def solver(self):
            from mastapy.nodal_analysis.system_solvers import _114
            
            return self._parent._cast(_114.Solver)

        @property
        def backward_euler_transient_solver(self) -> 'BackwardEulerTransientSolver':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BackwardEulerTransientSolver.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BackwardEulerTransientSolver._Cast_BackwardEulerTransientSolver':
        return self._Cast_BackwardEulerTransientSolver(self)
