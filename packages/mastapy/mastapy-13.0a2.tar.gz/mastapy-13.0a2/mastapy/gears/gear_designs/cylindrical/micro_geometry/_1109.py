"""_1109.py

LeadReliefWithDeviation
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1122
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEAD_RELIEF_WITH_DEVIATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'LeadReliefWithDeviation')


__docformat__ = 'restructuredtext en'
__all__ = ('LeadReliefWithDeviation',)


class LeadReliefWithDeviation(_1122.ReliefWithDeviation):
    """LeadReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _LEAD_RELIEF_WITH_DEVIATION

    class _Cast_LeadReliefWithDeviation:
        """Special nested class for casting LeadReliefWithDeviation to subclasses."""

        def __init__(self, parent: 'LeadReliefWithDeviation'):
            self._parent = parent

        @property
        def relief_with_deviation(self):
            return self._parent._cast(_1122.ReliefWithDeviation)

        @property
        def lead_form_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1108
            
            return self._parent._cast(_1108.LeadFormReliefWithDeviation)

        @property
        def lead_slope_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1110
            
            return self._parent._cast(_1110.LeadSlopeReliefWithDeviation)

        @property
        def total_lead_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1124
            
            return self._parent._cast(_1124.TotalLeadReliefWithDeviation)

        @property
        def lead_relief_with_deviation(self) -> 'LeadReliefWithDeviation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LeadReliefWithDeviation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def distance_along_face_width(self) -> 'float':
        """float: 'DistanceAlongFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DistanceAlongFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def lead_relief(self) -> 'float':
        """float: 'LeadRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadRelief

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LeadReliefWithDeviation._Cast_LeadReliefWithDeviation':
        return self._Cast_LeadReliefWithDeviation(self)
