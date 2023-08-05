"""_3975.py

SpiralBevelGearSetCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.part_model.gears import _2523
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3843
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3973, _3974, _3892
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'SpiralBevelGearSetCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCompoundStabilityAnalysis',)


class SpiralBevelGearSetCompoundStabilityAnalysis(_3892.BevelGearSetCompoundStabilityAnalysis):
    """SpiralBevelGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS

    class _Cast_SpiralBevelGearSetCompoundStabilityAnalysis:
        """Special nested class for casting SpiralBevelGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'SpiralBevelGearSetCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_set_compound_stability_analysis(self):
            return self._parent._cast(_3892.BevelGearSetCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3880
            
            return self._parent._cast(_3880.AGMAGleasonConicalGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3908
            
            return self._parent._cast(_3908.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3934
            
            return self._parent._cast(_3934.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3972
            
            return self._parent._cast(_3972.SpecialisedAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3874
            
            return self._parent._cast(_3874.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3953
            
            return self._parent._cast(_3953.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(self) -> 'SpiralBevelGearSetCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2523.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2523.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3843.SpiralBevelGearSetStabilityAnalysis]':
        """List[SpiralBevelGearSetStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gears_compound_stability_analysis(self) -> 'List[_3973.SpiralBevelGearCompoundStabilityAnalysis]':
        """List[SpiralBevelGearCompoundStabilityAnalysis]: 'SpiralBevelGearsCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearsCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_meshes_compound_stability_analysis(self) -> 'List[_3974.SpiralBevelGearMeshCompoundStabilityAnalysis]':
        """List[SpiralBevelGearMeshCompoundStabilityAnalysis]: 'SpiralBevelMeshesCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelMeshesCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3843.SpiralBevelGearSetStabilityAnalysis]':
        """List[SpiralBevelGearSetStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis':
        return self._Cast_SpiralBevelGearSetCompoundStabilityAnalysis(self)
