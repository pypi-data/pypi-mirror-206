"""_2205.py

RelativeComponentAlignment
"""
from typing import TypeVar, Generic

from mastapy.math_utility import _1479
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.system_model import _2206
from mastapy import _0
from mastapy.system_model.part_model import _2424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RELATIVE_COMPONENT_ALIGNMENT = python_net_import('SMT.MastaAPI.SystemModel', 'RelativeComponentAlignment')


__docformat__ = 'restructuredtext en'
__all__ = ('RelativeComponentAlignment',)


T = TypeVar('T', bound='_2424.Component')


class RelativeComponentAlignment(_0.APIBase, Generic[T]):
    """RelativeComponentAlignment

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _RELATIVE_COMPONENT_ALIGNMENT

    class _Cast_RelativeComponentAlignment:
        """Special nested class for casting RelativeComponentAlignment to subclasses."""

        def __init__(self, parent: 'RelativeComponentAlignment'):
            self._parent = parent

        @property
        def relative_component_alignment(self) -> 'RelativeComponentAlignment':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RelativeComponentAlignment.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def alignment_axis(self) -> '_1479.AlignmentAxis':
        """AlignmentAxis: 'AlignmentAxis' is the original name of this property."""

        temp = self.wrapped.AlignmentAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1479.AlignmentAxis)
        return constructor.new_from_mastapy_type(_1479.AlignmentAxis)(value) if value is not None else None

    @alignment_axis.setter
    def alignment_axis(self, value: '_1479.AlignmentAxis'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1479.AlignmentAxis.type_())
        self.wrapped.AlignmentAxis = value

    @property
    def axial_offset(self) -> '_2206.RelativeOffsetOption':
        """RelativeOffsetOption: 'AxialOffset' is the original name of this property."""

        temp = self.wrapped.AxialOffset

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _2206.RelativeOffsetOption)
        return constructor.new_from_mastapy_type(_2206.RelativeOffsetOption)(value) if value is not None else None

    @axial_offset.setter
    def axial_offset(self, value: '_2206.RelativeOffsetOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _2206.RelativeOffsetOption.type_())
        self.wrapped.AxialOffset = value

    @property
    def rotation_angle(self) -> 'float':
        """float: 'RotationAngle' is the original name of this property."""

        temp = self.wrapped.RotationAngle

        if temp is None:
            return 0.0

        return temp

    @rotation_angle.setter
    def rotation_angle(self, value: 'float'):
        self.wrapped.RotationAngle = float(value) if value else 0.0

    @property
    def specified_offset(self) -> 'float':
        """float: 'SpecifiedOffset' is the original name of this property."""

        temp = self.wrapped.SpecifiedOffset

        if temp is None:
            return 0.0

        return temp

    @specified_offset.setter
    def specified_offset(self, value: 'float'):
        self.wrapped.SpecifiedOffset = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'RelativeComponentAlignment._Cast_RelativeComponentAlignment':
        return self._Cast_RelativeComponentAlignment(self)
