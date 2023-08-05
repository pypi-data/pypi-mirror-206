"""_874.py

FaceGearLoadCase
"""
from mastapy.gears.load_case import _868
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Face', 'FaceGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearLoadCase',)


class FaceGearLoadCase(_868.GearLoadCaseBase):
    """FaceGearLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_LOAD_CASE

    class _Cast_FaceGearLoadCase:
        """Special nested class for casting FaceGearLoadCase to subclasses."""

        def __init__(self, parent: 'FaceGearLoadCase'):
            self._parent = parent

        @property
        def gear_load_case_base(self):
            return self._parent._cast(_868.GearLoadCaseBase)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def face_gear_load_case(self) -> 'FaceGearLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FaceGearLoadCase._Cast_FaceGearLoadCase':
        return self._Cast_FaceGearLoadCase(self)
