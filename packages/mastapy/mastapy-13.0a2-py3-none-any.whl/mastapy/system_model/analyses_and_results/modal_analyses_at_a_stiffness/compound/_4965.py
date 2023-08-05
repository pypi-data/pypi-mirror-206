"""_4965.py

AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4834
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4993
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness',)


class AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness(_4993.ConicalGearMeshCompoundModalAnalysisAtAStiffness):
    """AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4993.ConicalGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5019
            
            return self._parent._cast(_5019.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5025
            
            return self._parent._cast(_5025.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4995
            
            return self._parent._cast(_4995.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4972
            
            return self._parent._cast(_4972.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4977
            
            return self._parent._cast(_4977.BevelGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5023
            
            return self._parent._cast(_5023.HypoidGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5060
            
            return self._parent._cast(_5060.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5066
            
            return self._parent._cast(_5066.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5069
            
            return self._parent._cast(_5069.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5087
            
            return self._parent._cast(_5087.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(self) -> 'AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4834.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness]':
        """List[AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4834.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness]':
        """List[AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness':
        return self._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness(self)
