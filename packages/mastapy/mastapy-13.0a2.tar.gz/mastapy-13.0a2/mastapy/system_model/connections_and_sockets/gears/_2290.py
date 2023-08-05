"""_2290.py

CylindricalGearMesh
"""
from typing import List

from mastapy.math_utility import _1477
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1013
from mastapy.system_model.part_model.gears import _2505, _2504
from mastapy.system_model.connections_and_sockets.gears import _2294
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'CylindricalGearMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMesh',)


class CylindricalGearMesh(_2294.GearMesh):
    """CylindricalGearMesh

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH

    class _Cast_CylindricalGearMesh:
        """Special nested class for casting CylindricalGearMesh to subclasses."""

        def __init__(self, parent: 'CylindricalGearMesh'):
            self._parent = parent

        @property
        def gear_mesh(self):
            return self._parent._cast(_2294.GearMesh)

        @property
        def inter_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2262
            
            return self._parent._cast(_2262.InterMountableComponentConnection)

        @property
        def connection(self):
            from mastapy.system_model.connections_and_sockets import _2253
            
            return self._parent._cast(_2253.Connection)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def cylindrical_gear_mesh(self) -> 'CylindricalGearMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_distance_range(self) -> '_1477.Range':
        """Range: 'CentreDistanceRange' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CentreDistanceRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def centre_distance_with_normal_module_adjustment_by_scaling_entire_model(self) -> 'float':
        """float: 'CentreDistanceWithNormalModuleAdjustmentByScalingEntireModel' is the original name of this property."""

        temp = self.wrapped.CentreDistanceWithNormalModuleAdjustmentByScalingEntireModel

        if temp is None:
            return 0.0

        return temp

    @centre_distance_with_normal_module_adjustment_by_scaling_entire_model.setter
    def centre_distance_with_normal_module_adjustment_by_scaling_entire_model(self, value: 'float'):
        self.wrapped.CentreDistanceWithNormalModuleAdjustmentByScalingEntireModel = float(value) if value else 0.0

    @property
    def is_centre_distance_ready_to_change(self) -> 'bool':
        """bool: 'IsCentreDistanceReadyToChange' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsCentreDistanceReadyToChange

        if temp is None:
            return False

        return temp

    @property
    def override_design_pocketing_power_loss_coefficients(self) -> 'bool':
        """bool: 'OverrideDesignPocketingPowerLossCoefficients' is the original name of this property."""

        temp = self.wrapped.OverrideDesignPocketingPowerLossCoefficients

        if temp is None:
            return False

        return temp

    @override_design_pocketing_power_loss_coefficients.setter
    def override_design_pocketing_power_loss_coefficients(self, value: 'bool'):
        self.wrapped.OverrideDesignPocketingPowerLossCoefficients = bool(value) if value else False

    @property
    def active_gear_mesh_design(self) -> '_1013.CylindricalGearMeshDesign':
        """CylindricalGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_mesh_design(self) -> '_1013.CylindricalGearMeshDesign':
        """CylindricalGearMeshDesign: 'CylindricalGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_set(self) -> '_2505.CylindricalGearSet':
        """CylindricalGearSet: 'CylindricalGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gears(self) -> 'List[_2504.CylindricalGear]':
        """List[CylindricalGear]: 'CylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearMesh._Cast_CylindricalGearMesh':
        return self._Cast_CylindricalGearMesh(self)
