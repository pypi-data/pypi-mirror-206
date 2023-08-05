"""_1132.py

CylindricalAccuracyGrades
"""
from mastapy._internal import constructor
from mastapy.gears import _310
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_ACCURACY_GRADES = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'CylindricalAccuracyGrades')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalAccuracyGrades',)


class CylindricalAccuracyGrades(_310.AccuracyGrades):
    """CylindricalAccuracyGrades

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_ACCURACY_GRADES

    class _Cast_CylindricalAccuracyGrades:
        """Special nested class for casting CylindricalAccuracyGrades to subclasses."""

        def __init__(self, parent: 'CylindricalAccuracyGrades'):
            self._parent = parent

        @property
        def accuracy_grades(self):
            return self._parent._cast(_310.AccuracyGrades)

        @property
        def agma20151_accuracy_grades(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1128
            
            return self._parent._cast(_1128.AGMA20151AccuracyGrades)

        @property
        def iso1328_accuracy_grades(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1138
            
            return self._parent._cast(_1138.ISO1328AccuracyGrades)

        @property
        def cylindrical_accuracy_grades(self) -> 'CylindricalAccuracyGrades':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalAccuracyGrades.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_quality_grade(self) -> 'int':
        """int: 'HelixQualityGrade' is the original name of this property."""

        temp = self.wrapped.HelixQualityGrade

        if temp is None:
            return 0

        return temp

    @helix_quality_grade.setter
    def helix_quality_grade(self, value: 'int'):
        self.wrapped.HelixQualityGrade = int(value) if value else 0

    @property
    def pitch_quality_grade(self) -> 'int':
        """int: 'PitchQualityGrade' is the original name of this property."""

        temp = self.wrapped.PitchQualityGrade

        if temp is None:
            return 0

        return temp

    @pitch_quality_grade.setter
    def pitch_quality_grade(self, value: 'int'):
        self.wrapped.PitchQualityGrade = int(value) if value else 0

    @property
    def profile_quality_grade(self) -> 'int':
        """int: 'ProfileQualityGrade' is the original name of this property."""

        temp = self.wrapped.ProfileQualityGrade

        if temp is None:
            return 0

        return temp

    @profile_quality_grade.setter
    def profile_quality_grade(self, value: 'int'):
        self.wrapped.ProfileQualityGrade = int(value) if value else 0

    @property
    def radial_quality_grade(self) -> 'int':
        """int: 'RadialQualityGrade' is the original name of this property."""

        temp = self.wrapped.RadialQualityGrade

        if temp is None:
            return 0

        return temp

    @radial_quality_grade.setter
    def radial_quality_grade(self, value: 'int'):
        self.wrapped.RadialQualityGrade = int(value) if value else 0

    @property
    def cast_to(self) -> 'CylindricalAccuracyGrades._Cast_CylindricalAccuracyGrades':
        return self._Cast_CylindricalAccuracyGrades(self)
