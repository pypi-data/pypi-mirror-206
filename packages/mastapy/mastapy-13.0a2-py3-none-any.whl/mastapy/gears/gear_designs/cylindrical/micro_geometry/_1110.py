"""_1110.py

LeadSlopeReliefWithDeviation
"""
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1109
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEAD_SLOPE_RELIEF_WITH_DEVIATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'LeadSlopeReliefWithDeviation')


__docformat__ = 'restructuredtext en'
__all__ = ('LeadSlopeReliefWithDeviation',)


class LeadSlopeReliefWithDeviation(_1109.LeadReliefWithDeviation):
    """LeadSlopeReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _LEAD_SLOPE_RELIEF_WITH_DEVIATION

    class _Cast_LeadSlopeReliefWithDeviation:
        """Special nested class for casting LeadSlopeReliefWithDeviation to subclasses."""

        def __init__(self, parent: 'LeadSlopeReliefWithDeviation'):
            self._parent = parent

        @property
        def lead_relief_with_deviation(self):
            return self._parent._cast(_1109.LeadReliefWithDeviation)

        @property
        def relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1122
            
            return self._parent._cast(_1122.ReliefWithDeviation)

        @property
        def lead_slope_relief_with_deviation(self) -> 'LeadSlopeReliefWithDeviation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LeadSlopeReliefWithDeviation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LeadSlopeReliefWithDeviation._Cast_LeadSlopeReliefWithDeviation':
        return self._Cast_LeadSlopeReliefWithDeviation(self)
