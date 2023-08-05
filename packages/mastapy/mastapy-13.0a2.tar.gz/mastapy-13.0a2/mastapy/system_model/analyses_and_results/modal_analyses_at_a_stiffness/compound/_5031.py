"""_5031.py

KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.part_model.gears import _2518
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4902
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5029, _5030, _5028
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness',)


class KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness(_5028.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_5028.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4994
            
            return self._parent._cast(_4994.ConicalGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5020
            
            return self._parent._cast(_5020.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5058
            
            return self._parent._cast(_5058.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4960
            
            return self._parent._cast(_4960.AbstractAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5039
            
            return self._parent._cast(_5039.PartCompoundModalAnalysisAtAStiffness)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(self) -> 'KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2518.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2518.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4902.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness]':
        """List[KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_modal_analysis_at_a_stiffness(self) -> 'List[_5029.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness]':
        """List[KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness]: 'KlingelnbergCycloPalloidHypoidGearsCompoundModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_modal_analysis_at_a_stiffness(self) -> 'List[_5030.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness]: 'KlingelnbergCycloPalloidHypoidMeshesCompoundModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4902.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness]':
        """List[KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness(self)
