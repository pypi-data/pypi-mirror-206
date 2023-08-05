"""_310.py

AccuracyGrades
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACCURACY_GRADES = python_net_import('SMT.MastaAPI.Gears', 'AccuracyGrades')


__docformat__ = 'restructuredtext en'
__all__ = ('AccuracyGrades',)


class AccuracyGrades(_0.APIBase):
    """AccuracyGrades

    This is a mastapy class.
    """

    TYPE = _ACCURACY_GRADES

    class _Cast_AccuracyGrades:
        """Special nested class for casting AccuracyGrades to subclasses."""

        def __init__(self, parent: 'AccuracyGrades'):
            self._parent = parent

        @property
        def agma20151_accuracy_grades(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1128
            
            return self._parent._cast(_1128.AGMA20151AccuracyGrades)

        @property
        def cylindrical_accuracy_grades(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1132
            
            return self._parent._cast(_1132.CylindricalAccuracyGrades)

        @property
        def iso1328_accuracy_grades(self):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1138
            
            return self._parent._cast(_1138.ISO1328AccuracyGrades)

        @property
        def agma_gleason_conical_accuracy_grades(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1186
            
            return self._parent._cast(_1186.AGMAGleasonConicalAccuracyGrades)

        @property
        def accuracy_grades(self) -> 'AccuracyGrades':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AccuracyGrades.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AccuracyGrades._Cast_AccuracyGrades':
        return self._Cast_AccuracyGrades(self)
