"""_22.py

ShaftGroove
"""
from mastapy._internal import constructor
from mastapy.shafts import _42, _21
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_GROOVE = python_net_import('SMT.MastaAPI.Shafts', 'ShaftGroove')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftGroove',)


class ShaftGroove(_21.ShaftFeature):
    """ShaftGroove

    This is a mastapy class.
    """

    TYPE = _SHAFT_GROOVE

    class _Cast_ShaftGroove:
        """Special nested class for casting ShaftGroove to subclasses."""

        def __init__(self, parent: 'ShaftGroove'):
            self._parent = parent

        @property
        def shaft_feature(self):
            return self._parent._cast(_21.ShaftFeature)

        @property
        def shaft_groove(self) -> 'ShaftGroove':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftGroove.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def depth(self) -> 'float':
        """float: 'Depth' is the original name of this property."""

        temp = self.wrapped.Depth

        if temp is None:
            return 0.0

        return temp

    @depth.setter
    def depth(self, value: 'float'):
        self.wrapped.Depth = float(value) if value else 0.0

    @property
    def fillet_radius(self) -> 'float':
        """float: 'FilletRadius' is the original name of this property."""

        temp = self.wrapped.FilletRadius

        if temp is None:
            return 0.0

        return temp

    @fillet_radius.setter
    def fillet_radius(self, value: 'float'):
        self.wrapped.FilletRadius = float(value) if value else 0.0

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

    def add_new_groove(self):
        """ 'AddNewGroove' is the original name of this method."""

        self.wrapped.AddNewGroove()

    @property
    def cast_to(self) -> 'ShaftGroove._Cast_ShaftGroove':
        return self._Cast_ShaftGroove(self)
