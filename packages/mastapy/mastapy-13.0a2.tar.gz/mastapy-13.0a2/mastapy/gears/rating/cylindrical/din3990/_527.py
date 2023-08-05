"""_527.py

DIN3990GearSingleFlankRating
"""
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.iso6336 import _506
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DIN3990_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.DIN3990', 'DIN3990GearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('DIN3990GearSingleFlankRating',)


class DIN3990GearSingleFlankRating(_506.ISO63361996GearSingleFlankRating):
    """DIN3990GearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _DIN3990_GEAR_SINGLE_FLANK_RATING

    class _Cast_DIN3990GearSingleFlankRating:
        """Special nested class for casting DIN3990GearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'DIN3990GearSingleFlankRating'):
            self._parent = parent

        @property
        def iso63361996_gear_single_flank_rating(self):
            return self._parent._cast(_506.ISO63361996GearSingleFlankRating)

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _514
            
            return self._parent._cast(_514.ISO6336AbstractMetalGearSingleFlankRating)

        @property
        def iso6336_abstract_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _512
            
            return self._parent._cast(_512.ISO6336AbstractGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical import _461
            
            return self._parent._cast(_461.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(self):
            from mastapy.gears.rating import _360
            
            return self._parent._cast(_360.GearSingleFlankRating)

        @property
        def din3990_gear_single_flank_rating(self) -> 'DIN3990GearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DIN3990GearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def relative_notch_sensitivity_factor_for_static_stress(self) -> 'float':
        """float: 'RelativeNotchSensitivityFactorForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeNotchSensitivityFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'DIN3990GearSingleFlankRating._Cast_DIN3990GearSingleFlankRating':
        return self._Cast_DIN3990GearSingleFlankRating(self)
