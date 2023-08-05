"""_780.py

ConicalMeshManufacturingConfig
"""
from mastapy.gears.manufacturing.bevel import _783, _789, _782
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshManufacturingConfig',)


class ConicalMeshManufacturingConfig(_782.ConicalMeshMicroGeometryConfigBase):
    """ConicalMeshManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MANUFACTURING_CONFIG

    class _Cast_ConicalMeshManufacturingConfig:
        """Special nested class for casting ConicalMeshManufacturingConfig to subclasses."""

        def __init__(self, parent: 'ConicalMeshManufacturingConfig'):
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
        def conical_mesh_manufacturing_config(self) -> 'ConicalMeshManufacturingConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_config(self) -> '_783.ConicalPinionManufacturingConfig':
        """ConicalPinionManufacturingConfig: 'PinionConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config(self) -> '_789.ConicalWheelManufacturingConfig':
        """ConicalWheelManufacturingConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig':
        return self._Cast_ConicalMeshManufacturingConfig(self)
