"""_607.py

CylindricalGearManufacturingConfig
"""
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.gears.manufacturing.cylindrical import _618, _619, _606
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.cylindrical import _1007
from mastapy.gears.manufacturing.cylindrical.cutters import _708
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _734, _737, _728
from mastapy.gears.manufacturing.cylindrical.process_simulation import _634
from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import _1083
from mastapy.gears.analysis import _1215
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CYLINDRICAL_GEAR_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalGearManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearManufacturingConfig',)


class CylindricalGearManufacturingConfig(_1215.GearImplementationDetail):
    """CylindricalGearManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MANUFACTURING_CONFIG

    class _Cast_CylindricalGearManufacturingConfig:
        """Special nested class for casting CylindricalGearManufacturingConfig to subclasses."""

        def __init__(self, parent: 'CylindricalGearManufacturingConfig'):
            self._parent = parent

        @property
        def gear_implementation_detail(self):
            return self._parent._cast(_1215.GearImplementationDetail)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(self) -> 'CylindricalGearManufacturingConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def finish_cutter_database_selector(self) -> 'str':
        """str: 'FinishCutterDatabaseSelector' is the original name of this property."""

        temp = self.wrapped.FinishCutterDatabaseSelector.SelectedItemName

        if temp is None:
            return ''

        return temp

    @finish_cutter_database_selector.setter
    def finish_cutter_database_selector(self, value: 'str'):
        self.wrapped.FinishCutterDatabaseSelector.SetSelectedItem(str(value) if value else '')

    @property
    def finishing_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods':
        """enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods: 'FinishingMethod' is the original name of this property."""

        temp = self.wrapped.FinishingMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @finishing_method.setter
    def finishing_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.FinishingMethod = value

    @property
    def limiting_finish_depth_radius_mean(self) -> 'float':
        """float: 'LimitingFinishDepthRadiusMean' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LimitingFinishDepthRadiusMean

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_finish_depth_radius(self) -> 'float':
        """float: 'MeanFinishDepthRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanFinishDepthRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_finish_cutter_gear_root_clearance_factor(self) -> 'float':
        """float: 'MinimumFinishCutterGearRootClearanceFactor' is the original name of this property."""

        temp = self.wrapped.MinimumFinishCutterGearRootClearanceFactor

        if temp is None:
            return 0.0

        return temp

    @minimum_finish_cutter_gear_root_clearance_factor.setter
    def minimum_finish_cutter_gear_root_clearance_factor(self, value: 'float'):
        self.wrapped.MinimumFinishCutterGearRootClearanceFactor = float(value) if value else 0.0

    @property
    def minimum_finish_depth_radius(self) -> 'float':
        """float: 'MinimumFinishDepthRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFinishDepthRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_points_for_reporting_main_profile_finish_stock(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfPointsForReportingMainProfileFinishStock' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsForReportingMainProfileFinishStock

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else 0

    @number_of_points_for_reporting_main_profile_finish_stock.setter
    def number_of_points_for_reporting_main_profile_finish_stock(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfPointsForReportingMainProfileFinishStock = value

    @property
    def rough_cutter_database_selector(self) -> 'str':
        """str: 'RoughCutterDatabaseSelector' is the original name of this property."""

        temp = self.wrapped.RoughCutterDatabaseSelector.SelectedItemName

        if temp is None:
            return ''

        return temp

    @rough_cutter_database_selector.setter
    def rough_cutter_database_selector(self, value: 'str'):
        self.wrapped.RoughCutterDatabaseSelector.SetSelectedItem(str(value) if value else '')

    @property
    def roughing_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods':
        """enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods: 'RoughingMethod' is the original name of this property."""

        temp = self.wrapped.RoughingMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @roughing_method.setter
    def roughing_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.RoughingMethod = value

    @property
    def design(self) -> '_1007.CylindricalGearDesign':
        """CylindricalGearDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter(self) -> '_708.CylindricalGearRealCutterDesign':
        """CylindricalGearRealCutterDesign: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter_simulation(self) -> '_734.GearCutterSimulation':
        """GearCutterSimulation: 'FinishCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutterSimulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_manufacturing_process_controls(self) -> '_737.ManufacturingProcessControls':
        """ManufacturingProcessControls: 'FinishManufacturingProcessControls' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishManufacturingProcessControls

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_process_simulation(self) -> '_634.CutterProcessSimulation':
        """CutterProcessSimulation: 'FinishProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishProcessSimulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_stock_specification(self) -> '_1083.FinishStockSpecification':
        """FinishStockSpecification: 'FinishStockSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishStockSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finished_gear_specification(self) -> '_728.CylindricalGearSpecification':
        """CylindricalGearSpecification: 'FinishedGearSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishedGearSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_blank(self) -> '_606.CylindricalGearBlank':
        """CylindricalGearBlank: 'GearBlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter(self) -> '_708.CylindricalGearRealCutterDesign':
        """CylindricalGearRealCutterDesign: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter_simulation(self) -> '_734.GearCutterSimulation':
        """GearCutterSimulation: 'RoughCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutterSimulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_gear_specification(self) -> '_728.CylindricalGearSpecification':
        """CylindricalGearSpecification: 'RoughGearSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughGearSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_manufacturing_process_controls(self) -> '_737.ManufacturingProcessControls':
        """ManufacturingProcessControls: 'RoughManufacturingProcessControls' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughManufacturingProcessControls

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_process_simulation(self) -> '_634.CutterProcessSimulation':
        """CutterProcessSimulation: 'RoughProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughProcessSimulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def create_new_finish_cutter_compatible_with_gear_in_design_mode(self):
        """ 'CreateNewFinishCutterCompatibleWithGearInDesignMode' is the original name of this method."""

        self.wrapped.CreateNewFinishCutterCompatibleWithGearInDesignMode()

    def create_new_rough_cutter_compatible_with_gear_in_design_mode(self):
        """ 'CreateNewRoughCutterCompatibleWithGearInDesignMode' is the original name of this method."""

        self.wrapped.CreateNewRoughCutterCompatibleWithGearInDesignMode()

    @property
    def cast_to(self) -> 'CylindricalGearManufacturingConfig._Cast_CylindricalGearManufacturingConfig':
        return self._Cast_CylindricalGearManufacturingConfig(self)
