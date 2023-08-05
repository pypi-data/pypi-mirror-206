"""_1264.py

HairpinConductor
"""
from mastapy._internal import constructor
from mastapy.electric_machines import _1301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HAIRPIN_CONDUCTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'HairpinConductor')


__docformat__ = 'restructuredtext en'
__all__ = ('HairpinConductor',)


class HairpinConductor(_1301.WindingConductor):
    """HairpinConductor

    This is a mastapy class.
    """

    TYPE = _HAIRPIN_CONDUCTOR

    class _Cast_HairpinConductor:
        """Special nested class for casting HairpinConductor to subclasses."""

        def __init__(self, parent: 'HairpinConductor'):
            self._parent = parent

        @property
        def winding_conductor(self):
            return self._parent._cast(_1301.WindingConductor)

        @property
        def hairpin_conductor(self) -> 'HairpinConductor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HairpinConductor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self) -> 'float':
        """float: 'Angle' is the original name of this property."""

        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @angle.setter
    def angle(self, value: 'float'):
        self.wrapped.Angle = float(value) if value else 0.0

    @property
    def angle_offset(self) -> 'float':
        """float: 'AngleOffset' is the original name of this property."""

        temp = self.wrapped.AngleOffset

        if temp is None:
            return 0.0

        return temp

    @angle_offset.setter
    def angle_offset(self, value: 'float'):
        self.wrapped.AngleOffset = float(value) if value else 0.0

    @property
    def corner_radius(self) -> 'float':
        """float: 'CornerRadius' is the original name of this property."""

        temp = self.wrapped.CornerRadius

        if temp is None:
            return 0.0

        return temp

    @corner_radius.setter
    def corner_radius(self, value: 'float'):
        self.wrapped.CornerRadius = float(value) if value else 0.0

    @property
    def radial_offset(self) -> 'float':
        """float: 'RadialOffset' is the original name of this property."""

        temp = self.wrapped.RadialOffset

        if temp is None:
            return 0.0

        return temp

    @radial_offset.setter
    def radial_offset(self, value: 'float'):
        self.wrapped.RadialOffset = float(value) if value else 0.0

    @property
    def radius(self) -> 'float':
        """float: 'Radius' is the original name of this property."""

        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    def radius(self, value: 'float'):
        self.wrapped.Radius = float(value) if value else 0.0

    @property
    def winding_area(self) -> 'float':
        """float: 'WindingArea' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingArea

        if temp is None:
            return 0.0

        return temp

    @property
    def winding_material_height(self) -> 'float':
        """float: 'WindingMaterialHeight' is the original name of this property."""

        temp = self.wrapped.WindingMaterialHeight

        if temp is None:
            return 0.0

        return temp

    @winding_material_height.setter
    def winding_material_height(self, value: 'float'):
        self.wrapped.WindingMaterialHeight = float(value) if value else 0.0

    @property
    def winding_material_width(self) -> 'float':
        """float: 'WindingMaterialWidth' is the original name of this property."""

        temp = self.wrapped.WindingMaterialWidth

        if temp is None:
            return 0.0

        return temp

    @winding_material_width.setter
    def winding_material_width(self, value: 'float'):
        self.wrapped.WindingMaterialWidth = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'HairpinConductor._Cast_HairpinConductor':
        return self._Cast_HairpinConductor(self)
