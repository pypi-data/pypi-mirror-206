"""_5019.py

GearMeshCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4889
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5025
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'GearMeshCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundModalAnalysisAtAStiffness',)


class GearMeshCompoundModalAnalysisAtAStiffness(_5025.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness):
    """GearMeshCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_GearMeshCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting GearMeshCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'GearMeshCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(self):
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
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4965
            
            return self._parent._cast(_4965.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4972
            
            return self._parent._cast(_4972.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4977
            
            return self._parent._cast(_4977.BevelGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4990
            
            return self._parent._cast(_4990.ConceptGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4993
            
            return self._parent._cast(_4993.ConicalGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5008
            
            return self._parent._cast(_5008.CylindricalGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5014
            
            return self._parent._cast(_5014.FaceGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5023
            
            return self._parent._cast(_5023.HypoidGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5027
            
            return self._parent._cast(_5027.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5030
            
            return self._parent._cast(_5030.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5033
            
            return self._parent._cast(_5033.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness)

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
        def worm_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5084
            
            return self._parent._cast(_5084.WormGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5087
            
            return self._parent._cast(_5087.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(self) -> 'GearMeshCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4889.GearMeshModalAnalysisAtAStiffness]':
        """List[GearMeshModalAnalysisAtAStiffness]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4889.GearMeshModalAnalysisAtAStiffness]':
        """List[GearMeshModalAnalysisAtAStiffness]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshCompoundModalAnalysisAtAStiffness._Cast_GearMeshCompoundModalAnalysisAtAStiffness':
        return self._Cast_GearMeshCompoundModalAnalysisAtAStiffness(self)
