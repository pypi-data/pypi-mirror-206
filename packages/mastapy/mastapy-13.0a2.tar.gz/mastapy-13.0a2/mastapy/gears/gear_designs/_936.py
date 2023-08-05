"""_936.py

BevelHypoidGearDesignSettingsItem
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears import _340
from mastapy.utility.databases import _1816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_DESIGN_SETTINGS_ITEM = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'BevelHypoidGearDesignSettingsItem')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelHypoidGearDesignSettingsItem',)


class BevelHypoidGearDesignSettingsItem(_1816.NamedDatabaseItem):
    """BevelHypoidGearDesignSettingsItem

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_DESIGN_SETTINGS_ITEM

    class _Cast_BevelHypoidGearDesignSettingsItem:
        """Special nested class for casting BevelHypoidGearDesignSettingsItem to subclasses."""

        def __init__(self, parent: 'BevelHypoidGearDesignSettingsItem'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def bevel_hypoid_gear_design_settings_item(self) -> 'BevelHypoidGearDesignSettingsItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelHypoidGearDesignSettingsItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allow_overriding_manufacturing_config_micro_geometry_in_a_load_case(self) -> 'bool':
        """bool: 'AllowOverridingManufacturingConfigMicroGeometryInALoadCase' is the original name of this property."""

        temp = self.wrapped.AllowOverridingManufacturingConfigMicroGeometryInALoadCase

        if temp is None:
            return False

        return temp

    @allow_overriding_manufacturing_config_micro_geometry_in_a_load_case.setter
    def allow_overriding_manufacturing_config_micro_geometry_in_a_load_case(self, value: 'bool'):
        self.wrapped.AllowOverridingManufacturingConfigMicroGeometryInALoadCase = bool(value) if value else False

    @property
    def minimum_ratio(self) -> 'float':
        """float: 'MinimumRatio' is the original name of this property."""

        temp = self.wrapped.MinimumRatio

        if temp is None:
            return 0.0

        return temp

    @minimum_ratio.setter
    def minimum_ratio(self, value: 'float'):
        self.wrapped.MinimumRatio = float(value) if value else 0.0

    @property
    def quality_grade_type(self) -> '_340.QualityGradeTypes':
        """QualityGradeTypes: 'QualityGradeType' is the original name of this property."""

        temp = self.wrapped.QualityGradeType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _340.QualityGradeTypes)
        return constructor.new_from_mastapy_type(_340.QualityGradeTypes)(value) if value is not None else None

    @quality_grade_type.setter
    def quality_grade_type(self, value: '_340.QualityGradeTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _340.QualityGradeTypes.type_())
        self.wrapped.QualityGradeType = value

    @property
    def cast_to(self) -> 'BevelHypoidGearDesignSettingsItem._Cast_BevelHypoidGearDesignSettingsItem':
        return self._Cast_BevelHypoidGearDesignSettingsItem(self)
