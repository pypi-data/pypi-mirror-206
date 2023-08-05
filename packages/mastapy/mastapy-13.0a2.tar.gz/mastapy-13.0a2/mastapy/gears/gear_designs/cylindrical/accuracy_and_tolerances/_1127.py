"""_1127.py

AGMA20151A01AccuracyGrader
"""
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1139, _1131
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA20151A01_ACCURACY_GRADER = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'AGMA20151A01AccuracyGrader')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMA20151A01AccuracyGrader',)


class AGMA20151A01AccuracyGrader(_1131.CylindricalAccuracyGraderWithProfileFormAndSlope):
    """AGMA20151A01AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _AGMA20151A01_ACCURACY_GRADER

    class _Cast_AGMA20151A01AccuracyGrader:
        """Special nested class for casting AGMA20151A01AccuracyGrader to subclasses."""

        def __init__(self, parent: 'AGMA20151A01AccuracyGrader'):
            self._parent = parent

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(self):
            return self._parent._cast(_1131.CylindricalAccuracyGraderWithProfileFormAndSlope)

        @property
        def cylindrical_accuracy_grader(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1130
            
            return self._parent._cast(_1130.CylindricalAccuracyGrader)

        @property
        def agma20151a01_accuracy_grader(self) -> 'AGMA20151A01AccuracyGrader':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMA20151A01AccuracyGrader.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_form_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'HelixFormTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixFormTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def helix_slope_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'HelixSlopeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixSlopeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_form_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'ProfileFormTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_slope_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'ProfileSlopeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def runout_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'RunoutTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RunoutTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def sector_pitch_deviation_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'SectorPitchDeviationTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SectorPitchDeviationTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def single_flank_toothto_tooth_composite_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'SingleFlankToothtoToothCompositeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingleFlankToothtoToothCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def single_flank_total_composite_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'SingleFlankTotalCompositeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingleFlankTotalCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def single_pitch_deviation_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'SinglePitchDeviationTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SinglePitchDeviationTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def toothto_tooth_radial_composite_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'ToothtoToothRadialCompositeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothtoToothRadialCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_cumulative_pitch_deviation_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'TotalCumulativePitchDeviationTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalCumulativePitchDeviationTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_helix_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'TotalHelixTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalHelixTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_profile_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'TotalProfileTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalProfileTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_radial_composite_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'TotalRadialCompositeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalRadialCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AGMA20151A01AccuracyGrader._Cast_AGMA20151A01AccuracyGrader':
        return self._Cast_AGMA20151A01AccuracyGrader(self)
