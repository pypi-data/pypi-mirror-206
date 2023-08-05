"""_853.py

CylindricalGearMeshLoadedContactLine
"""
from typing import List

from mastapy.gears.ltca.cylindrical import _854
from mastapy._internal import constructor, conversion
from mastapy.gears.ltca import _838
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_LOADED_CONTACT_LINE = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalGearMeshLoadedContactLine')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshLoadedContactLine',)


class CylindricalGearMeshLoadedContactLine(_838.GearMeshLoadedContactLine):
    """CylindricalGearMeshLoadedContactLine

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_LOADED_CONTACT_LINE

    class _Cast_CylindricalGearMeshLoadedContactLine:
        """Special nested class for casting CylindricalGearMeshLoadedContactLine to subclasses."""

        def __init__(self, parent: 'CylindricalGearMeshLoadedContactLine'):
            self._parent = parent

        @property
        def gear_mesh_loaded_contact_line(self):
            return self._parent._cast(_838.GearMeshLoadedContactLine)

        @property
        def cylindrical_gear_mesh_loaded_contact_line(self) -> 'CylindricalGearMeshLoadedContactLine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshLoadedContactLine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_contact_strip_end_points(self) -> 'List[_854.CylindricalGearMeshLoadedContactPoint]':
        """List[CylindricalGearMeshLoadedContactPoint]: 'LoadedContactStripEndPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedContactStripEndPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearMeshLoadedContactLine._Cast_CylindricalGearMeshLoadedContactLine':
        return self._Cast_CylindricalGearMeshLoadedContactLine(self)
