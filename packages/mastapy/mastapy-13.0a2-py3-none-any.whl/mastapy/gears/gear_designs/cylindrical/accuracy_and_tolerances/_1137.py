"""_1137.py

ISO1328AccuracyGraderCommon
"""
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1139, _1131
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO1328_ACCURACY_GRADER_COMMON = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'ISO1328AccuracyGraderCommon')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO1328AccuracyGraderCommon',)


class ISO1328AccuracyGraderCommon(_1131.CylindricalAccuracyGraderWithProfileFormAndSlope):
    """ISO1328AccuracyGraderCommon

    This is a mastapy class.
    """

    TYPE = _ISO1328_ACCURACY_GRADER_COMMON

    class _Cast_ISO1328AccuracyGraderCommon:
        """Special nested class for casting ISO1328AccuracyGraderCommon to subclasses."""

        def __init__(self, parent: 'ISO1328AccuracyGraderCommon'):
            self._parent = parent

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(self):
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
        def iso132811995_accuracy_grader(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1135
            
            return self._parent._cast(_1135.ISO132811995AccuracyGrader)

        @property
        def iso132812013_accuracy_grader(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1136
            
            return self._parent._cast(_1136.ISO132812013AccuracyGrader)

        @property
        def iso1328_accuracy_grader_common(self) -> 'ISO1328AccuracyGraderCommon':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO1328AccuracyGraderCommon.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_pitch_deviation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'BasePitchDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasePitchDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def toothto_tooth_radial_composite_deviation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'ToothtoToothRadialCompositeDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothtoToothRadialCompositeDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_radial_composite_deviation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'TotalRadialCompositeDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalRadialCompositeDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ISO1328AccuracyGraderCommon._Cast_ISO1328AccuracyGraderCommon':
        return self._Cast_ISO1328AccuracyGraderCommon(self)
