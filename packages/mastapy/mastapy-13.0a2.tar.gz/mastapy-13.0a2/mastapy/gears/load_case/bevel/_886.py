"""_886.py

BevelLoadCase
"""
from mastapy.gears.load_case.conical import _880
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Bevel', 'BevelLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelLoadCase',)


class BevelLoadCase(_880.ConicalGearLoadCase):
    """BevelLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_LOAD_CASE

    class _Cast_BevelLoadCase:
        """Special nested class for casting BevelLoadCase to subclasses."""

        def __init__(self, parent: 'BevelLoadCase'):
            self._parent = parent

        @property
        def conical_gear_load_case(self):
            return self._parent._cast(_880.ConicalGearLoadCase)

        @property
        def gear_load_case_base(self):
            from mastapy.gears.load_case import _868
            
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
        def bevel_load_case(self) -> 'BevelLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelLoadCase._Cast_BevelLoadCase':
        return self._Cast_BevelLoadCase(self)
