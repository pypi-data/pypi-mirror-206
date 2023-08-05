"""_1113.py

MeshAlignment
"""
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1107
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_ALIGNMENT = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'MeshAlignment')


__docformat__ = 'restructuredtext en'
__all__ = ('MeshAlignment',)


class MeshAlignment(_0.APIBase):
    """MeshAlignment

    This is a mastapy class.
    """

    TYPE = _MESH_ALIGNMENT

    class _Cast_MeshAlignment:
        """Special nested class for casting MeshAlignment to subclasses."""

        def __init__(self, parent: 'MeshAlignment'):
            self._parent = parent

        @property
        def mesh_alignment(self) -> 'MeshAlignment':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeshAlignment.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a_alignment(self) -> '_1107.GearAlignment':
        """GearAlignment: 'GearAAlignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearAAlignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_alignment(self) -> '_1107.GearAlignment':
        """GearAlignment: 'GearBAlignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBAlignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MeshAlignment._Cast_MeshAlignment':
        return self._Cast_MeshAlignment(self)
