"""_781.py

ConicalMeshMicroGeometryConfig
"""
from mastapy.gears.manufacturing.bevel import _782
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MICRO_GEOMETRY_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshMicroGeometryConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshMicroGeometryConfig',)


class ConicalMeshMicroGeometryConfig(_782.ConicalMeshMicroGeometryConfigBase):
    """ConicalMeshMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MICRO_GEOMETRY_CONFIG

    class _Cast_ConicalMeshMicroGeometryConfig:
        """Special nested class for casting ConicalMeshMicroGeometryConfig to subclasses."""

        def __init__(self, parent: 'ConicalMeshMicroGeometryConfig'):
            self._parent = parent

        @property
        def conical_mesh_micro_geometry_config_base(self):
            return self._parent._cast(_782.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_implementation_detail(self):
            from mastapy.gears.analysis import _1219
            
            return self._parent._cast(_1219.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1216
            
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_micro_geometry_config(self) -> 'ConicalMeshMicroGeometryConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshMicroGeometryConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalMeshMicroGeometryConfig._Cast_ConicalMeshMicroGeometryConfig':
        return self._Cast_ConicalMeshMicroGeometryConfig(self)
