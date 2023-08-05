"""_1171.py

ConceptGearMeshDesign
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.concept import _1172, _1170
from mastapy.gears.gear_designs import _944
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Concept', 'ConceptGearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearMeshDesign',)


class ConceptGearMeshDesign(_944.GearMeshDesign):
    """ConceptGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_DESIGN

    class _Cast_ConceptGearMeshDesign:
        """Special nested class for casting ConceptGearMeshDesign to subclasses."""

        def __init__(self, parent: 'ConceptGearMeshDesign'):
            self._parent = parent

        @property
        def gear_mesh_design(self):
            return self._parent._cast(_944.GearMeshDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def concept_gear_mesh_design(self) -> 'ConceptGearMeshDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset(self) -> 'float':
        """float: 'Offset' is the original name of this property."""

        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    def offset(self, value: 'float'):
        self.wrapped.Offset = float(value) if value else 0.0

    @property
    def shaft_angle(self) -> 'float':
        """float: 'ShaftAngle' is the original name of this property."""

        temp = self.wrapped.ShaftAngle

        if temp is None:
            return 0.0

        return temp

    @shaft_angle.setter
    def shaft_angle(self, value: 'float'):
        self.wrapped.ShaftAngle = float(value) if value else 0.0

    @property
    def concept_gear_set(self) -> '_1172.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'ConceptGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gears(self) -> 'List[_1170.ConceptGearDesign]':
        """List[ConceptGearDesign]: 'ConceptGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearMeshDesign._Cast_ConceptGearMeshDesign':
        return self._Cast_ConceptGearMeshDesign(self)
