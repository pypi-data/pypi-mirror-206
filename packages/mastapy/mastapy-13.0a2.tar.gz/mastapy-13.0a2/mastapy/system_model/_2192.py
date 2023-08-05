"""_2192.py

DutyCycleImporterDesignEntityMatch
"""
from typing import TypeVar, Generic

from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_IMPORTER_DESIGN_ENTITY_MATCH = python_net_import('SMT.MastaAPI.SystemModel', 'DutyCycleImporterDesignEntityMatch')


__docformat__ = 'restructuredtext en'
__all__ = ('DutyCycleImporterDesignEntityMatch',)


T = TypeVar('T')


class DutyCycleImporterDesignEntityMatch(_0.APIBase, Generic[T]):
    """DutyCycleImporterDesignEntityMatch

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _DUTY_CYCLE_IMPORTER_DESIGN_ENTITY_MATCH

    class _Cast_DutyCycleImporterDesignEntityMatch:
        """Special nested class for casting DutyCycleImporterDesignEntityMatch to subclasses."""

        def __init__(self, parent: 'DutyCycleImporterDesignEntityMatch'):
            self._parent = parent

        @property
        def duty_cycle_importer_design_entity_match(self) -> 'DutyCycleImporterDesignEntityMatch':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DutyCycleImporterDesignEntityMatch.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def destination(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'Destination' is the original name of this property."""

        temp = self.wrapped.Destination

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @destination.setter
    def destination(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.Destination = value

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'DutyCycleImporterDesignEntityMatch._Cast_DutyCycleImporterDesignEntityMatch':
        return self._Cast_DutyCycleImporterDesignEntityMatch(self)
