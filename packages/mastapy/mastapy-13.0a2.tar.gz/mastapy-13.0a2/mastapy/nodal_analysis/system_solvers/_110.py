"""_110.py

SimpleVelocityBasedStepHalvingTransientSolver
"""
from mastapy.nodal_analysis.system_solvers import _115
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SIMPLE_VELOCITY_BASED_STEP_HALVING_TRANSIENT_SOLVER = python_net_import('SMT.MastaAPI.NodalAnalysis.SystemSolvers', 'SimpleVelocityBasedStepHalvingTransientSolver')


__docformat__ = 'restructuredtext en'
__all__ = ('SimpleVelocityBasedStepHalvingTransientSolver',)


class SimpleVelocityBasedStepHalvingTransientSolver(_115.StepHalvingTransientSolver):
    """SimpleVelocityBasedStepHalvingTransientSolver

    This is a mastapy class.
    """

    TYPE = _SIMPLE_VELOCITY_BASED_STEP_HALVING_TRANSIENT_SOLVER

    class _Cast_SimpleVelocityBasedStepHalvingTransientSolver:
        """Special nested class for casting SimpleVelocityBasedStepHalvingTransientSolver to subclasses."""

        def __init__(self, parent: 'SimpleVelocityBasedStepHalvingTransientSolver'):
            self._parent = parent

        @property
        def step_halving_transient_solver(self):
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
        def backward_euler_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _100
            
            return self._parent._cast(_100.BackwardEulerTransientSolver)

        @property
        def lobatto_iiia_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _104
            
            return self._parent._cast(_104.LobattoIIIATransientSolver)

        @property
        def newmark_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _107
            
            return self._parent._cast(_107.NewmarkTransientSolver)

        @property
        def simple_velocity_based_step_halving_transient_solver(self) -> 'SimpleVelocityBasedStepHalvingTransientSolver':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SimpleVelocityBasedStepHalvingTransientSolver.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SimpleVelocityBasedStepHalvingTransientSolver._Cast_SimpleVelocityBasedStepHalvingTransientSolver':
        return self._Cast_SimpleVelocityBasedStepHalvingTransientSolver(self)
