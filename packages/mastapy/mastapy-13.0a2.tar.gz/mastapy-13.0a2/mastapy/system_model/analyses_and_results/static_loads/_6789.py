"""_6789.py

BevelDifferentialGearSetLoadCase
"""
from typing import List

from mastapy.system_model.part_model.gears import _2495
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6787, _6788, _6794
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetLoadCase',)


class BevelDifferentialGearSetLoadCase(_6794.BevelGearSetLoadCase):
    """BevelDifferentialGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE

    class _Cast_BevelDifferentialGearSetLoadCase:
        """Special nested class for casting BevelDifferentialGearSetLoadCase to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearSetLoadCase'):
            self._parent = parent

        @property
        def bevel_gear_set_load_case(self):
            return self._parent._cast(_6794.BevelGearSetLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6780
            
            return self._parent._cast(_6780.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6812
            
            return self._parent._cast(_6812.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6859
            
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
        def bevel_differential_gear_set_load_case(self) -> 'BevelDifferentialGearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2495.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_6787.BevelDifferentialGearLoadCase]':
        """List[BevelDifferentialGearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gears_load_case(self) -> 'List[_6787.BevelDifferentialGearLoadCase]':
        """List[BevelDifferentialGearLoadCase]: 'BevelDifferentialGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_load_case(self) -> 'List[_6788.BevelDifferentialGearMeshLoadCase]':
        """List[BevelDifferentialGearMeshLoadCase]: 'BevelDifferentialMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase':
        return self._Cast_BevelDifferentialGearSetLoadCase(self)
