"""_1219.py

GearMeshImplementationDetail
"""
from mastapy.gears.analysis import _1216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_IMPLEMENTATION_DETAIL = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearMeshImplementationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshImplementationDetail',)


class GearMeshImplementationDetail(_1216.GearMeshDesignAnalysis):
    """GearMeshImplementationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_IMPLEMENTATION_DETAIL

    class _Cast_GearMeshImplementationDetail:
        """Special nested class for casting GearMeshImplementationDetail to subclasses."""

        def __init__(self, parent: 'GearMeshImplementationDetail'):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(self):
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def cylindrical_mesh_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _617
            
            return self._parent._cast(_617.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _780
            
            return self._parent._cast(_780.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _781
            
            return self._parent._cast(_781.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _782
            
            return self._parent._cast(_782.ConicalMeshMicroGeometryConfigBase)

        @property
        def face_gear_mesh_micro_geometry(self):
            from mastapy.gears.gear_designs.face import _987
            
            return self._parent._cast(_987.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1092
            
            return self._parent._cast(_1092.CylindricalGearMeshMicroGeometry)

        @property
        def gear_mesh_fe_model(self):
            from mastapy.gears.fe_model import _1192
            
            return self._parent._cast(_1192.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1196
            
            return self._parent._cast(_1196.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(self):
            from mastapy.gears.fe_model.conical import _1199
            
            return self._parent._cast(_1199.ConicalMeshFEModel)

        @property
        def gear_mesh_implementation_detail(self) -> 'GearMeshImplementationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshImplementationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearMeshImplementationDetail._Cast_GearMeshImplementationDetail':
        return self._Cast_GearMeshImplementationDetail(self)
