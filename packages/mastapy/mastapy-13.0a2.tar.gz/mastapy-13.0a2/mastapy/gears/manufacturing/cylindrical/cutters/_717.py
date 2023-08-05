"""_717.py

RoughCutterCreationSettings
"""
from mastapy.gears.gear_designs.cylindrical import _1076
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _736
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROUGH_CUTTER_CREATION_SETTINGS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'RoughCutterCreationSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('RoughCutterCreationSettings',)


class RoughCutterCreationSettings(_0.APIBase):
    """RoughCutterCreationSettings

    This is a mastapy class.
    """

    TYPE = _ROUGH_CUTTER_CREATION_SETTINGS

    class _Cast_RoughCutterCreationSettings:
        """Special nested class for casting RoughCutterCreationSettings to subclasses."""

        def __init__(self, parent: 'RoughCutterCreationSettings'):
            self._parent = parent

        @property
        def rough_cutter_creation_settings(self) -> 'RoughCutterCreationSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RoughCutterCreationSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def finish_thickness_used_to_generate_cutter(self) -> '_1076.TolerancedMetalMeasurements':
        """TolerancedMetalMeasurements: 'FinishThicknessUsedToGenerateCutter' is the original name of this property."""

        temp = self.wrapped.FinishThicknessUsedToGenerateCutter

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1076.TolerancedMetalMeasurements)
        return constructor.new_from_mastapy_type(_1076.TolerancedMetalMeasurements)(value) if value is not None else None

    @finish_thickness_used_to_generate_cutter.setter
    def finish_thickness_used_to_generate_cutter(self, value: '_1076.TolerancedMetalMeasurements'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1076.TolerancedMetalMeasurements.type_())
        self.wrapped.FinishThicknessUsedToGenerateCutter = value

    @property
    def rough_thickness_used_to_generate_cutter(self) -> '_1076.TolerancedMetalMeasurements':
        """TolerancedMetalMeasurements: 'RoughThicknessUsedToGenerateCutter' is the original name of this property."""

        temp = self.wrapped.RoughThicknessUsedToGenerateCutter

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1076.TolerancedMetalMeasurements)
        return constructor.new_from_mastapy_type(_1076.TolerancedMetalMeasurements)(value) if value is not None else None

    @rough_thickness_used_to_generate_cutter.setter
    def rough_thickness_used_to_generate_cutter(self, value: '_1076.TolerancedMetalMeasurements'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1076.TolerancedMetalMeasurements.type_())
        self.wrapped.RoughThicknessUsedToGenerateCutter = value

    @property
    def finish_tool_clearances(self) -> '_736.ManufacturingOperationConstraints':
        """ManufacturingOperationConstraints: 'FinishToolClearances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishToolClearances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_tool_clearances(self) -> '_736.ManufacturingOperationConstraints':
        """ManufacturingOperationConstraints: 'RoughToolClearances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughToolClearances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RoughCutterCreationSettings._Cast_RoughCutterCreationSettings':
        return self._Cast_RoughCutterCreationSettings(self)
