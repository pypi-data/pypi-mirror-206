"""_2618.py

MultibodyDynamicsAnalysis
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5432
from mastapy.nodal_analysis.system_solvers import _117
from mastapy.system_model.analyses_and_results.analysis_cases import _7513
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'MultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MultibodyDynamicsAnalysis',)


class MultibodyDynamicsAnalysis(_7513.TimeSeriesLoadAnalysisCase):
    """MultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_MultibodyDynamicsAnalysis:
        """Special nested class for casting MultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'MultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def time_series_load_analysis_case(self):
            return self._parent._cast(_7513.TimeSeriesLoadAnalysisCase)

        @property
        def analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7497
            
            return self._parent._cast(_7497.AnalysisCase)

        @property
        def context(self):
            from mastapy.system_model.analyses_and_results import _2629
            
            return self._parent._cast(_2629.Context)

        @property
        def multibody_dynamics_analysis(self) -> 'MultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_interface_analysis_results_available(self) -> 'bool':
        """bool: 'HasInterfaceAnalysisResultsAvailable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasInterfaceAnalysisResultsAvailable

        if temp is None:
            return False

        return temp

    @property
    def percentage_time_spent_in_masta_solver(self) -> 'float':
        """float: 'PercentageTimeSpentInMASTASolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentageTimeSpentInMASTASolver

        if temp is None:
            return 0.0

        return temp

    @property
    def mbd_options(self) -> '_5432.MBDAnalysisOptions':
        """MBDAnalysisOptions: 'MBDOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MBDOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transient_solver(self) -> '_117.TransientSolver':
        """TransientSolver: 'TransientSolver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MultibodyDynamicsAnalysis._Cast_MultibodyDynamicsAnalysis':
        return self._Cast_MultibodyDynamicsAnalysis(self)
