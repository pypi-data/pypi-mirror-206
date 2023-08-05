"""_789.py

ConicalWheelManufacturingConfig
"""
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _819, _816
from mastapy.gears.manufacturing.bevel.cutters import _810, _811
from mastapy.gears.manufacturing.bevel import _771
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CONICAL_WHEEL_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalWheelManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalWheelManufacturingConfig',)


class ConicalWheelManufacturingConfig(_771.ConicalGearManufacturingConfig):
    """ConicalWheelManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_WHEEL_MANUFACTURING_CONFIG

    class _Cast_ConicalWheelManufacturingConfig:
        """Special nested class for casting ConicalWheelManufacturingConfig to subclasses."""

        def __init__(self, parent: 'ConicalWheelManufacturingConfig'):
            self._parent = parent

        @property
        def conical_gear_manufacturing_config(self):
            return self._parent._cast(_771.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _773
            
            return self._parent._cast(_773.ConicalGearMicroGeometryConfigBase)

        @property
        def gear_implementation_detail(self):
            from mastapy.gears.analysis import _1215
            
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
        def conical_wheel_manufacturing_config(self) -> 'ConicalWheelManufacturingConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalWheelManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def use_cutter_tilt(self) -> 'bool':
        """bool: 'UseCutterTilt' is the original name of this property."""

        temp = self.wrapped.UseCutterTilt

        if temp is None:
            return False

        return temp

    @use_cutter_tilt.setter
    def use_cutter_tilt(self, value: 'bool'):
        self.wrapped.UseCutterTilt = bool(value) if value else False

    @property
    def wheel_finish_manufacturing_machine(self) -> 'str':
        """str: 'WheelFinishManufacturingMachine' is the original name of this property."""

        temp = self.wrapped.WheelFinishManufacturingMachine.SelectedItemName

        if temp is None:
            return ''

        return temp

    @wheel_finish_manufacturing_machine.setter
    def wheel_finish_manufacturing_machine(self, value: 'str'):
        self.wrapped.WheelFinishManufacturingMachine.SetSelectedItem(str(value) if value else '')

    @property
    def wheel_rough_manufacturing_machine(self) -> 'str':
        """str: 'WheelRoughManufacturingMachine' is the original name of this property."""

        temp = self.wrapped.WheelRoughManufacturingMachine.SelectedItemName

        if temp is None:
            return ''

        return temp

    @wheel_rough_manufacturing_machine.setter
    def wheel_rough_manufacturing_machine(self, value: 'str'):
        self.wrapped.WheelRoughManufacturingMachine.SetSelectedItem(str(value) if value else '')

    @property
    def specified_cradle_style_machine_settings(self) -> '_819.CradleStyleConicalMachineSettingsGenerated':
        """CradleStyleConicalMachineSettingsGenerated: 'SpecifiedCradleStyleMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecifiedCradleStyleMachineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def specified_machine_settings(self) -> '_816.BasicConicalGearMachineSettings':
        """BasicConicalGearMachineSettings: 'SpecifiedMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecifiedMachineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_finish_cutter(self) -> '_810.WheelFinishCutter':
        """WheelFinishCutter: 'WheelFinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelFinishCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_rough_cutter(self) -> '_811.WheelRoughCutter':
        """WheelRoughCutter: 'WheelRoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelRoughCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalWheelManufacturingConfig._Cast_ConicalWheelManufacturingConfig':
        return self._Cast_ConicalWheelManufacturingConfig(self)
