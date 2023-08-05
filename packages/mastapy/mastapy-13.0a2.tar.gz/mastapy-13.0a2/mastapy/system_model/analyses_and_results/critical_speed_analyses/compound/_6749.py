"""_6749.py

StraightBevelGearSetCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.part_model.gears import _2527
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6620
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6747, _6748, _6657
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'StraightBevelGearSetCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetCompoundCriticalSpeedAnalysis',)


class StraightBevelGearSetCompoundCriticalSpeedAnalysis(_6657.BevelGearSetCompoundCriticalSpeedAnalysis):
    """StraightBevelGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'StraightBevelGearSetCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_set_compound_critical_speed_analysis(self):
            return self._parent._cast(_6657.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6645
            
            return self._parent._cast(_6645.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6673
            
            return self._parent._cast(_6673.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6699
            
            return self._parent._cast(_6699.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6737
            
            return self._parent._cast(_6737.SpecialisedAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def abstract_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6639
            
            return self._parent._cast(_6639.AbstractAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6718
            
            return self._parent._cast(_6718.PartCompoundCriticalSpeedAnalysis)

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
        def straight_bevel_gear_set_compound_critical_speed_analysis(self) -> 'StraightBevelGearSetCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2527.StraightBevelGearSet':
        """StraightBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2527.StraightBevelGearSet':
        """StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6620.StraightBevelGearSetCriticalSpeedAnalysis]':
        """List[StraightBevelGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gears_compound_critical_speed_analysis(self) -> 'List[_6747.StraightBevelGearCompoundCriticalSpeedAnalysis]':
        """List[StraightBevelGearCompoundCriticalSpeedAnalysis]: 'StraightBevelGearsCompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_compound_critical_speed_analysis(self) -> 'List[_6748.StraightBevelGearMeshCompoundCriticalSpeedAnalysis]':
        """List[StraightBevelGearMeshCompoundCriticalSpeedAnalysis]: 'StraightBevelMeshesCompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6620.StraightBevelGearSetCriticalSpeedAnalysis]':
        """List[StraightBevelGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis':
        return self._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis(self)
