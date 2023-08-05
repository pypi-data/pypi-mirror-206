"""_1354.py

NonLinearDQModelMultipleOperatingPointsLoadCase
"""
from mastapy.electric_machines.load_cases_and_analyses import _1341, _1340, _1346
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_DQ_MODEL_MULTIPLE_OPERATING_POINTS_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'NonLinearDQModelMultipleOperatingPointsLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('NonLinearDQModelMultipleOperatingPointsLoadCase',)


class NonLinearDQModelMultipleOperatingPointsLoadCase(_1346.ElectricMachineLoadCaseBase):
    """NonLinearDQModelMultipleOperatingPointsLoadCase

    This is a mastapy class.
    """

    TYPE = _NON_LINEAR_DQ_MODEL_MULTIPLE_OPERATING_POINTS_LOAD_CASE

    class _Cast_NonLinearDQModelMultipleOperatingPointsLoadCase:
        """Special nested class for casting NonLinearDQModelMultipleOperatingPointsLoadCase to subclasses."""

        def __init__(self, parent: 'NonLinearDQModelMultipleOperatingPointsLoadCase'):
            self._parent = parent

        @property
        def electric_machine_load_case_base(self):
            return self._parent._cast(_1346.ElectricMachineLoadCaseBase)

        @property
        def dynamic_force_load_case(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1336
            
            return self._parent._cast(_1336.DynamicForceLoadCase)

        @property
        def efficiency_map_load_case(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1338
            
            return self._parent._cast(_1338.EfficiencyMapLoadCase)

        @property
        def speed_torque_curve_load_case(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1362
            
            return self._parent._cast(_1362.SpeedTorqueCurveLoadCase)

        @property
        def non_linear_dq_model_multiple_operating_points_load_case(self) -> 'NonLinearDQModelMultipleOperatingPointsLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NonLinearDQModelMultipleOperatingPointsLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def control_strategy(self) -> '_1341.ElectricMachineControlStrategy':
        """ElectricMachineControlStrategy: 'ControlStrategy' is the original name of this property."""

        temp = self.wrapped.ControlStrategy

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1341.ElectricMachineControlStrategy)
        return constructor.new_from_mastapy_type(_1341.ElectricMachineControlStrategy)(value) if value is not None else None

    @control_strategy.setter
    def control_strategy(self, value: '_1341.ElectricMachineControlStrategy'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1341.ElectricMachineControlStrategy.type_())
        self.wrapped.ControlStrategy = value

    @property
    def include_resistive_voltages(self) -> 'bool':
        """bool: 'IncludeResistiveVoltages' is the original name of this property."""

        temp = self.wrapped.IncludeResistiveVoltages

        if temp is None:
            return False

        return temp

    @include_resistive_voltages.setter
    def include_resistive_voltages(self, value: 'bool'):
        self.wrapped.IncludeResistiveVoltages = bool(value) if value else False

    @property
    def basic_mechanical_loss_settings(self) -> '_1340.ElectricMachineBasicMechanicalLossSettings':
        """ElectricMachineBasicMechanicalLossSettings: 'BasicMechanicalLossSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicMechanicalLossSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'NonLinearDQModelMultipleOperatingPointsLoadCase._Cast_NonLinearDQModelMultipleOperatingPointsLoadCase':
        return self._Cast_NonLinearDQModelMultipleOperatingPointsLoadCase(self)
