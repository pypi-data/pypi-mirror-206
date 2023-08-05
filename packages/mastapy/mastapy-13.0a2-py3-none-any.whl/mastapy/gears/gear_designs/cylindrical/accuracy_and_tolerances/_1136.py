"""_1136.py

ISO132812013AccuracyGrader
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1139, _1137
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO132812013_ACCURACY_GRADER = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'ISO132812013AccuracyGrader')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO132812013AccuracyGrader',)


class ISO132812013AccuracyGrader(_1137.ISO1328AccuracyGraderCommon):
    """ISO132812013AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _ISO132812013_ACCURACY_GRADER

    class _Cast_ISO132812013AccuracyGrader:
        """Special nested class for casting ISO132812013AccuracyGrader to subclasses."""

        def __init__(self, parent: 'ISO132812013AccuracyGrader'):
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
        def agmaiso13281b14_accuracy_grader(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1129
            
            return self._parent._cast(_1129.AGMAISO13281B14AccuracyGrader)

        @property
        def iso132812013_accuracy_grader(self) -> 'ISO132812013AccuracyGrader':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO132812013AccuracyGrader.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_value_for_toothto_tooth_single_flank_composite_deviation(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DesignValueForToothtoToothSingleFlankCompositeDeviation' is the original name of this property."""

        temp = self.wrapped.DesignValueForToothtoToothSingleFlankCompositeDeviation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @design_value_for_toothto_tooth_single_flank_composite_deviation.setter
    def design_value_for_toothto_tooth_single_flank_composite_deviation(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DesignValueForToothtoToothSingleFlankCompositeDeviation = value

    @property
    def adjacent_pitch_difference_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'AdjacentPitchDifferenceTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjacentPitchDifferenceTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def sector_pitch_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'SectorPitchTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SectorPitchTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def single_pitch_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'SinglePitchTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SinglePitchTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def toothto_tooth_single_flank_composite_tolerance_maximum(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'ToothtoToothSingleFlankCompositeToleranceMaximum' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothtoToothSingleFlankCompositeToleranceMaximum

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def toothto_tooth_single_flank_composite_tolerance_minimum(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'ToothtoToothSingleFlankCompositeToleranceMinimum' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothtoToothSingleFlankCompositeToleranceMinimum

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_cumulative_pitch_index_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'TotalCumulativePitchIndexTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalCumulativePitchIndexTolerance

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
    def total_single_flank_composite_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'TotalSingleFlankCompositeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalSingleFlankCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ISO132812013AccuracyGrader._Cast_ISO132812013AccuracyGrader':
        return self._Cast_ISO132812013AccuracyGrader(self)
