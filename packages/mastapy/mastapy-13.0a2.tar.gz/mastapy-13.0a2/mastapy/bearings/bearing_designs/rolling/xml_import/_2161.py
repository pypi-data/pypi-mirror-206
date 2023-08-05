"""_2161.py

AbstractXmlVariableAssignment
"""
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_XML_VARIABLE_ASSIGNMENT = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling.XmlImport', 'AbstractXmlVariableAssignment')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractXmlVariableAssignment',)


class AbstractXmlVariableAssignment(_0.APIBase):
    """AbstractXmlVariableAssignment

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_XML_VARIABLE_ASSIGNMENT

    class _Cast_AbstractXmlVariableAssignment:
        """Special nested class for casting AbstractXmlVariableAssignment to subclasses."""

        def __init__(self, parent: 'AbstractXmlVariableAssignment'):
            self._parent = parent

        @property
        def xml_variable_assignment(self):
            from mastapy.bearings.bearing_designs.rolling.xml_import import _2165
            
            return self._parent._cast(_2165.XMLVariableAssignment)

        @property
        def abstract_xml_variable_assignment(self) -> 'AbstractXmlVariableAssignment':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractXmlVariableAssignment.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def definitions(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'Definitions' is the original name of this property."""

        temp = self.wrapped.Definitions

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @definitions.setter
    def definitions(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.Definitions = value

    @property
    def description(self) -> 'str':
        """str: 'Description' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Description

        if temp is None:
            return ''

        return temp

    @property
    def variable_name(self) -> 'str':
        """str: 'VariableName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VariableName

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'AbstractXmlVariableAssignment._Cast_AbstractXmlVariableAssignment':
        return self._Cast_AbstractXmlVariableAssignment(self)
