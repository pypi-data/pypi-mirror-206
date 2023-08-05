"""_881.py

ConicalGearSetLoadCase
"""
from mastapy.gears.load_case import _869
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Conical', 'ConicalGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetLoadCase',)


class ConicalGearSetLoadCase(_869.GearSetLoadCaseBase):
    """ConicalGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_LOAD_CASE

    class _Cast_ConicalGearSetLoadCase:
        """Special nested class for casting ConicalGearSetLoadCase to subclasses."""

        def __init__(self, parent: 'ConicalGearSetLoadCase'):
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
        def bevel_set_load_case(self):
            from mastapy.gears.load_case.bevel import _888
            
            return self._parent._cast(_888.BevelSetLoadCase)

        @property
        def conical_gear_set_load_case(self) -> 'ConicalGearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase':
        return self._Cast_ConicalGearSetLoadCase(self)
