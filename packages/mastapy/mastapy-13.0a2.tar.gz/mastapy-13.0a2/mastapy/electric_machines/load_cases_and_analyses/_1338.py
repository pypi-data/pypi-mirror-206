"""_1338.py

EfficiencyMapLoadCase
"""
from mastapy.electric_machines.load_cases_and_analyses import _1342, _1337, _1354
from mastapy._internal import constructor
from mastapy.electric_machines import _1259
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EFFICIENCY_MAP_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'EfficiencyMapLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('EfficiencyMapLoadCase',)


class EfficiencyMapLoadCase(_1354.NonLinearDQModelMultipleOperatingPointsLoadCase):
    """EfficiencyMapLoadCase

    This is a mastapy class.
    """

    TYPE = _EFFICIENCY_MAP_LOAD_CASE

    class _Cast_EfficiencyMapLoadCase:
        """Special nested class for casting EfficiencyMapLoadCase to subclasses."""

        def __init__(self, parent: 'EfficiencyMapLoadCase'):
            self._parent = parent

        @property
        def non_linear_dq_model_multiple_operating_points_load_case(self):
            return self._parent._cast(_1354.NonLinearDQModelMultipleOperatingPointsLoadCase)

        @property
        def electric_machine_load_case_base(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1346
            
            return self._parent._cast(_1346.ElectricMachineLoadCaseBase)

        @property
        def efficiency_map_load_case(self) -> 'EfficiencyMapLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EfficiencyMapLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def efficiency_map_settings(self) -> '_1342.ElectricMachineEfficiencyMapSettings':
        """ElectricMachineEfficiencyMapSettings: 'EfficiencyMapSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EfficiencyMapSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def analysis_for(self, setup: '_1259.ElectricMachineSetup') -> '_1337.EfficiencyMapAnalysis':
        """ 'AnalysisFor' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.EfficiencyMapAnalysis
        """

        method_result = self.wrapped.AnalysisFor(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'EfficiencyMapLoadCase._Cast_EfficiencyMapLoadCase':
        return self._Cast_EfficiencyMapLoadCase(self)
