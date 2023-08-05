"""_2527.py

StraightBevelGearSet
"""
from typing import List

from mastapy.gears.gear_designs.straight_bevel import _958
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2526, _2499
from mastapy.system_model.connections_and_sockets.gears import _2308
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSet',)


class StraightBevelGearSet(_2499.BevelGearSet):
    """StraightBevelGearSet

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET

    class _Cast_StraightBevelGearSet:
        """Special nested class for casting StraightBevelGearSet to subclasses."""

        def __init__(self, parent: 'StraightBevelGearSet'):
            self._parent = parent

        @property
        def bevel_gear_set(self):
            return self._parent._cast(_2499.BevelGearSet)

        @property
        def agma_gleason_conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2493
            
            return self._parent._cast(_2493.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2503
            
            return self._parent._cast(_2503.ConicalGearSet)

        @property
        def gear_set(self):
            from mastapy.system_model.part_model.gears import _2511
            
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
        def straight_bevel_gear_set(self) -> 'StraightBevelGearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self) -> '_958.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_gear_set_design(self) -> '_958.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'StraightBevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_gears(self) -> 'List[_2526.StraightBevelGear]':
        """List[StraightBevelGear]: 'StraightBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes(self) -> 'List[_2308.StraightBevelGearMesh]':
        """List[StraightBevelGearMesh]: 'StraightBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelGearSet._Cast_StraightBevelGearSet':
        return self._Cast_StraightBevelGearSet(self)
