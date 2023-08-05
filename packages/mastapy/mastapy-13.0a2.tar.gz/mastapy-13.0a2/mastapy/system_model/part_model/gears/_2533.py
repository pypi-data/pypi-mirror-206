"""_2533.py

ZerolBevelGearSet
"""
from typing import List

from mastapy.gears.gear_designs.zerol_bevel import _949
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2532, _2499
from mastapy.system_model.connections_and_sockets.gears import _2312
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSet',)


class ZerolBevelGearSet(_2499.BevelGearSet):
    """ZerolBevelGearSet

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET

    class _Cast_ZerolBevelGearSet:
        """Special nested class for casting ZerolBevelGearSet to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearSet'):
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
        def zerol_bevel_gear_set(self) -> 'ZerolBevelGearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self) -> '_949.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gear_set_design(self) -> '_949.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'ZerolBevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gears(self) -> 'List[_2532.ZerolBevelGear]':
        """List[ZerolBevelGear]: 'ZerolBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes(self) -> 'List[_2312.ZerolBevelGearMesh]':
        """List[ZerolBevelGearMesh]: 'ZerolBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearSet._Cast_ZerolBevelGearSet':
        return self._Cast_ZerolBevelGearSet(self)
