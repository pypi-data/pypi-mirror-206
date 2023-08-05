"""_1130.py

CylindricalAccuracyGrader
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1132
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_ACCURACY_GRADER = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'CylindricalAccuracyGrader')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalAccuracyGrader',)


class CylindricalAccuracyGrader(_0.APIBase):
    """CylindricalAccuracyGrader

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_ACCURACY_GRADER

    class _Cast_CylindricalAccuracyGrader:
        """Special nested class for casting CylindricalAccuracyGrader to subclasses."""

        def __init__(self, parent: 'CylindricalAccuracyGrader'):
            self._parent = parent

        @property
        def agma2000a88_accuracy_grader(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1126
            
            return self._parent._cast(_1126.AGMA2000A88AccuracyGrader)

        @property
        def agma20151a01_accuracy_grader(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1127
            
            return self._parent._cast(_1127.AGMA20151A01AccuracyGrader)

        @property
        def agmaiso13281b14_accuracy_grader(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1129
            
            return self._parent._cast(_1129.AGMAISO13281B14AccuracyGrader)

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1131
            
            return self._parent._cast(_1131.CylindricalAccuracyGraderWithProfileFormAndSlope)

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
        def cylindrical_accuracy_grader(self) -> 'CylindricalAccuracyGrader':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalAccuracyGrader.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def tolerance_standard(self) -> 'str':
        """str: 'ToleranceStandard' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToleranceStandard

        if temp is None:
            return ''

        return temp

    @property
    def accuracy_grades(self) -> '_1132.CylindricalAccuracyGrades':
        """CylindricalAccuracyGrades: 'AccuracyGrades' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGrades

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader':
        return self._Cast_CylindricalAccuracyGrader(self)
