"""_352.py

BendingAndContactReportingObject
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BENDING_AND_CONTACT_REPORTING_OBJECT = python_net_import('SMT.MastaAPI.Gears.Rating', 'BendingAndContactReportingObject')


__docformat__ = 'restructuredtext en'
__all__ = ('BendingAndContactReportingObject',)


class BendingAndContactReportingObject(_0.APIBase):
    """BendingAndContactReportingObject

    This is a mastapy class.
    """

    TYPE = _BENDING_AND_CONTACT_REPORTING_OBJECT

    class _Cast_BendingAndContactReportingObject:
        """Special nested class for casting BendingAndContactReportingObject to subclasses."""

        def __init__(self, parent: 'BendingAndContactReportingObject'):
            self._parent = parent

        @property
        def bending_and_contact_reporting_object(self) -> 'BendingAndContactReportingObject':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BendingAndContactReportingObject.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending(self) -> 'float':
        """float: 'Bending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bending

        if temp is None:
            return 0.0

        return temp

    @property
    def contact(self) -> 'float':
        """float: 'Contact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Contact

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'BendingAndContactReportingObject._Cast_BendingAndContactReportingObject':
        return self._Cast_BendingAndContactReportingObject(self)
