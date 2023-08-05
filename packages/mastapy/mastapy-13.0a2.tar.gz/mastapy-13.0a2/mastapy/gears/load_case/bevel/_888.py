"""_888.py

BevelSetLoadCase
"""
from mastapy.gears.load_case.conical import _881
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Bevel', 'BevelSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelSetLoadCase',)


class BevelSetLoadCase(_881.ConicalGearSetLoadCase):
    """BevelSetLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_SET_LOAD_CASE

    class _Cast_BevelSetLoadCase:
        """Special nested class for casting BevelSetLoadCase to subclasses."""

        def __init__(self, parent: 'BevelSetLoadCase'):
            self._parent = parent

        @property
        def conical_gear_set_load_case(self):
            return self._parent._cast(_881.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case_base(self):
            from mastapy.gears.load_case import _869
            
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
        def bevel_set_load_case(self) -> 'BevelSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelSetLoadCase._Cast_BevelSetLoadCase':
        return self._Cast_BevelSetLoadCase(self)
