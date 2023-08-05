"""_33.py

ShaftRadialHole
"""
from mastapy._internal import constructor
from mastapy.shafts import _42, _21
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_RADIAL_HOLE = python_net_import('SMT.MastaAPI.Shafts', 'ShaftRadialHole')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftRadialHole',)


class ShaftRadialHole(_21.ShaftFeature):
    """ShaftRadialHole

    This is a mastapy class.
    """

    TYPE = _SHAFT_RADIAL_HOLE

    class _Cast_ShaftRadialHole:
        """Special nested class for casting ShaftRadialHole to subclasses."""

        def __init__(self, parent: 'ShaftRadialHole'):
            self._parent = parent

        @property
        def shaft_feature(self):
            return self._parent._cast(_21.ShaftFeature)

        @property
        def shaft_radial_hole(self) -> 'ShaftRadialHole':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftRadialHole.TYPE'):
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
    def diameter(self) -> 'float':
        """float: 'Diameter' is the original name of this property."""

        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @diameter.setter
    def diameter(self, value: 'float'):
        self.wrapped.Diameter = float(value) if value else 0.0

    @property
    def surface_roughness(self) -> '_42.ShaftSurfaceRoughness':
        """ShaftSurfaceRoughness: 'SurfaceRoughness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceRoughness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def add_new_radial_hole(self):
        """ 'AddNewRadialHole' is the original name of this method."""

        self.wrapped.AddNewRadialHole()

    @property
    def cast_to(self) -> 'ShaftRadialHole._Cast_ShaftRadialHole':
        return self._Cast_ShaftRadialHole(self)
