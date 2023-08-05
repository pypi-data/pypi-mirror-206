"""_2500.py

ConceptGear
"""
from mastapy.system_model.part_model.gears import _2510, _2509
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.concept import _1170
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGear')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGear',)


class ConceptGear(_2509.Gear):
    """ConceptGear

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR

    class _Cast_ConceptGear:
        """Special nested class for casting ConceptGear to subclasses."""

        def __init__(self, parent: 'ConceptGear'):
            self._parent = parent

        @property
        def gear(self):
            return self._parent._cast(_2509.Gear)

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
        def concept_gear(self) -> 'ConceptGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orientation(self) -> '_2510.GearOrientations':
        """GearOrientations: 'Orientation' is the original name of this property."""

        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _2510.GearOrientations)
        return constructor.new_from_mastapy_type(_2510.GearOrientations)(value) if value is not None else None

    @orientation.setter
    def orientation(self, value: '_2510.GearOrientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _2510.GearOrientations.type_())
        self.wrapped.Orientation = value

    @property
    def active_gear_design(self) -> '_1170.ConceptGearDesign':
        """ConceptGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gear_design(self) -> '_1170.ConceptGearDesign':
        """ConceptGearDesign: 'ConceptGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConceptGear._Cast_ConceptGear':
        return self._Cast_ConceptGear(self)
