"""_609.py

CylindricalGearSpecifiedProfile
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SPECIFIED_PROFILE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalGearSpecifiedProfile')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSpecifiedProfile',)


class CylindricalGearSpecifiedProfile(_0.APIBase):
    """CylindricalGearSpecifiedProfile

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SPECIFIED_PROFILE

    class _Cast_CylindricalGearSpecifiedProfile:
        """Special nested class for casting CylindricalGearSpecifiedProfile to subclasses."""

        def __init__(self, parent: 'CylindricalGearSpecifiedProfile'):
            self._parent = parent

        @property
        def cylindrical_gear_specified_profile(self) -> 'CylindricalGearSpecifiedProfile':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSpecifiedProfile.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset_at_minimum_roll_distance(self) -> 'float':
        """float: 'OffsetAtMinimumRollDistance' is the original name of this property."""

        temp = self.wrapped.OffsetAtMinimumRollDistance

        if temp is None:
            return 0.0

        return temp

    @offset_at_minimum_roll_distance.setter
    def offset_at_minimum_roll_distance(self, value: 'float'):
        self.wrapped.OffsetAtMinimumRollDistance = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'CylindricalGearSpecifiedProfile._Cast_CylindricalGearSpecifiedProfile':
        return self._Cast_CylindricalGearSpecifiedProfile(self)
