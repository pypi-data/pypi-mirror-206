"""_513.py

ISO6336AbstractMeshSingleFlankRating
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.rating.cylindrical import _474, _463
from mastapy.gears.rating.cylindrical.iso6336 import _512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_ABSTRACT_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ISO6336AbstractMeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO6336AbstractMeshSingleFlankRating',)


class ISO6336AbstractMeshSingleFlankRating(_463.CylindricalMeshSingleFlankRating):
    """ISO6336AbstractMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO6336_ABSTRACT_MESH_SINGLE_FLANK_RATING

    class _Cast_ISO6336AbstractMeshSingleFlankRating:
        """Special nested class for casting ISO6336AbstractMeshSingleFlankRating to subclasses."""

        def __init__(self, parent: 'ISO6336AbstractMeshSingleFlankRating'):
            self._parent = parent

        @property
        def cylindrical_mesh_single_flank_rating(self):
            return self._parent._cast(_463.CylindricalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(self):
            from mastapy.gears.rating import _362
            
            return self._parent._cast(_362.MeshSingleFlankRating)

        @property
        def metal_plastic_or_plastic_metal_vdi2736_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _485
            
            return self._parent._cast(_485.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating)

        @property
        def plastic_gear_vdi2736_abstract_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _487
            
            return self._parent._cast(_487.PlasticGearVDI2736AbstractMeshSingleFlankRating)

        @property
        def plastic_plastic_vdi2736_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _489
            
            return self._parent._cast(_489.PlasticPlasticVDI2736MeshSingleFlankRating)

        @property
        def iso63361996_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _507
            
            return self._parent._cast(_507.ISO63361996MeshSingleFlankRating)

        @property
        def iso63362006_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _509
            
            return self._parent._cast(_509.ISO63362006MeshSingleFlankRating)

        @property
        def iso63362019_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _511
            
            return self._parent._cast(_511.ISO63362019MeshSingleFlankRating)

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _515
            
            return self._parent._cast(_515.ISO6336AbstractMetalMeshSingleFlankRating)

        @property
        def din3990_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.din3990 import _528
            
            return self._parent._cast(_528.DIN3990MeshSingleFlankRating)

        @property
        def iso6336_abstract_mesh_single_flank_rating(self) -> 'ISO6336AbstractMeshSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO6336AbstractMeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def application_factor(self) -> 'float':
        """float: 'ApplicationFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApplicationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_factor_contact(self) -> 'float':
        """float: 'ContactRatioFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRatioFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_factor_for_nominal_root_root_stress(self) -> 'float':
        """float: 'ContactRatioFactorForNominalRootRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRatioFactorForNominalRootRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_factor_source(self) -> 'str':
        """str: 'DynamicFactorSource' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicFactorSource

        if temp is None:
            return ''

        return temp

    @property
    def elasticity_factor(self) -> 'float':
        """float: 'ElasticityFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticityFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def face_load_factor_bending(self) -> 'float':
        """float: 'FaceLoadFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceLoadFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def face_load_factor_contact_source(self) -> 'str':
        """str: 'FaceLoadFactorContactSource' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceLoadFactorContactSource

        if temp is None:
            return ''

        return temp

    @property
    def helix_angle_factor_bending(self) -> 'float':
        """float: 'HelixAngleFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngleFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_angle_factor_contact(self) -> 'float':
        """float: 'HelixAngleFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngleFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_coefficient_of_friction_calculated_constant_flash_temperature_method(self) -> 'float':
        """float: 'MeanCoefficientOfFrictionCalculatedConstantFlashTemperatureMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanCoefficientOfFrictionCalculatedConstantFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_contact_pattern_enhancement(self) -> '_474.MisalignmentContactPatternEnhancements':
        """MisalignmentContactPatternEnhancements: 'MisalignmentContactPatternEnhancement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentContactPatternEnhancement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _474.MisalignmentContactPatternEnhancements)
        return constructor.new_from_mastapy_type(_474.MisalignmentContactPatternEnhancements)(value) if value is not None else None

    @property
    def nominal_contact_stress(self) -> 'float':
        """float: 'NominalContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity_at_end_of_active_profile(self) -> 'float':
        """float: 'SlidingVelocityAtEndOfActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingVelocityAtEndOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity_at_pitch_point(self) -> 'float':
        """float: 'SlidingVelocityAtPitchPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingVelocityAtPitchPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity_at_start_of_active_profile(self) -> 'float':
        """float: 'SlidingVelocityAtStartOfActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingVelocityAtStartOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_tangential_velocities_at_end_of_active_profile(self) -> 'float':
        """float: 'SumOfTangentialVelocitiesAtEndOfActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SumOfTangentialVelocitiesAtEndOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_tangential_velocities_at_pitch_point(self) -> 'float':
        """float: 'SumOfTangentialVelocitiesAtPitchPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SumOfTangentialVelocitiesAtPitchPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_tangential_velocities_at_start_of_active_profile(self) -> 'float':
        """float: 'SumOfTangentialVelocitiesAtStartOfActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SumOfTangentialVelocitiesAtStartOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def total_contact_ratio(self) -> 'float':
        """float: 'TotalContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_load_factor_bending(self) -> 'float':
        """float: 'TransverseLoadFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseLoadFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def zone_factor(self) -> 'float':
        """float: 'ZoneFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZoneFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_single_flank_ratings(self) -> 'List[_512.ISO6336AbstractGearSingleFlankRating]':
        """List[ISO6336AbstractGearSingleFlankRating]: 'GearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def isodin_cylindrical_gear_single_flank_ratings(self) -> 'List[_512.ISO6336AbstractGearSingleFlankRating]':
        """List[ISO6336AbstractGearSingleFlankRating]: 'ISODINCylindricalGearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISODINCylindricalGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating':
        return self._Cast_ISO6336AbstractMeshSingleFlankRating(self)
