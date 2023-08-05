"""_1463.py

ClampedSection
"""
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor
from mastapy.bolts import _1454
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CLAMPED_SECTION = python_net_import('SMT.MastaAPI.Bolts', 'ClampedSection')


__docformat__ = 'restructuredtext en'
__all__ = ('ClampedSection',)


class ClampedSection(_0.APIBase):
    """ClampedSection

    This is a mastapy class.
    """

    TYPE = _CLAMPED_SECTION

    class _Cast_ClampedSection:
        """Special nested class for casting ClampedSection to subclasses."""

        def __init__(self, parent: 'ClampedSection'):
            self._parent = parent

        @property
        def clamped_section(self) -> 'ClampedSection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClampedSection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def edit_material(self) -> 'str':
        """str: 'EditMaterial' is the original name of this property."""

        temp = self.wrapped.EditMaterial.SelectedItemName

        if temp is None:
            return ''

        return temp

    @edit_material.setter
    def edit_material(self, value: 'str'):
        self.wrapped.EditMaterial.SetSelectedItem(str(value) if value else '')

    @property
    def part_thickness(self) -> 'float':
        """float: 'PartThickness' is the original name of this property."""

        temp = self.wrapped.PartThickness

        if temp is None:
            return 0.0

        return temp

    @part_thickness.setter
    def part_thickness(self, value: 'float'):
        self.wrapped.PartThickness = float(value) if value else 0.0

    @property
    def material(self) -> '_1454.BoltedJointMaterial':
        """BoltedJointMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Material

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ClampedSection._Cast_ClampedSection':
        return self._Cast_ClampedSection(self)
