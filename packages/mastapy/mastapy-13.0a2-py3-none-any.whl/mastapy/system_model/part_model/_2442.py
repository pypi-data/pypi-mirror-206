"""_2442.py

MassDisc
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2459
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MassDisc')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDisc',)


class MassDisc(_2459.VirtualComponent):
    """MassDisc

    This is a mastapy class.
    """

    TYPE = _MASS_DISC

    class _Cast_MassDisc:
        """Special nested class for casting MassDisc to subclasses."""

        def __init__(self, parent: 'MassDisc'):
            self._parent = parent

        @property
        def virtual_component(self):
            return self._parent._cast(_2459.VirtualComponent)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2444
            
            return self._parent._cast(_2444.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2424
            
            return self._parent._cast(_2424.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def mass_disc(self) -> 'MassDisc':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MassDisc.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def density(self) -> 'float':
        """float: 'Density' is the original name of this property."""

        temp = self.wrapped.Density

        if temp is None:
            return 0.0

        return temp

    @density.setter
    def density(self, value: 'float'):
        self.wrapped.Density = float(value) if value else 0.0

    @property
    def disc_rotation(self) -> 'float':
        """float: 'DiscRotation' is the original name of this property."""

        temp = self.wrapped.DiscRotation

        if temp is None:
            return 0.0

        return temp

    @disc_rotation.setter
    def disc_rotation(self, value: 'float'):
        self.wrapped.DiscRotation = float(value) if value else 0.0

    @property
    def disc_skew(self) -> 'float':
        """float: 'DiscSkew' is the original name of this property."""

        temp = self.wrapped.DiscSkew

        if temp is None:
            return 0.0

        return temp

    @disc_skew.setter
    def disc_skew(self, value: 'float'):
        self.wrapped.DiscSkew = float(value) if value else 0.0

    @property
    def inner_diameter(self) -> 'float':
        """float: 'InnerDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def is_distributed(self) -> 'bool':
        """bool: 'IsDistributed' is the original name of this property."""

        temp = self.wrapped.IsDistributed

        if temp is None:
            return False

        return temp

    @is_distributed.setter
    def is_distributed(self, value: 'bool'):
        self.wrapped.IsDistributed = bool(value) if value else False

    @property
    def outer_diameter(self) -> 'float':
        """float: 'OuterDiameter' is the original name of this property."""

        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    def outer_diameter(self, value: 'float'):
        self.wrapped.OuterDiameter = float(value) if value else 0.0

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
    def cast_to(self) -> 'MassDisc._Cast_MassDisc':
        return self._Cast_MassDisc(self)
