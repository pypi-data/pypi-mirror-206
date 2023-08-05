"""_611.py

CylindricalManufacturedGearDutyCycle
"""
from mastapy.gears.analysis import _1214
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalManufacturedGearDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalManufacturedGearDutyCycle',)


class CylindricalManufacturedGearDutyCycle(_1214.GearImplementationAnalysisDutyCycle):
    """CylindricalManufacturedGearDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_DUTY_CYCLE

    class _Cast_CylindricalManufacturedGearDutyCycle:
        """Special nested class for casting CylindricalManufacturedGearDutyCycle to subclasses."""

        def __init__(self, parent: 'CylindricalManufacturedGearDutyCycle'):
            self._parent = parent

        @property
        def gear_implementation_analysis_duty_cycle(self):
            return self._parent._cast(_1214.GearImplementationAnalysisDutyCycle)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def cylindrical_manufactured_gear_duty_cycle(self) -> 'CylindricalManufacturedGearDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalManufacturedGearDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalManufacturedGearDutyCycle._Cast_CylindricalManufacturedGearDutyCycle':
        return self._Cast_CylindricalManufacturedGearDutyCycle(self)
