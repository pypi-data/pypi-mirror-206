"""_5647.py

PartStaticLoadCaseGroup
"""
from typing import List

from mastapy.system_model.part_model import _2448
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6892
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5645
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups', 'PartStaticLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('PartStaticLoadCaseGroup',)


class PartStaticLoadCaseGroup(_5645.DesignEntityStaticLoadCaseGroup):
    """PartStaticLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _PART_STATIC_LOAD_CASE_GROUP

    class _Cast_PartStaticLoadCaseGroup:
        """Special nested class for casting PartStaticLoadCaseGroup to subclasses."""

        def __init__(self, parent: 'PartStaticLoadCaseGroup'):
            self._parent = parent

        @property
        def design_entity_static_load_case_group(self):
            return self._parent._cast(_5645.DesignEntityStaticLoadCaseGroup)

        @property
        def abstract_assembly_static_load_case_group(self):
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5642
            
            return self._parent._cast(_5642.AbstractAssemblyStaticLoadCaseGroup)

        @property
        def component_static_load_case_group(self):
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5643
            
            return self._parent._cast(_5643.ComponentStaticLoadCaseGroup)

        @property
        def gear_set_static_load_case_group(self):
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5646
            
            return self._parent._cast(_5646.GearSetStaticLoadCaseGroup)

        @property
        def part_static_load_case_group(self) -> 'PartStaticLoadCaseGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self) -> '_2448.Part':
        """Part: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_load_cases(self) -> 'List[_6892.PartLoadCase]':
        """List[PartLoadCase]: 'PartLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def clear_user_specified_excitation_data_for_all_load_cases(self):
        """ 'ClearUserSpecifiedExcitationDataForAllLoadCases' is the original name of this method."""

        self.wrapped.ClearUserSpecifiedExcitationDataForAllLoadCases()

    @property
    def cast_to(self) -> 'PartStaticLoadCaseGroup._Cast_PartStaticLoadCaseGroup':
        return self._Cast_PartStaticLoadCaseGroup(self)
