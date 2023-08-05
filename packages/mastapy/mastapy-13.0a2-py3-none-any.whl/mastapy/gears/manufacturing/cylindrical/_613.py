"""_613.py

CylindricalManufacturedGearMeshDutyCycle
"""
from mastapy.gears.analysis import _1218
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_MESH_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalManufacturedGearMeshDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalManufacturedGearMeshDutyCycle',)


class CylindricalManufacturedGearMeshDutyCycle(_1218.GearMeshImplementationAnalysisDutyCycle):
    """CylindricalManufacturedGearMeshDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_MESH_DUTY_CYCLE

    class _Cast_CylindricalManufacturedGearMeshDutyCycle:
        """Special nested class for casting CylindricalManufacturedGearMeshDutyCycle to subclasses."""

        def __init__(self, parent: 'CylindricalManufacturedGearMeshDutyCycle'):
            self._parent = parent

        @property
        def gear_mesh_implementation_analysis_duty_cycle(self):
            return self._parent._cast(_1218.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1216
            
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(self) -> 'CylindricalManufacturedGearMeshDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalManufacturedGearMeshDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalManufacturedGearMeshDutyCycle._Cast_CylindricalManufacturedGearMeshDutyCycle':
        return self._Cast_CylindricalManufacturedGearMeshDutyCycle(self)
