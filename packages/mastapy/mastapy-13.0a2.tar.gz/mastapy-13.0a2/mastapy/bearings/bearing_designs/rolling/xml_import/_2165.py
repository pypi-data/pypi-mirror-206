"""_2165.py

XMLVariableAssignment
"""
from typing import TypeVar, Generic

from mastapy.bearings.bearing_designs.rolling.xml_import import _2161
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_XML_VARIABLE_ASSIGNMENT = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling.XmlImport', 'XMLVariableAssignment')


__docformat__ = 'restructuredtext en'
__all__ = ('XMLVariableAssignment',)


T = TypeVar('T')


class XMLVariableAssignment(_2161.AbstractXmlVariableAssignment, Generic[T]):
    """XMLVariableAssignment

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _XML_VARIABLE_ASSIGNMENT

    class _Cast_XMLVariableAssignment:
        """Special nested class for casting XMLVariableAssignment to subclasses."""

        def __init__(self, parent: 'XMLVariableAssignment'):
            self._parent = parent

        @property
        def abstract_xml_variable_assignment(self):
            return self._parent._cast(_2161.AbstractXmlVariableAssignment)

        @property
        def xml_variable_assignment(self) -> 'XMLVariableAssignment':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'XMLVariableAssignment.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'XMLVariableAssignment._Cast_XMLVariableAssignment':
        return self._Cast_XMLVariableAssignment(self)
