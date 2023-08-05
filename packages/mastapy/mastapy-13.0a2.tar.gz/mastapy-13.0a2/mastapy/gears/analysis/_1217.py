"""_1217.py

GearMeshImplementationAnalysis
"""
from mastapy.gears.analysis import _1216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_IMPLEMENTATION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearMeshImplementationAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshImplementationAnalysis',)


class GearMeshImplementationAnalysis(_1216.GearMeshDesignAnalysis):
    """GearMeshImplementationAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_IMPLEMENTATION_ANALYSIS

    class _Cast_GearMeshImplementationAnalysis:
        """Special nested class for casting GearMeshImplementationAnalysis to subclasses."""

        def __init__(self, parent: 'GearMeshImplementationAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(self):
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _614
            
            return self._parent._cast(_614.CylindricalManufacturedGearMeshLoadCase)

        @property
        def conical_mesh_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _779
            
            return self._parent._cast(_779.ConicalMeshManufacturingAnalysis)

        @property
        def gear_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca import _836
            
            return self._parent._cast(_836.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _852
            
            return self._parent._cast(_852.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _865
            
            return self._parent._cast(_865.ConicalMeshLoadDistributionAnalysis)

        @property
        def gear_mesh_implementation_analysis(self) -> 'GearMeshImplementationAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshImplementationAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis':
        return self._Cast_GearMeshImplementationAnalysis(self)
