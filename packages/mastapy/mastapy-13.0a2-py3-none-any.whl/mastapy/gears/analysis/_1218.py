"""_1218.py

GearMeshImplementationAnalysisDutyCycle
"""
from mastapy.gears.analysis import _1216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_IMPLEMENTATION_ANALYSIS_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearMeshImplementationAnalysisDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshImplementationAnalysisDutyCycle',)


class GearMeshImplementationAnalysisDutyCycle(_1216.GearMeshDesignAnalysis):
    """GearMeshImplementationAnalysisDutyCycle

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_IMPLEMENTATION_ANALYSIS_DUTY_CYCLE

    class _Cast_GearMeshImplementationAnalysisDutyCycle:
        """Special nested class for casting GearMeshImplementationAnalysisDutyCycle to subclasses."""

        def __init__(self, parent: 'GearMeshImplementationAnalysisDutyCycle'):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(self):
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(self):
            from mastapy.gears.manufacturing.cylindrical import _613
            
            return self._parent._cast(_613.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(self) -> 'GearMeshImplementationAnalysisDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshImplementationAnalysisDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearMeshImplementationAnalysisDutyCycle._Cast_GearMeshImplementationAnalysisDutyCycle':
        return self._Cast_GearMeshImplementationAnalysisDutyCycle(self)
