"""_453.py

CylindricalGearFlankRating
"""
from mastapy._internal import constructor
from mastapy.gears.rating import _355
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearFlankRating',)


class CylindricalGearFlankRating(_355.GearFlankRating):
    """CylindricalGearFlankRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FLANK_RATING

    class _Cast_CylindricalGearFlankRating:
        """Special nested class for casting CylindricalGearFlankRating to subclasses."""

        def __init__(self, parent: 'CylindricalGearFlankRating'):
            self._parent = parent

        @property
        def gear_flank_rating(self):
            return self._parent._cast(_355.GearFlankRating)

        @property
        def cylindrical_gear_flank_rating(self) -> 'CylindricalGearFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worst_dynamic_factor(self) -> 'float':
        """float: 'WorstDynamicFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstDynamicFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_face_load_factor_contact(self) -> 'float':
        """float: 'WorstFaceLoadFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstFaceLoadFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_load_sharing_factor(self) -> 'float':
        """float: 'WorstLoadSharingFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstLoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'CylindricalGearFlankRating._Cast_CylindricalGearFlankRating':
        return self._Cast_CylindricalGearFlankRating(self)
