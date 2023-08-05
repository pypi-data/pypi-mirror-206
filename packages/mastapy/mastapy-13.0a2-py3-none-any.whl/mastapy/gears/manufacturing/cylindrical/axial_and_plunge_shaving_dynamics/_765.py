"""_765.py

ShavingDynamicsViewModel
"""
from typing import List, TypeVar, Generic

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _744, _761, _756, _766,
    _760
)
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1021, _1073
from mastapy.utility_gui.charts import _1852
from mastapy._internal.implicit import enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVING_DYNAMICS_VIEW_MODEL = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ShavingDynamicsViewModel')


__docformat__ = 'restructuredtext en'
__all__ = ('ShavingDynamicsViewModel',)


T = TypeVar('T', bound='_760.ShavingDynamics')


class ShavingDynamicsViewModel(_766.ShavingDynamicsViewModelBase, Generic[T]):
    """ShavingDynamicsViewModel

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _SHAVING_DYNAMICS_VIEW_MODEL

    class _Cast_ShavingDynamicsViewModel:
        """Special nested class for casting ShavingDynamicsViewModel to subclasses."""

        def __init__(self, parent: 'ShavingDynamicsViewModel'):
            self._parent = parent

        @property
        def shaving_dynamics_view_model_base(self):
            return self._parent._cast(_766.ShavingDynamicsViewModelBase)

        @property
        def gear_manufacturing_configuration_view_model(self):
            from mastapy.gears.manufacturing.cylindrical import _623
            
            return self._parent._cast(_623.GearManufacturingConfigurationViewModel)

        @property
        def conventional_shaving_dynamics_view_model(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _749
            
            return self._parent._cast(_749.ConventionalShavingDynamicsViewModel)

        @property
        def plunge_shaving_dynamics_view_model(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _755
            
            return self._parent._cast(_755.PlungeShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model(self) -> 'ShavingDynamicsViewModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShavingDynamicsViewModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_profile_range_calculation_source(self) -> '_744.ActiveProfileRangeCalculationSource':
        """ActiveProfileRangeCalculationSource: 'ActiveProfileRangeCalculationSource' is the original name of this property."""

        temp = self.wrapped.ActiveProfileRangeCalculationSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _744.ActiveProfileRangeCalculationSource)
        return constructor.new_from_mastapy_type(_744.ActiveProfileRangeCalculationSource)(value) if value is not None else None

    @active_profile_range_calculation_source.setter
    def active_profile_range_calculation_source(self, value: '_744.ActiveProfileRangeCalculationSource'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _744.ActiveProfileRangeCalculationSource.type_())
        self.wrapped.ActiveProfileRangeCalculationSource = value

    @property
    def chart_display_method(self) -> '_1021.CylindricalGearProfileMeasurementType':
        """CylindricalGearProfileMeasurementType: 'ChartDisplayMethod' is the original name of this property."""

        temp = self.wrapped.ChartDisplayMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1021.CylindricalGearProfileMeasurementType)
        return constructor.new_from_mastapy_type(_1021.CylindricalGearProfileMeasurementType)(value) if value is not None else None

    @chart_display_method.setter
    def chart_display_method(self, value: '_1021.CylindricalGearProfileMeasurementType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1021.CylindricalGearProfileMeasurementType.type_())
        self.wrapped.ChartDisplayMethod = value

    @property
    def redressing_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'RedressingChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_measurement_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ThicknessType':
        """enum_with_selected_value.EnumWithSelectedValue_ThicknessType: 'SelectedMeasurementMethod' is the original name of this property."""

        temp = self.wrapped.SelectedMeasurementMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ThicknessType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @selected_measurement_method.setter
    def selected_measurement_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ThicknessType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ThicknessType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SelectedMeasurementMethod = value

    @property
    def shaver_tip_diameter_adjustment(self) -> 'float':
        """float: 'ShaverTipDiameterAdjustment' is the original name of this property."""

        temp = self.wrapped.ShaverTipDiameterAdjustment

        if temp is None:
            return 0.0

        return temp

    @shaver_tip_diameter_adjustment.setter
    def shaver_tip_diameter_adjustment(self, value: 'float'):
        self.wrapped.ShaverTipDiameterAdjustment = float(value) if value else 0.0

    @property
    def use_shaver_from_database(self) -> 'bool':
        """bool: 'UseShaverFromDatabase' is the original name of this property."""

        temp = self.wrapped.UseShaverFromDatabase

        if temp is None:
            return False

        return temp

    @use_shaver_from_database.setter
    def use_shaver_from_database(self, value: 'bool'):
        self.wrapped.UseShaverFromDatabase = bool(value) if value else False

    @property
    def calculation(self) -> '_761.ShavingDynamicsCalculation[T]':
        """ShavingDynamicsCalculation[T]: 'Calculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Calculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp) if temp is not None else None

    @property
    def redressing_settings(self) -> 'List[_756.RedressingSettings[T]]':
        """List[RedressingSettings[T]]: 'RedressingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingSettings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_shaver_to_database(self):
        """ 'AddShaverToDatabase' is the original name of this method."""

        self.wrapped.AddShaverToDatabase()

    def calculate(self):
        """ 'Calculate' is the original name of this method."""

        self.wrapped.Calculate()

    @property
    def cast_to(self) -> 'ShavingDynamicsViewModel._Cast_ShavingDynamicsViewModel':
        return self._Cast_ShavingDynamicsViewModel(self)
