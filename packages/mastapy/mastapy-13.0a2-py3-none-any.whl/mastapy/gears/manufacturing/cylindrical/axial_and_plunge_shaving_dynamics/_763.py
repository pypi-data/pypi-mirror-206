"""_763.py

ShavingDynamicsCalculationForHobbedGears
"""
from typing import List, TypeVar

from mastapy.utility_gui.charts import _1852
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.cylindrical import _1020
from mastapy._internal.python_net import python_net_import
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _759, _756, _761, _760
)
from mastapy._internal.cast_exception import CastException

_REPORTING_OVERRIDABLE = python_net_import('SMT.MastaAPI.Utility.Property', 'ReportingOverridable')
_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ShavingDynamicsCalculationForHobbedGears')


__docformat__ = 'restructuredtext en'
__all__ = ('ShavingDynamicsCalculationForHobbedGears',)


T = TypeVar('T', bound='_760.ShavingDynamics')


class ShavingDynamicsCalculationForHobbedGears(_761.ShavingDynamicsCalculation[T]):
    """ShavingDynamicsCalculationForHobbedGears

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS

    class _Cast_ShavingDynamicsCalculationForHobbedGears:
        """Special nested class for casting ShavingDynamicsCalculationForHobbedGears to subclasses."""

        def __init__(self, parent: 'ShavingDynamicsCalculationForHobbedGears'):
            self._parent = parent

        @property
        def shaving_dynamics_calculation(self):
            return self._parent._cast(_761.ShavingDynamicsCalculation)

        @property
        def conventional_shaving_dynamics_calculation_for_hobbed_gears(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _748
            
            return self._parent._cast(_748.ConventionalShavingDynamicsCalculationForHobbedGears)

        @property
        def plunge_shaving_dynamics_calculation_for_hobbed_gears(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _754
            
            return self._parent._cast(_754.PlungeShavingDynamicsCalculationForHobbedGears)

        @property
        def shaving_dynamics_calculation_for_hobbed_gears(self) -> 'ShavingDynamicsCalculationForHobbedGears':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShavingDynamicsCalculationForHobbedGears.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def redressing_chart_maximum_start_and_end_of_shaving_profile(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'RedressingChartMaximumStartAndEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingChartMaximumStartAndEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_chart_maximum_start_and_minimum_end_of_shaving_profile(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'RedressingChartMaximumStartAndMinimumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingChartMaximumStartAndMinimumEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_chart_minimum_start_and_end_of_shaving_profile(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'RedressingChartMinimumStartAndEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingChartMinimumStartAndEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_chart_minimum_start_and_maximum_end_of_shaving_profile(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'RedressingChartMinimumStartAndMaximumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingChartMinimumStartAndMaximumEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_redressing(self) -> 'list_with_selected_item.ListWithSelectedItem_T':
        """list_with_selected_item.ListWithSelectedItem_T: 'SelectedRedressing' is the original name of this property."""

        temp = self.wrapped.SelectedRedressing

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_T)(temp) if temp is not None else None

    @selected_redressing.setter
    def selected_redressing(self, value: 'list_with_selected_item.ListWithSelectedItem_T.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_T.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_T.implicit_type()
        value = wrapper_type[enclosed_type](value if value is not None else None)
        self.wrapped.SelectedRedressing = value

    @property
    def maximum_end_of_shaving_profile(self) -> '_1020.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'MaximumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumEndOfShavingProfile.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_start_of_shaving_profile(self) -> '_1020.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'MaximumStartOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumStartOfShavingProfile.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_end_of_shaving_profile(self) -> '_1020.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'MinimumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumEndOfShavingProfile.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_start_of_shaving_profile(self) -> '_1020.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'MinimumStartOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumStartOfShavingProfile.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_at_maximum_start_and_end_of_shaving_profile(self) -> '_759.ShaverRedressing[T]':
        """ShaverRedressing[T]: 'RedressingAtMaximumStartAndEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMaximumStartAndEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp) if temp is not None else None

    @property
    def redressing_at_maximum_start_and_minimum_end_of_shaving_profile(self) -> '_759.ShaverRedressing[T]':
        """ShaverRedressing[T]: 'RedressingAtMaximumStartAndMinimumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMaximumStartAndMinimumEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp) if temp is not None else None

    @property
    def redressing_at_minimum_start_and_end_of_shaving_profile(self) -> '_759.ShaverRedressing[T]':
        """ShaverRedressing[T]: 'RedressingAtMinimumStartAndEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMinimumStartAndEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp) if temp is not None else None

    @property
    def redressing_at_minimum_start_and_maximum_end_of_shaving_profile(self) -> '_759.ShaverRedressing[T]':
        """ShaverRedressing[T]: 'RedressingAtMinimumStartAndMaximumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMinimumStartAndMaximumEndOfShavingProfile

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

    @property
    def cast_to(self) -> 'ShavingDynamicsCalculationForHobbedGears._Cast_ShavingDynamicsCalculationForHobbedGears':
        return self._Cast_ShavingDynamicsCalculationForHobbedGears(self)
