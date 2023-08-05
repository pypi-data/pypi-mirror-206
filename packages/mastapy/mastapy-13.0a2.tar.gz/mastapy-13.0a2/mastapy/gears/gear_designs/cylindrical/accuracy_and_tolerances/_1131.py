"""_1131.py

CylindricalAccuracyGraderWithProfileFormAndSlope
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1130
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_ACCURACY_GRADER_WITH_PROFILE_FORM_AND_SLOPE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'CylindricalAccuracyGraderWithProfileFormAndSlope')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalAccuracyGraderWithProfileFormAndSlope',)


class CylindricalAccuracyGraderWithProfileFormAndSlope(_1130.CylindricalAccuracyGrader):
    """CylindricalAccuracyGraderWithProfileFormAndSlope

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_ACCURACY_GRADER_WITH_PROFILE_FORM_AND_SLOPE

    class _Cast_CylindricalAccuracyGraderWithProfileFormAndSlope:
        """Special nested class for casting CylindricalAccuracyGraderWithProfileFormAndSlope to subclasses."""

        def __init__(self, parent: 'CylindricalAccuracyGraderWithProfileFormAndSlope'):
            self._parent = parent

        @property
        def cylindrical_accuracy_grader(self):
            return self._parent._cast(_1130.CylindricalAccuracyGrader)

        @property
        def agma20151a01_accuracy_grader(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1127
            
            return self._parent._cast(_1127.AGMA20151A01AccuracyGrader)

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
        def iso1328_accuracy_grader_common(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1137
            
            return self._parent._cast(_1137.ISO1328AccuracyGraderCommon)

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(self) -> 'CylindricalAccuracyGraderWithProfileFormAndSlope':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalAccuracyGraderWithProfileFormAndSlope.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_slope_deviation_per_inch_face_width(self) -> 'float':
        """float: 'HelixSlopeDeviationPerInchFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixSlopeDeviationPerInchFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_pitches_for_sector_pitch_deviation(self) -> 'int':
        """int: 'NumberOfPitchesForSectorPitchDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfPitchesForSectorPitchDeviation

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self) -> 'CylindricalAccuracyGraderWithProfileFormAndSlope._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope':
        return self._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope(self)
