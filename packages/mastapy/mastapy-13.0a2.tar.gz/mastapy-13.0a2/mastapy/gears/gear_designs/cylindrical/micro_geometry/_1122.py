"""_1122.py

ReliefWithDeviation
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RELIEF_WITH_DEVIATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'ReliefWithDeviation')


__docformat__ = 'restructuredtext en'
__all__ = ('ReliefWithDeviation',)


class ReliefWithDeviation(_0.APIBase):
    """ReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _RELIEF_WITH_DEVIATION

    class _Cast_ReliefWithDeviation:
        """Special nested class for casting ReliefWithDeviation to subclasses."""

        def __init__(self, parent: 'ReliefWithDeviation'):
            self._parent = parent

        @property
        def lead_form_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1108
            
            return self._parent._cast(_1108.LeadFormReliefWithDeviation)

        @property
        def lead_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1109
            
            return self._parent._cast(_1109.LeadReliefWithDeviation)

        @property
        def lead_slope_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1110
            
            return self._parent._cast(_1110.LeadSlopeReliefWithDeviation)

        @property
        def profile_form_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1119
            
            return self._parent._cast(_1119.ProfileFormReliefWithDeviation)

        @property
        def profile_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1120
            
            return self._parent._cast(_1120.ProfileReliefWithDeviation)

        @property
        def profile_slope_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1121
            
            return self._parent._cast(_1121.ProfileSlopeReliefWithDeviation)

        @property
        def total_lead_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1124
            
            return self._parent._cast(_1124.TotalLeadReliefWithDeviation)

        @property
        def total_profile_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1125
            
            return self._parent._cast(_1125.TotalProfileReliefWithDeviation)

        @property
        def relief_with_deviation(self) -> 'ReliefWithDeviation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ReliefWithDeviation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lower_limit(self) -> 'float':
        """float: 'LowerLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LowerLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def relief(self) -> 'float':
        """float: 'Relief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Relief

        if temp is None:
            return 0.0

        return temp

    @property
    def section(self) -> 'str':
        """str: 'Section' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Section

        if temp is None:
            return ''

        return temp

    @property
    def upper_limit(self) -> 'float':
        """float: 'UpperLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UpperLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ReliefWithDeviation._Cast_ReliefWithDeviation':
        return self._Cast_ReliefWithDeviation(self)
