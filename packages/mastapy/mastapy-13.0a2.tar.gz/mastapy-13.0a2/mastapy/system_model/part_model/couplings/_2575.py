"""_2575.py

RollingRing
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears import _329
from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRing')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRing',)


class RollingRing(_2563.CouplingHalf):
    """RollingRing

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING

    class _Cast_RollingRing:
        """Special nested class for casting RollingRing to subclasses."""

        def __init__(self, parent: 'RollingRing'):
            self._parent = parent

        @property
        def coupling_half(self):
            return self._parent._cast(_2563.CouplingHalf)

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
        def rolling_ring(self) -> 'RollingRing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingRing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AverageDiameter' is the original name of this property."""

        temp = self.wrapped.AverageDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @average_diameter.setter
    def average_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AverageDiameter = value

    @property
    def is_internal(self) -> 'bool':
        """bool: 'IsInternal' is the original name of this property."""

        temp = self.wrapped.IsInternal

        if temp is None:
            return False

        return temp

    @is_internal.setter
    def is_internal(self, value: 'bool'):
        self.wrapped.IsInternal = bool(value) if value else False

    @property
    def largest_end(self) -> '_329.Hand':
        """Hand: 'LargestEnd' is the original name of this property."""

        temp = self.wrapped.LargestEnd

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _329.Hand)
        return constructor.new_from_mastapy_type(_329.Hand)(value) if value is not None else None

    @largest_end.setter
    def largest_end(self, value: '_329.Hand'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _329.Hand.type_())
        self.wrapped.LargestEnd = value

    @property
    def cast_to(self) -> 'RollingRing._Cast_RollingRing':
        return self._Cast_RollingRing(self)
