"""_880.py

ConicalGearLoadCase
"""
from mastapy.gears.load_case import _868
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Conical', 'ConicalGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearLoadCase',)


class ConicalGearLoadCase(_868.GearLoadCaseBase):
    """ConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_LOAD_CASE

    class _Cast_ConicalGearLoadCase:
        """Special nested class for casting ConicalGearLoadCase to subclasses."""

        def __init__(self, parent: 'ConicalGearLoadCase'):
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
        def bevel_load_case(self):
            from mastapy.gears.load_case.bevel import _886
            
            return self._parent._cast(_886.BevelLoadCase)

        @property
        def conical_gear_load_case(self) -> 'ConicalGearLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearLoadCase._Cast_ConicalGearLoadCase':
        return self._Cast_ConicalGearLoadCase(self)
