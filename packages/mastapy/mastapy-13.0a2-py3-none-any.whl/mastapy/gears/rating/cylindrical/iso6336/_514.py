"""_514.py

ISO6336AbstractMetalGearSingleFlankRating
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.rating.cylindrical.iso6336 import _512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_ABSTRACT_METAL_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ISO6336AbstractMetalGearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO6336AbstractMetalGearSingleFlankRating',)


class ISO6336AbstractMetalGearSingleFlankRating(_512.ISO6336AbstractGearSingleFlankRating):
    """ISO6336AbstractMetalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO6336_ABSTRACT_METAL_GEAR_SINGLE_FLANK_RATING

    class _Cast_ISO6336AbstractMetalGearSingleFlankRating:
        """Special nested class for casting ISO6336AbstractMetalGearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'ISO6336AbstractMetalGearSingleFlankRating'):
            self._parent = parent

        @property
        def iso6336_abstract_gear_single_flank_rating(self):
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
        def din3990_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.din3990 import _527
            
            return self._parent._cast(_527.DIN3990GearSingleFlankRating)

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(self) -> 'ISO6336AbstractMetalGearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO6336AbstractMetalGearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum_contact_ratio(self) -> 'float':
        """float: 'AddendumContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AddendumContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def base_pitch_deviation(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'BasePitchDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasePitchDeviation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @property
    def life_factor_for_bending_stress(self) -> 'float':
        """float: 'LifeFactorForBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_contact_stress(self) -> 'float':
        """float: 'LifeFactorForContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_reference_bending_stress(self) -> 'float':
        """float: 'LifeFactorForReferenceBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForReferenceBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_reference_contact_stress(self) -> 'float':
        """float: 'LifeFactorForReferenceContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForReferenceContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_static_bending_stress(self) -> 'float':
        """float: 'LifeFactorForStaticBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForStaticBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_for_static_contact_stress(self) -> 'float':
        """float: 'LifeFactorForStaticContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForStaticContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_factor(self) -> 'float':
        """float: 'LubricantFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_factor_for_reference_stress(self) -> 'float':
        """float: 'LubricantFactorForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_factor_for_static_stress(self) -> 'float':
        """float: 'LubricantFactorForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def moment_of_inertia_per_unit_face_width(self) -> 'float':
        """float: 'MomentOfInertiaPerUnitFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MomentOfInertiaPerUnitFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_form_deviation(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ProfileFormDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormDeviation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @property
    def relative_individual_gear_mass_per_unit_face_width_referenced_to_line_of_action(self) -> 'float':
        """float: 'RelativeIndividualGearMassPerUnitFaceWidthReferencedToLineOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeIndividualGearMassPerUnitFaceWidthReferencedToLineOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_notch_sensitivity_factor(self) -> 'float':
        """float: 'RelativeNotchSensitivityFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeNotchSensitivityFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_notch_sensitivity_factor_for_reference_stress(self) -> 'float':
        """float: 'RelativeNotchSensitivityFactorForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeNotchSensitivityFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

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
    def relative_surface_factor(self) -> 'float':
        """float: 'RelativeSurfaceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeSurfaceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_factor_for_reference_stress(self) -> 'float':
        """float: 'RelativeSurfaceFactorForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeSurfaceFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_factor_for_static_stress(self) -> 'float':
        """float: 'RelativeSurfaceFactorForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeSurfaceFactorForStaticStress

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
    def roughness_factor_for_reference_stress(self) -> 'float':
        """float: 'RoughnessFactorForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughnessFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def roughness_factor_for_static_stress(self) -> 'float':
        """float: 'RoughnessFactorForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughnessFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def shot_peening_bending_stress_benefit(self) -> 'float':
        """float: 'ShotPeeningBendingStressBenefit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShotPeeningBendingStressBenefit

        if temp is None:
            return 0.0

        return temp

    @property
    def single_pair_tooth_contact_factor(self) -> 'float':
        """float: 'SinglePairToothContactFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SinglePairToothContactFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor(self) -> 'float':
        """float: 'SizeFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_tooth_root(self) -> 'float':
        """float: 'SizeFactorToothRoot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorToothRoot

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_for_reference_bending_stress(self) -> 'float':
        """float: 'SizeFactorForReferenceBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorForReferenceBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_for_reference_contact_stress(self) -> 'float':
        """float: 'SizeFactorForReferenceContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorForReferenceContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_for_static_stress(self) -> 'float':
        """float: 'SizeFactorForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def static_size_factor_tooth_root(self) -> 'float':
        """float: 'StaticSizeFactorToothRoot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticSizeFactorToothRoot

        if temp is None:
            return 0.0

        return temp

    @property
    def velocity_factor(self) -> 'float':
        """float: 'VelocityFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VelocityFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def velocity_factor_for_reference_stress(self) -> 'float':
        """float: 'VelocityFactorForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VelocityFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def velocity_factor_for_static_stress(self) -> 'float':
        """float: 'VelocityFactorForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VelocityFactorForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def work_hardening_factor(self) -> 'float':
        """float: 'WorkHardeningFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkHardeningFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ISO6336AbstractMetalGearSingleFlankRating._Cast_ISO6336AbstractMetalGearSingleFlankRating':
        return self._Cast_ISO6336AbstractMetalGearSingleFlankRating(self)
