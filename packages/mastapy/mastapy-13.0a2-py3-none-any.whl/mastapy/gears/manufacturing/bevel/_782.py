"""_782.py

ConicalMeshMicroGeometryConfigBase
"""
from mastapy.gears.gear_designs.conical import _1149
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _773
from mastapy.gears.analysis import _1219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MICRO_GEOMETRY_CONFIG_BASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshMicroGeometryConfigBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshMicroGeometryConfigBase',)


class ConicalMeshMicroGeometryConfigBase(_1219.GearMeshImplementationDetail):
    """ConicalMeshMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MICRO_GEOMETRY_CONFIG_BASE

    class _Cast_ConicalMeshMicroGeometryConfigBase:
        """Special nested class for casting ConicalMeshMicroGeometryConfigBase to subclasses."""

        def __init__(self, parent: 'ConicalMeshMicroGeometryConfigBase'):
            self._parent = parent

        @property
        def gear_mesh_implementation_detail(self):
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
        def conical_mesh_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _780
            
            return self._parent._cast(_780.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _781
            
            return self._parent._cast(_781.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(self) -> 'ConicalMeshMicroGeometryConfigBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshMicroGeometryConfigBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh(self) -> '_1149.ConicalGearMeshDesign':
        """ConicalGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config(self) -> '_773.ConicalGearMicroGeometryConfigBase':
        """ConicalGearMicroGeometryConfigBase: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase':
        return self._Cast_ConicalMeshMicroGeometryConfigBase(self)
