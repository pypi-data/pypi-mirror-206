"""_6948.py

WormGearSetLoadCase
"""
from typing import List

from mastapy.system_model.part_model.gears import _2531
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6946, _6947, _6859
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'WormGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetLoadCase',)


class WormGearSetLoadCase(_6859.GearSetLoadCase):
    """WormGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_LOAD_CASE

    class _Cast_WormGearSetLoadCase:
        """Special nested class for casting WormGearSetLoadCase to subclasses."""

        def __init__(self, parent: 'WormGearSetLoadCase'):
            self._parent = parent

        @property
        def gear_set_load_case(self):
            return self._parent._cast(_6859.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6916
            
            return self._parent._cast(_6916.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6771
            
            return self._parent._cast(_6771.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.PartLoadCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def worm_gear_set_load_case(self) -> 'WormGearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2531.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_6946.WormGearLoadCase]':
        """List[WormGearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gears_load_case(self) -> 'List[_6946.WormGearLoadCase]':
        """List[WormGearLoadCase]: 'WormGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_load_case(self) -> 'List[_6947.WormGearMeshLoadCase]':
        """List[WormGearMeshLoadCase]: 'WormMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'WormGearSetLoadCase._Cast_WormGearSetLoadCase':
        return self._Cast_WormGearSetLoadCase(self)
