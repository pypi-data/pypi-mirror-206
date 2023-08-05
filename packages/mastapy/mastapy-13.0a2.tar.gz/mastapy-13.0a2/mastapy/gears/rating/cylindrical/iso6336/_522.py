"""_522.py

ToothFlankFractureAnalysisContactPointN1457
"""
from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy.gears.gear_designs.cylindrical import _1020
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_CONTACT_POINT_N1457 = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ToothFlankFractureAnalysisContactPointN1457')


__docformat__ = 'restructuredtext en'
__all__ = ('ToothFlankFractureAnalysisContactPointN1457',)


class ToothFlankFractureAnalysisContactPointN1457(_0.APIBase):
    """ToothFlankFractureAnalysisContactPointN1457

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_CONTACT_POINT_N1457

    class _Cast_ToothFlankFractureAnalysisContactPointN1457:
        """Special nested class for casting ToothFlankFractureAnalysisContactPointN1457 to subclasses."""

        def __init__(self, parent: 'ToothFlankFractureAnalysisContactPointN1457'):
            self._parent = parent

        @property
        def tooth_flank_fracture_analysis_row_n1457(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _525
            
            return self._parent._cast(_525.ToothFlankFractureAnalysisRowN1457)

        @property
        def tooth_flank_fracture_analysis_contact_point_n1457(self) -> 'ToothFlankFractureAnalysisContactPointN1457':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ToothFlankFractureAnalysisContactPointN1457.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def half_of_hertzian_contact_width(self) -> 'float':
        """float: 'HalfOfHertzianContactWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfOfHertzianContactWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_stress(self) -> 'float':
        """float: 'HertzianContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_coefficient_of_friction(self) -> 'float':
        """float: 'MeanCoefficientOfFriction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanCoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def coordinates(self) -> 'Vector2D':
        """Vector2D: 'Coordinates' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Coordinates

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

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
    def cast_to(self) -> 'ToothFlankFractureAnalysisContactPointN1457._Cast_ToothFlankFractureAnalysisContactPointN1457':
        return self._Cast_ToothFlankFractureAnalysisContactPointN1457(self)
