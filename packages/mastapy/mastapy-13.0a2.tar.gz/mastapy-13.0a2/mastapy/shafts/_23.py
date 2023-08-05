"""_23.py

ShaftKey
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.shafts import _45, _21
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_KEY = python_net_import('SMT.MastaAPI.Shafts', 'ShaftKey')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftKey',)


class ShaftKey(_21.ShaftFeature):
    """ShaftKey

    This is a mastapy class.
    """

    TYPE = _SHAFT_KEY

    class _Cast_ShaftKey:
        """Special nested class for casting ShaftKey to subclasses."""

        def __init__(self, parent: 'ShaftKey'):
            self._parent = parent

        @property
        def shaft_feature(self):
            return self._parent._cast(_21.ShaftFeature)

        @property
        def shaft_key(self) -> 'ShaftKey':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftKey.TYPE'):
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
    def number_of_keys(self) -> 'int':
        """int: 'NumberOfKeys' is the original name of this property."""

        temp = self.wrapped.NumberOfKeys

        if temp is None:
            return 0

        return temp

    @number_of_keys.setter
    def number_of_keys(self, value: 'int'):
        self.wrapped.NumberOfKeys = int(value) if value else 0

    @property
    def surface_finish(self) -> '_45.SurfaceFinishes':
        """SurfaceFinishes: 'SurfaceFinish' is the original name of this property."""

        temp = self.wrapped.SurfaceFinish

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _45.SurfaceFinishes)
        return constructor.new_from_mastapy_type(_45.SurfaceFinishes)(value) if value is not None else None

    @surface_finish.setter
    def surface_finish(self, value: '_45.SurfaceFinishes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _45.SurfaceFinishes.type_())
        self.wrapped.SurfaceFinish = value

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ShaftKey._Cast_ShaftKey':
        return self._Cast_ShaftKey(self)
