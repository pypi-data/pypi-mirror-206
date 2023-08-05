"""_778.py

ConicalMeshFlankNurbsMicroGeometryConfig
"""
from mastapy.gears.manufacturing.bevel import _777
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_FLANK_NURBS_MICRO_GEOMETRY_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshFlankNurbsMicroGeometryConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshFlankNurbsMicroGeometryConfig',)


class ConicalMeshFlankNurbsMicroGeometryConfig(_777.ConicalMeshFlankMicroGeometryConfig):
    """ConicalMeshFlankNurbsMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_FLANK_NURBS_MICRO_GEOMETRY_CONFIG

    class _Cast_ConicalMeshFlankNurbsMicroGeometryConfig:
        """Special nested class for casting ConicalMeshFlankNurbsMicroGeometryConfig to subclasses."""

        def __init__(self, parent: 'ConicalMeshFlankNurbsMicroGeometryConfig'):
            self._parent = parent

        @property
        def conical_mesh_flank_micro_geometry_config(self):
            return self._parent._cast(_777.ConicalMeshFlankMicroGeometryConfig)

        @property
        def conical_mesh_flank_nurbs_micro_geometry_config(self) -> 'ConicalMeshFlankNurbsMicroGeometryConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshFlankNurbsMicroGeometryConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalMeshFlankNurbsMicroGeometryConfig._Cast_ConicalMeshFlankNurbsMicroGeometryConfig':
        return self._Cast_ConicalMeshFlankNurbsMicroGeometryConfig(self)
