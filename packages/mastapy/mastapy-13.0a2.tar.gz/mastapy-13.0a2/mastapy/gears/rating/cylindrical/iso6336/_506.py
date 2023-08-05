"""_506.py

ISO63361996GearSingleFlankRating
"""
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.iso6336 import _514
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO63361996_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ISO63361996GearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO63361996GearSingleFlankRating',)


class ISO63361996GearSingleFlankRating(_514.ISO6336AbstractMetalGearSingleFlankRating):
    """ISO63361996GearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63361996_GEAR_SINGLE_FLANK_RATING

    class _Cast_ISO63361996GearSingleFlankRating:
        """Special nested class for casting ISO63361996GearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'ISO63361996GearSingleFlankRating'):
            self._parent = parent

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(self):
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
        def din3990_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.din3990 import _527
            
            return self._parent._cast(_527.DIN3990GearSingleFlankRating)

        @property
        def iso63361996_gear_single_flank_rating(self) -> 'ISO63361996GearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO63361996GearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def nominal_tooth_root_stress(self) -> 'float':
        """float: 'NominalToothRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalToothRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating':
        return self._Cast_ISO63361996GearSingleFlankRating(self)
