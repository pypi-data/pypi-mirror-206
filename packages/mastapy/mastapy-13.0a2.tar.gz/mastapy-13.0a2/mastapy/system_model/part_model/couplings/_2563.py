"""_2563.py

CouplingHalf
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2444
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CouplingHalf')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalf',)


class CouplingHalf(_2444.MountableComponent):
    """CouplingHalf

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF

    class _Cast_CouplingHalf:
        """Special nested class for casting CouplingHalf to subclasses."""

        def __init__(self, parent: 'CouplingHalf'):
            self._parent = parent

        @property
        def mountable_component(self):
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
        def clutch_half(self):
            from mastapy.system_model.part_model.couplings import _2558
            
            return self._parent._cast(_2558.ClutchHalf)

        @property
        def concept_coupling_half(self):
            from mastapy.system_model.part_model.couplings import _2561
            
            return self._parent._cast(_2561.ConceptCouplingHalf)

        @property
        def cvt_pulley(self):
            from mastapy.system_model.part_model.couplings import _2566
            
            return self._parent._cast(_2566.CVTPulley)

        @property
        def part_to_part_shear_coupling_half(self):
            from mastapy.system_model.part_model.couplings import _2568
            
            return self._parent._cast(_2568.PartToPartShearCouplingHalf)

        @property
        def pulley(self):
            from mastapy.system_model.part_model.couplings import _2569
            
            return self._parent._cast(_2569.Pulley)

        @property
        def rolling_ring(self):
            from mastapy.system_model.part_model.couplings import _2575
            
            return self._parent._cast(_2575.RollingRing)

        @property
        def spring_damper_half(self):
            from mastapy.system_model.part_model.couplings import _2580
            
            return self._parent._cast(_2580.SpringDamperHalf)

        @property
        def synchroniser_half(self):
            from mastapy.system_model.part_model.couplings import _2583
            
            return self._parent._cast(_2583.SynchroniserHalf)

        @property
        def synchroniser_part(self):
            from mastapy.system_model.part_model.couplings import _2584
            
            return self._parent._cast(_2584.SynchroniserPart)

        @property
        def synchroniser_sleeve(self):
            from mastapy.system_model.part_model.couplings import _2585
            
            return self._parent._cast(_2585.SynchroniserSleeve)

        @property
        def torque_converter_pump(self):
            from mastapy.system_model.part_model.couplings import _2587
            
            return self._parent._cast(_2587.TorqueConverterPump)

        @property
        def torque_converter_turbine(self):
            from mastapy.system_model.part_model.couplings import _2589
            
            return self._parent._cast(_2589.TorqueConverterTurbine)

        @property
        def coupling_half(self) -> 'CouplingHalf':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalf.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Bore' is the original name of this property."""

        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @bore.setter
    def bore(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Bore = value

    @property
    def diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Diameter' is the original name of this property."""

        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @diameter.setter
    def diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Diameter = value

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
    def cast_to(self) -> 'CouplingHalf._Cast_CouplingHalf':
        return self._Cast_CouplingHalf(self)
