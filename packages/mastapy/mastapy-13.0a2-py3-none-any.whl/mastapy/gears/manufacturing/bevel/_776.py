"""_776.py

ConicalMeshFlankManufacturingConfig
"""
from mastapy.gears.manufacturing.bevel.control_parameters import _812
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _819, _818
from mastapy.gears.manufacturing.bevel import _777
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_FLANK_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshFlankManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshFlankManufacturingConfig',)


class ConicalMeshFlankManufacturingConfig(_777.ConicalMeshFlankMicroGeometryConfig):
    """ConicalMeshFlankManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_FLANK_MANUFACTURING_CONFIG

    class _Cast_ConicalMeshFlankManufacturingConfig:
        """Special nested class for casting ConicalMeshFlankManufacturingConfig to subclasses."""

        def __init__(self, parent: 'ConicalMeshFlankManufacturingConfig'):
            self._parent = parent

        @property
        def conical_mesh_flank_micro_geometry_config(self):
            return self._parent._cast(_777.ConicalMeshFlankMicroGeometryConfig)

        @property
        def conical_mesh_flank_manufacturing_config(self) -> 'ConicalMeshFlankManufacturingConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshFlankManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def control_parameters(self) -> '_812.ConicalGearManufacturingControlParameters':
        """ConicalGearManufacturingControlParameters: 'ControlParameters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ControlParameters

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def specified_cradle_style_machine_settings(self) -> '_819.CradleStyleConicalMachineSettingsGenerated':
        """CradleStyleConicalMachineSettingsGenerated: 'SpecifiedCradleStyleMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecifiedCradleStyleMachineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def specified_phoenix_style_machine_settings(self) -> '_818.BasicConicalGearMachineSettingsGenerated':
        """BasicConicalGearMachineSettingsGenerated: 'SpecifiedPhoenixStyleMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecifiedPhoenixStyleMachineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalMeshFlankManufacturingConfig._Cast_ConicalMeshFlankManufacturingConfig':
        return self._Cast_ConicalMeshFlankManufacturingConfig(self)
