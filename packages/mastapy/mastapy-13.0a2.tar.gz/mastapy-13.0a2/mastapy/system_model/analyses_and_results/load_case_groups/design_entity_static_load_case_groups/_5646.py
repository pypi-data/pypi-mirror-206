"""_5646.py

GearSetStaticLoadCaseGroup
"""
from typing import List, TypeVar, Generic

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5643, _5644, _5647
from mastapy.system_model.part_model.gears import _2511, _2509
from mastapy.system_model.analyses_and_results.static_loads import _6854, _6856, _6859
from mastapy.system_model.connections_and_sockets.gears import _2294
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups', 'GearSetStaticLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetStaticLoadCaseGroup',)


TGearSet = TypeVar('TGearSet', bound='_2511.GearSet')
TGear = TypeVar('TGear', bound='_2509.Gear')
TGearStaticLoad = TypeVar('TGearStaticLoad', bound='_6854.GearLoadCase')
TGearMesh = TypeVar('TGearMesh', bound='_2294.GearMesh')
TGearMeshStaticLoad = TypeVar('TGearMeshStaticLoad', bound='_6856.GearMeshLoadCase')
TGearSetStaticLoad = TypeVar('TGearSetStaticLoad', bound='_6859.GearSetLoadCase')


class GearSetStaticLoadCaseGroup(_5647.PartStaticLoadCaseGroup, Generic[TGearSet, TGear, TGearStaticLoad, TGearMesh, TGearMeshStaticLoad, TGearSetStaticLoad]):
    """GearSetStaticLoadCaseGroup

    This is a mastapy class.

    Generic Types:
        TGearSet
        TGear
        TGearStaticLoad
        TGearMesh
        TGearMeshStaticLoad
        TGearSetStaticLoad
    """

    TYPE = _GEAR_SET_STATIC_LOAD_CASE_GROUP

    class _Cast_GearSetStaticLoadCaseGroup:
        """Special nested class for casting GearSetStaticLoadCaseGroup to subclasses."""

        def __init__(self, parent: 'GearSetStaticLoadCaseGroup'):
            self._parent = parent

        @property
        def part_static_load_case_group(self):
            return self._parent._cast(_5647.PartStaticLoadCaseGroup)

        @property
        def design_entity_static_load_case_group(self):
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5645
            
            return self._parent._cast(_5645.DesignEntityStaticLoadCaseGroup)

        @property
        def gear_set_static_load_case_group(self) -> 'GearSetStaticLoadCaseGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self) -> 'TGearSet':
        """TGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(TGearSet)(temp) if temp is not None else None

    @property
    def gear_set(self) -> 'TGearSet':
        """TGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(TGearSet)(temp) if temp is not None else None

    @property
    def part_load_cases(self) -> 'List[TGearSetStaticLoad]':
        """List[TGearSetStaticLoad]: 'PartLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_set_load_cases(self) -> 'List[TGearSetStaticLoad]':
        """List[TGearSetStaticLoad]: 'GearSetLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gears_load_cases(self) -> 'List[_5643.ComponentStaticLoadCaseGroup[TGear, TGearStaticLoad]]':
        """List[ComponentStaticLoadCaseGroup[TGear, TGearStaticLoad]]: 'GearsLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_load_cases(self) -> 'List[_5644.ConnectionStaticLoadCaseGroup[TGearMesh, TGearMeshStaticLoad]]':
        """List[ConnectionStaticLoadCaseGroup[TGearMesh, TGearMeshStaticLoad]]: 'MeshesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearSetStaticLoadCaseGroup._Cast_GearSetStaticLoadCaseGroup':
        return self._Cast_GearSetStaticLoadCaseGroup(self)
