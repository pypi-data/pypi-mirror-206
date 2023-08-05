"""_1214.py

GearImplementationAnalysisDutyCycle
"""
from mastapy.gears.analysis import _1212
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_IMPLEMENTATION_ANALYSIS_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearImplementationAnalysisDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('GearImplementationAnalysisDutyCycle',)


class GearImplementationAnalysisDutyCycle(_1212.GearDesignAnalysis):
    """GearImplementationAnalysisDutyCycle

    This is a mastapy class.
    """

    TYPE = _GEAR_IMPLEMENTATION_ANALYSIS_DUTY_CYCLE

    class _Cast_GearImplementationAnalysisDutyCycle:
        """Special nested class for casting GearImplementationAnalysisDutyCycle to subclasses."""

        def __init__(self, parent: 'GearImplementationAnalysisDutyCycle'):
            self._parent = parent

        @property
        def gear_design_analysis(self):
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def cylindrical_manufactured_gear_duty_cycle(self):
            from mastapy.gears.manufacturing.cylindrical import _611
            
            return self._parent._cast(_611.CylindricalManufacturedGearDutyCycle)

        @property
        def gear_implementation_analysis_duty_cycle(self) -> 'GearImplementationAnalysisDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearImplementationAnalysisDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearImplementationAnalysisDutyCycle._Cast_GearImplementationAnalysisDutyCycle':
        return self._Cast_GearImplementationAnalysisDutyCycle(self)
