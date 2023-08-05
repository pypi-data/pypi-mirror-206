"""_838.py

GearMeshLoadedContactLine
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.ltca import _839
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_LOADED_CONTACT_LINE = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearMeshLoadedContactLine')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshLoadedContactLine',)


class GearMeshLoadedContactLine(_0.APIBase):
    """GearMeshLoadedContactLine

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_LOADED_CONTACT_LINE

    class _Cast_GearMeshLoadedContactLine:
        """Special nested class for casting GearMeshLoadedContactLine to subclasses."""

        def __init__(self, parent: 'GearMeshLoadedContactLine'):
            self._parent = parent

        @property
        def cylindrical_gear_mesh_loaded_contact_line(self):
            from mastapy.gears.ltca.cylindrical import _853
            
            return self._parent._cast(_853.CylindricalGearMeshLoadedContactLine)

        @property
        def conical_mesh_loaded_contact_line(self):
            from mastapy.gears.ltca.conical import _867
            
            return self._parent._cast(_867.ConicalMeshLoadedContactLine)

        @property
        def gear_mesh_loaded_contact_line(self) -> 'GearMeshLoadedContactLine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshLoadedContactLine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_line_index(self) -> 'int':
        """int: 'ContactLineIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactLineIndex

        if temp is None:
            return 0

        return temp

    @property
    def mesh_position_index(self) -> 'int':
        """int: 'MeshPositionIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPositionIndex

        if temp is None:
            return 0

        return temp

    @property
    def tooth_number_of_gear_a(self) -> 'int':
        """int: 'ToothNumberOfGearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothNumberOfGearA

        if temp is None:
            return 0

        return temp

    @property
    def tooth_number_of_gear_b(self) -> 'int':
        """int: 'ToothNumberOfGearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothNumberOfGearB

        if temp is None:
            return 0

        return temp

    @property
    def loaded_contact_strip_end_points(self) -> 'List[_839.GearMeshLoadedContactPoint]':
        """List[GearMeshLoadedContactPoint]: 'LoadedContactStripEndPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedContactStripEndPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshLoadedContactLine._Cast_GearMeshLoadedContactLine':
        return self._Cast_GearMeshLoadedContactLine(self)
