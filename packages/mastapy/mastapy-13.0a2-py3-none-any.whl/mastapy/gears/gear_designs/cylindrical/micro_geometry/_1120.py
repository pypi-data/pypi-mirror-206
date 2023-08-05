"""_1120.py

ProfileReliefWithDeviation
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1020
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1122
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_RELIEF_WITH_DEVIATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'ProfileReliefWithDeviation')


__docformat__ = 'restructuredtext en'
__all__ = ('ProfileReliefWithDeviation',)


class ProfileReliefWithDeviation(_1122.ReliefWithDeviation):
    """ProfileReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _PROFILE_RELIEF_WITH_DEVIATION

    class _Cast_ProfileReliefWithDeviation:
        """Special nested class for casting ProfileReliefWithDeviation to subclasses."""

        def __init__(self, parent: 'ProfileReliefWithDeviation'):
            self._parent = parent

        @property
        def relief_with_deviation(self):
            return self._parent._cast(_1122.ReliefWithDeviation)

        @property
        def profile_form_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1119
            
            return self._parent._cast(_1119.ProfileFormReliefWithDeviation)

        @property
        def profile_slope_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1121
            
            return self._parent._cast(_1121.ProfileSlopeReliefWithDeviation)

        @property
        def total_profile_relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1125
            
            return self._parent._cast(_1125.TotalProfileReliefWithDeviation)

        @property
        def profile_relief_with_deviation(self) -> 'ProfileReliefWithDeviation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ProfileReliefWithDeviation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def profile_relief(self) -> 'float':
        """float: 'ProfileRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileRelief

        if temp is None:
            return 0.0

        return temp

    @property
    def roll_distance(self) -> 'float':
        """float: 'RollDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def position_on_profile(self) -> '_1020.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'PositionOnProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PositionOnProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation':
        return self._Cast_ProfileReliefWithDeviation(self)
