"""_2501.py

ConceptGearSet
"""
from typing import List

from mastapy.gears.gear_designs.concept import _1172
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2500, _2511
from mastapy.system_model.connections_and_sockets.gears import _2286
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSet',)


class ConceptGearSet(_2511.GearSet):
    """ConceptGearSet

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET

    class _Cast_ConceptGearSet:
        """Special nested class for casting ConceptGearSet to subclasses."""

        def __init__(self, parent: 'ConceptGearSet'):
            self._parent = parent

        @property
        def gear_set(self):
            return self._parent._cast(_2511.GearSet)

        @property
        def specialised_assembly(self):
            from mastapy.system_model.part_model import _2456
            
            return self._parent._cast(_2456.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2414
            
            return self._parent._cast(_2414.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def concept_gear_set(self) -> 'ConceptGearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self) -> '_1172.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gear_set_design(self) -> '_1172.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'ConceptGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gears(self) -> 'List[_2500.ConceptGear]':
        """List[ConceptGear]: 'ConceptGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes(self) -> 'List[_2286.ConceptGearMesh]':
        """List[ConceptGearMesh]: 'ConceptMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearSet._Cast_ConceptGearSet':
        return self._Cast_ConceptGearSet(self)
