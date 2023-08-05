"""_510.py

ISO63362019GearSingleFlankRating
"""
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.iso6336 import _508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO63362019_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ISO63362019GearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO63362019GearSingleFlankRating',)


class ISO63362019GearSingleFlankRating(_508.ISO63362006GearSingleFlankRating):
    """ISO63362019GearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63362019_GEAR_SINGLE_FLANK_RATING

    class _Cast_ISO63362019GearSingleFlankRating:
        """Special nested class for casting ISO63362019GearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'ISO63362019GearSingleFlankRating'):
            self._parent = parent

        @property
        def iso63362006_gear_single_flank_rating(self):
            return self._parent._cast(_508.ISO63362006GearSingleFlankRating)

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
        def iso63362019_gear_single_flank_rating(self) -> 'ISO63362019GearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO63362019GearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_distribution_influence_factor(self) -> 'float':
        """float: 'LoadDistributionInfluenceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDistributionInfluenceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ISO63362019GearSingleFlankRating._Cast_ISO63362019GearSingleFlankRating':
        return self._Cast_ISO63362019GearSingleFlankRating(self)
