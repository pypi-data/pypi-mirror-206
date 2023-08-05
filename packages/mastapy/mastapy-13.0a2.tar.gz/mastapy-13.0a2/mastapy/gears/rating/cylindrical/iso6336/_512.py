"""_512.py

ISO6336AbstractGearSingleFlankRating
"""
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical import _461
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_ABSTRACT_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ISO6336AbstractGearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO6336AbstractGearSingleFlankRating',)


class ISO6336AbstractGearSingleFlankRating(_461.CylindricalGearSingleFlankRating):
    """ISO6336AbstractGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO6336_ABSTRACT_GEAR_SINGLE_FLANK_RATING

    class _Cast_ISO6336AbstractGearSingleFlankRating:
        """Special nested class for casting ISO6336AbstractGearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'ISO6336AbstractGearSingleFlankRating'):
            self._parent = parent

        @property
        def cylindrical_gear_single_flank_rating(self):
            return self._parent._cast(_461.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(self):
            from mastapy.gears.rating import _360
            
            return self._parent._cast(_360.GearSingleFlankRating)

        @property
        def plastic_gear_vdi2736_abstract_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _486
            
            return self._parent._cast(_486.PlasticGearVDI2736AbstractGearSingleFlankRating)

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_metal_plastic_or_a_plastic_metal_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _491
            
            return self._parent._cast(_491.PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh)

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_plastic_plastic_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _492
            
            return self._parent._cast(_492.PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh)

        @property
        def iso63361996_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _506
            
            return self._parent._cast(_506.ISO63361996GearSingleFlankRating)

        @property
        def iso63362006_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _508
            
            return self._parent._cast(_508.ISO63362006GearSingleFlankRating)

        @property
        def iso63362019_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _510
            
            return self._parent._cast(_510.ISO63362019GearSingleFlankRating)

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _514
            
            return self._parent._cast(_514.ISO6336AbstractMetalGearSingleFlankRating)

        @property
        def din3990_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.din3990 import _527
            
            return self._parent._cast(_527.DIN3990GearSingleFlankRating)

        @property
        def iso6336_abstract_gear_single_flank_rating(self) -> 'ISO6336AbstractGearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO6336AbstractGearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def e(self) -> 'float':
        """float: 'E' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.E

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_for_root_stress(self) -> 'float':
        """float: 'FaceWidthForRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceWidthForRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def form_factor(self) -> 'float':
        """float: 'FormFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FormFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def g(self) -> 'float':
        """float: 'G' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.G

        if temp is None:
            return 0.0

        return temp

    @property
    def h(self) -> 'float':
        """float: 'H' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.H

        if temp is None:
            return 0.0

        return temp

    @property
    def intermediate_angle(self) -> 'float':
        """float: 'IntermediateAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IntermediateAngle

        if temp is None:
            return 0.0

        return temp

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
    def notch_parameter(self) -> 'float':
        """float: 'NotchParameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NotchParameter

        if temp is None:
            return 0.0

        return temp

    @property
    def roughness_factor(self) -> 'float':
        """float: 'RoughnessFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughnessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_correction_factor(self) -> 'float':
        """float: 'StressCorrectionFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_correction_factor_bending_for_test_gears(self) -> 'float':
        """float: 'StressCorrectionFactorBendingForTestGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressCorrectionFactorBendingForTestGears

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating':
        return self._Cast_ISO6336AbstractGearSingleFlankRating(self)
