"""_627.py

LeadModificationSegment
"""
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical import _631
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEAD_MODIFICATION_SEGMENT = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'LeadModificationSegment')


__docformat__ = 'restructuredtext en'
__all__ = ('LeadModificationSegment',)


class LeadModificationSegment(_631.ModificationSegment):
    """LeadModificationSegment

    This is a mastapy class.
    """

    TYPE = _LEAD_MODIFICATION_SEGMENT

    class _Cast_LeadModificationSegment:
        """Special nested class for casting LeadModificationSegment to subclasses."""

        def __init__(self, parent: 'LeadModificationSegment'):
            self._parent = parent

        @property
        def modification_segment(self):
            return self._parent._cast(_631.ModificationSegment)

        @property
        def lead_modification_segment(self) -> 'LeadModificationSegment':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LeadModificationSegment.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def distance_from_centre(self) -> 'float':
        """float: 'DistanceFromCentre' is the original name of this property."""

        temp = self.wrapped.DistanceFromCentre

        if temp is None:
            return 0.0

        return temp

    @distance_from_centre.setter
    def distance_from_centre(self, value: 'float'):
        self.wrapped.DistanceFromCentre = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'LeadModificationSegment._Cast_LeadModificationSegment':
        return self._Cast_LeadModificationSegment(self)
