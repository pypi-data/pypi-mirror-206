"""_856.py

CylindricalMeshLoadDistributionAtRotation
"""
from typing import List

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1113
from mastapy._internal import constructor, conversion
from mastapy.gears.ltca.cylindrical import _853
from mastapy.gears.ltca import _837
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_LOAD_DISTRIBUTION_AT_ROTATION = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalMeshLoadDistributionAtRotation')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalMeshLoadDistributionAtRotation',)


class CylindricalMeshLoadDistributionAtRotation(_837.GearMeshLoadDistributionAtRotation):
    """CylindricalMeshLoadDistributionAtRotation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_LOAD_DISTRIBUTION_AT_ROTATION

    class _Cast_CylindricalMeshLoadDistributionAtRotation:
        """Special nested class for casting CylindricalMeshLoadDistributionAtRotation to subclasses."""

        def __init__(self, parent: 'CylindricalMeshLoadDistributionAtRotation'):
            self._parent = parent

        @property
        def gear_mesh_load_distribution_at_rotation(self):
            return self._parent._cast(_837.GearMeshLoadDistributionAtRotation)

        @property
        def cylindrical_mesh_load_distribution_at_rotation(self) -> 'CylindricalMeshLoadDistributionAtRotation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalMeshLoadDistributionAtRotation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_alignment(self) -> '_1113.MeshAlignment':
        """MeshAlignment: 'MeshAlignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshAlignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def loaded_contact_lines(self) -> 'List[_853.CylindricalGearMeshLoadedContactLine]':
        """List[CylindricalGearMeshLoadedContactLine]: 'LoadedContactLines' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedContactLines

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalMeshLoadDistributionAtRotation._Cast_CylindricalMeshLoadDistributionAtRotation':
        return self._Cast_CylindricalMeshLoadDistributionAtRotation(self)
