"""_102.py

DynamicSolver
"""
from mastapy.nodal_analysis.system_solvers import _116
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_SOLVER = python_net_import('SMT.MastaAPI.NodalAnalysis.SystemSolvers', 'DynamicSolver')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicSolver',)


class DynamicSolver(_116.StiffnessSolver):
    """DynamicSolver

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_SOLVER

    class _Cast_DynamicSolver:
        """Special nested class for casting DynamicSolver to subclasses."""

        def __init__(self, parent: 'DynamicSolver'):
            self._parent = parent

        @property
        def stiffness_solver(self):
            return self._parent._cast(_116.StiffnessSolver)

        @property
        def solver(self):
            from mastapy.nodal_analysis.system_solvers import _114
            
            return self._parent._cast(_114.Solver)

        @property
        def backward_euler_acceleration_step_halving_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _99
            
            return self._parent._cast(_99.BackwardEulerAccelerationStepHalvingTransientSolver)

        @property
        def backward_euler_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _100
            
            return self._parent._cast(_100.BackwardEulerTransientSolver)

        @property
        def internal_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _103
            
            return self._parent._cast(_103.InternalTransientSolver)

        @property
        def lobatto_iiia_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _104
            
            return self._parent._cast(_104.LobattoIIIATransientSolver)

        @property
        def lobatto_iiic_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _105
            
            return self._parent._cast(_105.LobattoIIICTransientSolver)

        @property
        def newmark_acceleration_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _106
            
            return self._parent._cast(_106.NewmarkAccelerationTransientSolver)

        @property
        def newmark_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _107
            
            return self._parent._cast(_107.NewmarkTransientSolver)

        @property
        def semi_implicit_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _108
            
            return self._parent._cast(_108.SemiImplicitTransientSolver)

        @property
        def simple_acceleration_based_step_halving_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _109
            
            return self._parent._cast(_109.SimpleAccelerationBasedStepHalvingTransientSolver)

        @property
        def simple_velocity_based_step_halving_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _110
            
            return self._parent._cast(_110.SimpleVelocityBasedStepHalvingTransientSolver)

        @property
        def step_halving_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _115
            
            return self._parent._cast(_115.StepHalvingTransientSolver)

        @property
        def transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _117
            
            return self._parent._cast(_117.TransientSolver)

        @property
        def wilson_theta_transient_solver(self):
            from mastapy.nodal_analysis.system_solvers import _118
            
            return self._parent._cast(_118.WilsonThetaTransientSolver)

        @property
        def dynamic_solver(self) -> 'DynamicSolver':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicSolver.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DynamicSolver._Cast_DynamicSolver':
        return self._Cast_DynamicSolver(self)
