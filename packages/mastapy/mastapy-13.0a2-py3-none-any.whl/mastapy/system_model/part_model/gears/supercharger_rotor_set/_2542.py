"""_2542.py

SuperchargerRotorSet
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility_gui.charts import _1850
from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
    _2544, _2534, _2537, _2535,
    _2536, _2539, _2538
)
from mastapy.utility.databases import _1816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SUPERCHARGER_ROTOR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'SuperchargerRotorSet')


__docformat__ = 'restructuredtext en'
__all__ = ('SuperchargerRotorSet',)


class SuperchargerRotorSet(_1816.NamedDatabaseItem):
    """SuperchargerRotorSet

    This is a mastapy class.
    """

    TYPE = _SUPERCHARGER_ROTOR_SET

    class _Cast_SuperchargerRotorSet:
        """Special nested class for casting SuperchargerRotorSet to subclasses."""

        def __init__(self, parent: 'SuperchargerRotorSet'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def supercharger_rotor_set(self) -> 'SuperchargerRotorSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SuperchargerRotorSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_reaction_force(self) -> 'float':
        """float: 'AxialReactionForce' is the original name of this property."""

        temp = self.wrapped.AxialReactionForce

        if temp is None:
            return 0.0

        return temp

    @axial_reaction_force.setter
    def axial_reaction_force(self, value: 'float'):
        self.wrapped.AxialReactionForce = float(value) if value else 0.0

    @property
    def dynamic_load_factor(self) -> 'float':
        """float: 'DynamicLoadFactor' is the original name of this property."""

        temp = self.wrapped.DynamicLoadFactor

        if temp is None:
            return 0.0

        return temp

    @dynamic_load_factor.setter
    def dynamic_load_factor(self, value: 'float'):
        self.wrapped.DynamicLoadFactor = float(value) if value else 0.0

    @property
    def lateral_reaction_force(self) -> 'float':
        """float: 'LateralReactionForce' is the original name of this property."""

        temp = self.wrapped.LateralReactionForce

        if temp is None:
            return 0.0

        return temp

    @lateral_reaction_force.setter
    def lateral_reaction_force(self, value: 'float'):
        self.wrapped.LateralReactionForce = float(value) if value else 0.0

    @property
    def lateral_reaction_moment(self) -> 'float':
        """float: 'LateralReactionMoment' is the original name of this property."""

        temp = self.wrapped.LateralReactionMoment

        if temp is None:
            return 0.0

        return temp

    @lateral_reaction_moment.setter
    def lateral_reaction_moment(self, value: 'float'):
        self.wrapped.LateralReactionMoment = float(value) if value else 0.0

    @property
    def selected_file_name(self) -> 'str':
        """str: 'SelectedFileName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedFileName

        if temp is None:
            return ''

        return temp

    @property
    def supercharger_map_chart(self) -> '_1850.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'SuperchargerMapChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SuperchargerMapChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def vertical_reaction_force(self) -> 'float':
        """float: 'VerticalReactionForce' is the original name of this property."""

        temp = self.wrapped.VerticalReactionForce

        if temp is None:
            return 0.0

        return temp

    @vertical_reaction_force.setter
    def vertical_reaction_force(self, value: 'float'):
        self.wrapped.VerticalReactionForce = float(value) if value else 0.0

    @property
    def vertical_reaction_moment(self) -> 'float':
        """float: 'VerticalReactionMoment' is the original name of this property."""

        temp = self.wrapped.VerticalReactionMoment

        if temp is None:
            return 0.0

        return temp

    @vertical_reaction_moment.setter
    def vertical_reaction_moment(self, value: 'float'):
        self.wrapped.VerticalReactionMoment = float(value) if value else 0.0

    @property
    def y_variable_for_imported_data(self) -> '_2544.YVariableForImportedData':
        """YVariableForImportedData: 'YVariableForImportedData' is the original name of this property."""

        temp = self.wrapped.YVariableForImportedData

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _2544.YVariableForImportedData)
        return constructor.new_from_mastapy_type(_2544.YVariableForImportedData)(value) if value is not None else None

    @y_variable_for_imported_data.setter
    def y_variable_for_imported_data(self, value: '_2544.YVariableForImportedData'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _2544.YVariableForImportedData.type_())
        self.wrapped.YVariableForImportedData = value

    @property
    def boost_pressure(self) -> '_2534.BoostPressureInputOptions':
        """BoostPressureInputOptions: 'BoostPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoostPressure

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def file(self) -> '_2537.RotorSetDataInputFileOptions':
        """RotorSetDataInputFileOptions: 'File' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.File

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def input_power(self) -> '_2535.InputPowerInputOptions':
        """InputPowerInputOptions: 'InputPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InputPower

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pressure_ratio(self) -> '_2536.PressureRatioInputOptions':
        """PressureRatioInputOptions: 'PressureRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PressureRatio

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_speed(self) -> '_2539.RotorSpeedInputOptions':
        """RotorSpeedInputOptions: 'RotorSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def measured_points(self) -> 'List[_2538.RotorSetMeasuredPoint]':
        """List[RotorSetMeasuredPoint]: 'MeasuredPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasuredPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def select_different_file(self):
        """ 'SelectDifferentFile' is the original name of this method."""

        self.wrapped.SelectDifferentFile()

    @property
    def cast_to(self) -> 'SuperchargerRotorSet._Cast_SuperchargerRotorSet':
        return self._Cast_SuperchargerRotorSet(self)
