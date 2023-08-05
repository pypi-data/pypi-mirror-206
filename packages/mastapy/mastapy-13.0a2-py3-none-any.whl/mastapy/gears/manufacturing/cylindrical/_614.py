"""_614.py

CylindricalManufacturedGearMeshLoadCase
"""
from mastapy.gears.analysis import _1217
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalManufacturedGearMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalManufacturedGearMeshLoadCase',)


class CylindricalManufacturedGearMeshLoadCase(_1217.GearMeshImplementationAnalysis):
    """CylindricalManufacturedGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_MESH_LOAD_CASE

    class _Cast_CylindricalManufacturedGearMeshLoadCase:
        """Special nested class for casting CylindricalManufacturedGearMeshLoadCase to subclasses."""

        def __init__(self, parent: 'CylindricalManufacturedGearMeshLoadCase'):
            self._parent = parent

        @property
        def gear_mesh_implementation_analysis(self):
            return self._parent._cast(_1217.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1216
            
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(self) -> 'CylindricalManufacturedGearMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalManufacturedGearMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalManufacturedGearMeshLoadCase._Cast_CylindricalManufacturedGearMeshLoadCase':
        return self._Cast_CylindricalManufacturedGearMeshLoadCase(self)
