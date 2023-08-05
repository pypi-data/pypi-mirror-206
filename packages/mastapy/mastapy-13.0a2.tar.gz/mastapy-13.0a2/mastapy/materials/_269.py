"""_269.py

MaterialsSettingsItem
"""
from typing import List

from mastapy.utility.property import _1829
from mastapy.materials import _270
from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIALS_SETTINGS_ITEM = python_net_import('SMT.MastaAPI.Materials', 'MaterialsSettingsItem')


__docformat__ = 'restructuredtext en'
__all__ = ('MaterialsSettingsItem',)


class MaterialsSettingsItem(_1816.NamedDatabaseItem):
    """MaterialsSettingsItem

    This is a mastapy class.
    """

    TYPE = _MATERIALS_SETTINGS_ITEM

    class _Cast_MaterialsSettingsItem:
        """Special nested class for casting MaterialsSettingsItem to subclasses."""

        def __init__(self, parent: 'MaterialsSettingsItem'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def materials_settings_item(self) -> 'MaterialsSettingsItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MaterialsSettingsItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def available_material_standards(self) -> 'List[_1829.EnumWithBool[_270.MaterialStandards]]':
        """List[EnumWithBool[MaterialStandards]]: 'AvailableMaterialStandards' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AvailableMaterialStandards

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MaterialsSettingsItem._Cast_MaterialsSettingsItem':
        return self._Cast_MaterialsSettingsItem(self)
