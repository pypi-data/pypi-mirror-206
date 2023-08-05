"""_2059.py

ThreePointContactInternalClearance
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _1958
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THREE_POINT_CONTACT_INTERNAL_CLEARANCE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'ThreePointContactInternalClearance')


__docformat__ = 'restructuredtext en'
__all__ = ('ThreePointContactInternalClearance',)


class ThreePointContactInternalClearance(_1958.InternalClearance):
    """ThreePointContactInternalClearance

    This is a mastapy class.
    """

    TYPE = _THREE_POINT_CONTACT_INTERNAL_CLEARANCE

    class _Cast_ThreePointContactInternalClearance:
        """Special nested class for casting ThreePointContactInternalClearance to subclasses."""

        def __init__(self, parent: 'ThreePointContactInternalClearance'):
            self._parent = parent

        @property
        def internal_clearance(self):
            return self._parent._cast(_1958.InternalClearance)

        @property
        def three_point_contact_internal_clearance(self) -> 'ThreePointContactInternalClearance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ThreePointContactInternalClearance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def operating_free_contact_angle(self) -> 'float':
        """float: 'OperatingFreeContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OperatingFreeContactAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ThreePointContactInternalClearance._Cast_ThreePointContactInternalClearance':
        return self._Cast_ThreePointContactInternalClearance(self)
