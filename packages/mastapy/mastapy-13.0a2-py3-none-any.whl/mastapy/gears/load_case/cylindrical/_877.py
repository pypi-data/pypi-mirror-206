"""_877.py

CylindricalGearLoadCase
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.load_case import _868
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Cylindrical', 'CylindricalGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearLoadCase',)


class CylindricalGearLoadCase(_868.GearLoadCaseBase):
    """CylindricalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LOAD_CASE

    class _Cast_CylindricalGearLoadCase:
        """Special nested class for casting CylindricalGearLoadCase to subclasses."""

        def __init__(self, parent: 'CylindricalGearLoadCase'):
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
        def cylindrical_gear_load_case(self) -> 'CylindricalGearLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def reversed_bending_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ReversedBendingFactor' is the original name of this property."""

        temp = self.wrapped.ReversedBendingFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @reversed_bending_factor.setter
    def reversed_bending_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ReversedBendingFactor = value

    @property
    def cast_to(self) -> 'CylindricalGearLoadCase._Cast_CylindricalGearLoadCase':
        return self._Cast_CylindricalGearLoadCase(self)
