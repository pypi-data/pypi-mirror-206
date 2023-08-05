"""_1135.py

ISO132811995AccuracyGrader
"""
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1139, _1137
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO132811995_ACCURACY_GRADER = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'ISO132811995AccuracyGrader')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO132811995AccuracyGrader',)


class ISO132811995AccuracyGrader(_1137.ISO1328AccuracyGraderCommon):
    """ISO132811995AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _ISO132811995_ACCURACY_GRADER

    class _Cast_ISO132811995AccuracyGrader:
        """Special nested class for casting ISO132811995AccuracyGrader to subclasses."""

        def __init__(self, parent: 'ISO132811995AccuracyGrader'):
            self._parent = parent

        @property
        def iso1328_accuracy_grader_common(self):
            return self._parent._cast(_1137.ISO1328AccuracyGraderCommon)

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1131
            
            return self._parent._cast(_1131.CylindricalAccuracyGraderWithProfileFormAndSlope)

        @property
        def cylindrical_accuracy_grader(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1130
            
            return self._parent._cast(_1130.CylindricalAccuracyGrader)

        @property
        def iso132811995_accuracy_grader(self) -> 'ISO132811995AccuracyGrader':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO132811995AccuracyGrader.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cumulative_pitch_deviation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'CumulativePitchDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CumulativePitchDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def helix_form_deviation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'HelixFormDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixFormDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def helix_slope_deviation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'HelixSlopeDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixSlopeDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_form_deviation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'ProfileFormDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_slope_deviation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'ProfileSlopeDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def runout(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'Runout' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Runout

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def single_pitch_deviation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'SinglePitchDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SinglePitchDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_cumulative_pitch_deviation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'TotalCumulativePitchDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalCumulativePitchDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_helix_deviation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'TotalHelixDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalHelixDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_profile_deviation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'TotalProfileDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalProfileDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ISO132811995AccuracyGrader._Cast_ISO132811995AccuracyGrader':
        return self._Cast_ISO132811995AccuracyGrader(self)
