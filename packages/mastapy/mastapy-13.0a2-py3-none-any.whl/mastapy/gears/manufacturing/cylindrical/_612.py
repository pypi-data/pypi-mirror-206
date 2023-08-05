"""_612.py

CylindricalManufacturedGearLoadCase
"""
from mastapy.gears.analysis import _1213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalManufacturedGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalManufacturedGearLoadCase',)


class CylindricalManufacturedGearLoadCase(_1213.GearImplementationAnalysis):
    """CylindricalManufacturedGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_LOAD_CASE

    class _Cast_CylindricalManufacturedGearLoadCase:
        """Special nested class for casting CylindricalManufacturedGearLoadCase to subclasses."""

        def __init__(self, parent: 'CylindricalManufacturedGearLoadCase'):
            self._parent = parent

        @property
        def gear_implementation_analysis(self):
            return self._parent._cast(_1213.GearImplementationAnalysis)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def cylindrical_manufactured_gear_load_case(self) -> 'CylindricalManufacturedGearLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalManufacturedGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalManufacturedGearLoadCase._Cast_CylindricalManufacturedGearLoadCase':
        return self._Cast_CylindricalManufacturedGearLoadCase(self)
