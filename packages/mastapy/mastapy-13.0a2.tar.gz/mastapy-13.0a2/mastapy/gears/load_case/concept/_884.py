"""_884.py

ConceptGearSetLoadCase
"""
from mastapy.gears.load_case import _869
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Concept', 'ConceptGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetLoadCase',)


class ConceptGearSetLoadCase(_869.GearSetLoadCaseBase):
    """ConceptGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_LOAD_CASE

    class _Cast_ConceptGearSetLoadCase:
        """Special nested class for casting ConceptGearSetLoadCase to subclasses."""

        def __init__(self, parent: 'ConceptGearSetLoadCase'):
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
        def concept_gear_set_load_case(self) -> 'ConceptGearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase':
        return self._Cast_ConceptGearSetLoadCase(self)
