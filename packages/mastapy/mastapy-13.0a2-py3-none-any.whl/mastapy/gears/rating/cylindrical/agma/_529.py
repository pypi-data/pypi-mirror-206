"""_529.py

AGMA2101GearSingleFlankRating
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.rating.cylindrical import _461
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA2101_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.AGMA', 'AGMA2101GearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMA2101GearSingleFlankRating',)


class AGMA2101GearSingleFlankRating(_461.CylindricalGearSingleFlankRating):
    """AGMA2101GearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _AGMA2101_GEAR_SINGLE_FLANK_RATING

    class _Cast_AGMA2101GearSingleFlankRating:
        """Special nested class for casting AGMA2101GearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'AGMA2101GearSingleFlankRating'):
            self._parent = parent

        @property
        def cylindrical_gear_single_flank_rating(self):
            return self._parent._cast(_461.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(self):
            from mastapy.gears.rating import _360
            
            return self._parent._cast(_360.GearSingleFlankRating)

        @property
        def agma2101_gear_single_flank_rating(self) -> 'AGMA2101GearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMA2101GearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_contact_load_factor(self) -> 'float':
        """float: 'AllowableContactLoadFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableContactLoadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_transmitted_power_for_bending_strength(self) -> 'float':
        """float: 'AllowableTransmittedPowerForBendingStrength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableTransmittedPowerForBendingStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_transmitted_power_for_bending_strength_at_unity_service_factor(self) -> 'float':
        """float: 'AllowableTransmittedPowerForBendingStrengthAtUnityServiceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableTransmittedPowerForBendingStrengthAtUnityServiceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_transmitted_power_for_pitting_resistance_at_unity_service_factor(self) -> 'float':
        """float: 'AllowableTransmittedPowerForPittingResistanceAtUnityServiceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableTransmittedPowerForPittingResistanceAtUnityServiceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_unit_load_for_bending_strength(self) -> 'float':
        """float: 'AllowableUnitLoadForBendingStrength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableUnitLoadForBendingStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def backup_ratio(self) -> 'float':
        """float: 'BackupRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BackupRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_j(self) -> 'float':
        """float: 'GeometryFactorJ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryFactorJ

        if temp is None:
            return 0.0

        return temp

    @property
    def hardness_ratio_factor(self) -> 'float':
        """float: 'HardnessRatioFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HardnessRatioFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def height_of_lewis_parabola(self) -> 'float':
        """float: 'HeightOfLewisParabola' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeightOfLewisParabola

        if temp is None:
            return 0.0

        return temp

    @property
    def helical_factor(self) -> 'float':
        """float: 'HelicalFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelicalFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_angle_factor(self) -> 'float':
        """float: 'HelixAngleFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngleFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_angle(self) -> 'float':
        """float: 'LoadAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_tolerance_diameter_for_the_agma_standard(self) -> 'float':
        """float: 'MaximumToleranceDiameterForTheAGMAStandard' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumToleranceDiameterForTheAGMAStandard

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_tolerance_diameter_for_the_agma_standard(self) -> 'float':
        """float: 'MinimumToleranceDiameterForTheAGMAStandard' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumToleranceDiameterForTheAGMAStandard

        if temp is None:
            return 0.0

        return temp

    @property
    def pitting_resistance_power_rating(self) -> 'float':
        """float: 'PittingResistancePowerRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PittingResistancePowerRating

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_factor_bending(self) -> 'float':
        """float: 'ReliabilityFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReliabilityFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_factor_contact(self) -> 'float':
        """float: 'ReliabilityFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReliabilityFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def rim_thickness_factor(self) -> 'float':
        """float: 'RimThicknessFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RimThicknessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius(self) -> 'float':
        """float: 'RootFilletRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootFilletRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def single_pitch_deviation_agma(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SinglePitchDeviationAGMA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SinglePitchDeviationAGMA

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @property
    def stress_correction_factor_agma(self) -> 'float':
        """float: 'StressCorrectionFactorAGMA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressCorrectionFactorAGMA

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_cycle_factor_for_pitting(self) -> 'float':
        """float: 'StressCycleFactorForPitting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressCycleFactorForPitting

        if temp is None:
            return 0.0

        return temp

    @property
    def tolerance_diameter(self) -> 'float':
        """float: 'ToleranceDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToleranceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_form_factor(self) -> 'float':
        """float: 'ToothFormFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothFormFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_thickness_at_critical_section(self) -> 'float':
        """float: 'ToothThicknessAtCriticalSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothThicknessAtCriticalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def unit_load_for_bending_strength(self) -> 'float':
        """float: 'UnitLoadForBendingStrength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UnitLoadForBendingStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'AGMA2101GearSingleFlankRating._Cast_AGMA2101GearSingleFlankRating':
        return self._Cast_AGMA2101GearSingleFlankRating(self)
