"""_2549.py

RingPins
"""
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import
from mastapy.cycloidal import _1450, _1451
from mastapy.system_model.part_model import _2444
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_RING_PINS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'RingPins')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPins',)


class RingPins(_2444.MountableComponent):
    """RingPins

    This is a mastapy class.
    """

    TYPE = _RING_PINS

    class _Cast_RingPins:
        """Special nested class for casting RingPins to subclasses."""

        def __init__(self, parent: 'RingPins'):
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
        def ring_pins(self) -> 'RingPins':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingPins.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def ring_pins_material_database(self) -> 'str':
        """str: 'RingPinsMaterialDatabase' is the original name of this property."""

        temp = self.wrapped.RingPinsMaterialDatabase.SelectedItemName

        if temp is None:
            return ''

        return temp

    @ring_pins_material_database.setter
    def ring_pins_material_database(self, value: 'str'):
        self.wrapped.RingPinsMaterialDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def ring_pins_design(self) -> '_1450.RingPinsDesign':
        """RingPinsDesign: 'RingPinsDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPinsDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_pins_material(self) -> '_1451.RingPinsMaterial':
        """RingPinsMaterial: 'RingPinsMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPinsMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RingPins._Cast_RingPins':
        return self._Cast_RingPins(self)
