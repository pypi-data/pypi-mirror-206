"""_108.py

SemiImplicitTransientSolver
"""
from mastapy.nodal_analysis.system_solvers import _103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SEMI_IMPLICIT_TRANSIENT_SOLVER = python_net_import('SMT.MastaAPI.NodalAnalysis.SystemSolvers', 'SemiImplicitTransientSolver')


__docformat__ = 'restructuredtext en'
__all__ = ('SemiImplicitTransientSolver',)


class SemiImplicitTransientSolver(_103.InternalTransientSolver):
    """SemiImplicitTransientSolver

    This is a mastapy class.
    """

    TYPE = _SEMI_IMPLICIT_TRANSIENT_SOLVER

    class _Cast_SemiImplicitTransientSolver:
        """Special nested class for casting SemiImplicitTransientSolver to subclasses."""

        def __init__(self, parent: 'SemiImplicitTransientSolver'):
            self._parent = parent

        @property
        def internal_transient_solver(self):
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
        def semi_implicit_transient_solver(self) -> 'SemiImplicitTransientSolver':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SemiImplicitTransientSolver.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SemiImplicitTransientSolver._Cast_SemiImplicitTransientSolver':
        return self._Cast_SemiImplicitTransientSolver(self)
