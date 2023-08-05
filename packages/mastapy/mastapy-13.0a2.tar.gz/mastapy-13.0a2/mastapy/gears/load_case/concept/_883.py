"""_883.py

ConceptGearLoadCase
"""
from mastapy.gears.load_case import _868
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Concept', 'ConceptGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearLoadCase',)


class ConceptGearLoadCase(_868.GearLoadCaseBase):
    """ConceptGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_LOAD_CASE

    class _Cast_ConceptGearLoadCase:
        """Special nested class for casting ConceptGearLoadCase to subclasses."""

        def __init__(self, parent: 'ConceptGearLoadCase'):
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
        def concept_gear_load_case(self) -> 'ConceptGearLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConceptGearLoadCase._Cast_ConceptGearLoadCase':
        return self._Cast_ConceptGearLoadCase(self)
