"""_1821.py

EnumWithSelectedValue
"""
from typing import List, TypeVar, Generic

from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _7515
from mastapy._internal.cast_exception import CastException

_ARRAY = python_net_import('System', 'Array')
_ENUM_WITH_SELECTED_VALUE = python_net_import('SMT.MastaAPI.Utility.Property', 'EnumWithSelectedValue')


__docformat__ = 'restructuredtext en'
__all__ = ('EnumWithSelectedValue',)


TAPIEnum = TypeVar('TAPIEnum')


class EnumWithSelectedValue(_7515.MarshalByRefObjectPermanent, Generic[TAPIEnum]):
    """EnumWithSelectedValue

    This is a mastapy class.

    Generic Types:
        TAPIEnum
    """

    TYPE = _ENUM_WITH_SELECTED_VALUE

    class _Cast_EnumWithSelectedValue:
        """Special nested class for casting EnumWithSelectedValue to subclasses."""

        def __init__(self, parent: 'EnumWithSelectedValue'):
            self._parent = parent

        @property
        def marshal_by_ref_object_permanent(self):
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def enum_with_selected_value(self) -> 'EnumWithSelectedValue':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EnumWithSelectedValue.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def selected_value(self) -> 'TAPIEnum':
        """TAPIEnum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedValue

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(TAPIEnum)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[TAPIEnum]':
        """List[TAPIEnum]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'EnumWithSelectedValue._Cast_EnumWithSelectedValue':
        return self._Cast_EnumWithSelectedValue(self)
