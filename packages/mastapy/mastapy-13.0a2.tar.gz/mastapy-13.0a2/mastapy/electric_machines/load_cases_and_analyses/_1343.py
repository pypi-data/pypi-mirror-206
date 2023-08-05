"""_1343.py

ElectricMachineFEAnalysis
"""
from mastapy._internal import constructor
from mastapy.electric_machines.results import _1310
from mastapy.nodal_analysis.elmer import _169
from mastapy.electric_machines.load_cases_and_analyses import _1357
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_FE_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineFEAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineFEAnalysis',)


class ElectricMachineFEAnalysis(_1357.SingleOperatingPointAnalysis):
    """ElectricMachineFEAnalysis

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_FE_ANALYSIS

    class _Cast_ElectricMachineFEAnalysis:
        """Special nested class for casting ElectricMachineFEAnalysis to subclasses."""

        def __init__(self, parent: 'ElectricMachineFEAnalysis'):
            self._parent = parent

        @property
        def single_operating_point_analysis(self):
            return self._parent._cast(_1357.SingleOperatingPointAnalysis)

        @property
        def electric_machine_analysis(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1339
            
            return self._parent._cast(_1339.ElectricMachineAnalysis)

        @property
        def electric_machine_fe_analysis(self) -> 'ElectricMachineFEAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineFEAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electro_magnetic_solver_analysis_time(self) -> 'float':
        """float: 'ElectroMagneticSolverAnalysisTime' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectroMagneticSolverAnalysisTime

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_force_results(self) -> '_1310.DynamicForceResults':
        """DynamicForceResults: 'DynamicForceResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicForceResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def viewable(self) -> '_169.ElmerResultsViewable':
        """ElmerResultsViewable: 'Viewable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Viewable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ElectricMachineFEAnalysis._Cast_ElectricMachineFEAnalysis':
        return self._Cast_ElectricMachineFEAnalysis(self)
