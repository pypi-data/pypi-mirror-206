"""_875.py

FaceGearSetLoadCase
"""
from mastapy.gears.load_case import _869
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Face', 'FaceGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetLoadCase',)


class FaceGearSetLoadCase(_869.GearSetLoadCaseBase):
    """FaceGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_LOAD_CASE

    class _Cast_FaceGearSetLoadCase:
        """Special nested class for casting FaceGearSetLoadCase to subclasses."""

        def __init__(self, parent: 'FaceGearSetLoadCase'):
            self._parent = parent

        @property
        def gear_set_load_case_base(self):
            return self._parent._cast(_869.GearSetLoadCaseBase)

        @property
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1220
            
            return self._parent._cast(_1220.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def face_gear_set_load_case(self) -> 'FaceGearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FaceGearSetLoadCase._Cast_FaceGearSetLoadCase':
        return self._Cast_FaceGearSetLoadCase(self)
