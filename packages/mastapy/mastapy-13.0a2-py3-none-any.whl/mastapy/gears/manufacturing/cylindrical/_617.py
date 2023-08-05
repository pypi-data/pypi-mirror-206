"""_617.py

CylindricalMeshManufacturingConfig
"""
from typing import List

from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _726, _729, _730
from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalMeshManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalMeshManufacturingConfig',)


class CylindricalMeshManufacturingConfig(_1219.GearMeshImplementationDetail):
    """CylindricalMeshManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_MANUFACTURING_CONFIG

    class _Cast_CylindricalMeshManufacturingConfig:
        """Special nested class for casting CylindricalMeshManufacturingConfig to subclasses."""

        def __init__(self, parent: 'CylindricalMeshManufacturingConfig'):
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
        def cylindrical_mesh_manufacturing_config(self) -> 'CylindricalMeshManufacturingConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalMeshManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a_as_manufactured(self) -> 'List[_726.CutterSimulationCalc]':
        """List[CutterSimulationCalc]: 'GearAAsManufactured' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearAAsManufactured

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_b_as_manufactured(self) -> 'List[_726.CutterSimulationCalc]':
        """List[CutterSimulationCalc]: 'GearBAsManufactured' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBAsManufactured

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshed_gear_a_as_manufactured(self) -> 'List[_729.CylindricalManufacturedRealGearInMesh]':
        """List[CylindricalManufacturedRealGearInMesh]: 'MeshedGearAAsManufactured' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGearAAsManufactured

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshed_gear_a_as_manufactured_virtual(self) -> 'List[_730.CylindricalManufacturedVirtualGearInMesh]':
        """List[CylindricalManufacturedVirtualGearInMesh]: 'MeshedGearAAsManufacturedVirtual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGearAAsManufacturedVirtual

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshed_gear_b_as_manufactured(self) -> 'List[_729.CylindricalManufacturedRealGearInMesh]':
        """List[CylindricalManufacturedRealGearInMesh]: 'MeshedGearBAsManufactured' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGearBAsManufactured

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshed_gear_b_as_manufactured_virtual(self) -> 'List[_730.CylindricalManufacturedVirtualGearInMesh]':
        """List[CylindricalManufacturedVirtualGearInMesh]: 'MeshedGearBAsManufacturedVirtual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGearBAsManufacturedVirtual

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalMeshManufacturingConfig._Cast_CylindricalMeshManufacturingConfig':
        return self._Cast_CylindricalMeshManufacturingConfig(self)
