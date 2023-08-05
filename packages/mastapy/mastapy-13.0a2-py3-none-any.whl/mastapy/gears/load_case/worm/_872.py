"""_872.py

WormGearSetLoadCase
"""
from mastapy.gears.load_case import _869
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Worm', 'WormGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetLoadCase',)


class WormGearSetLoadCase(_869.GearSetLoadCaseBase):
    """WormGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_LOAD_CASE

    class _Cast_WormGearSetLoadCase:
        """Special nested class for casting WormGearSetLoadCase to subclasses."""

        def __init__(self, parent: 'WormGearSetLoadCase'):
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
        def worm_gear_set_load_case(self) -> 'WormGearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'WormGearSetLoadCase._Cast_WormGearSetLoadCase':
        return self._Cast_WormGearSetLoadCase(self)
