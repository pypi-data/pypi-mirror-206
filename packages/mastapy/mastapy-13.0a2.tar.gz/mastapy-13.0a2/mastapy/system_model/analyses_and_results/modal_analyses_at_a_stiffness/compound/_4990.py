"""_4990.py

ConceptGearMeshCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2286
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4859
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5019
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'ConceptGearMeshCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearMeshCompoundModalAnalysisAtAStiffness',)


class ConceptGearMeshCompoundModalAnalysisAtAStiffness(_5019.GearMeshCompoundModalAnalysisAtAStiffness):
    """ConceptGearMeshCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_ConceptGearMeshCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting ConceptGearMeshCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'ConceptGearMeshCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(self):
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
        def concept_gear_mesh_compound_modal_analysis_at_a_stiffness(self) -> 'ConceptGearMeshCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearMeshCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2286.ConceptGearMesh':
        """ConceptGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2286.ConceptGearMesh':
        """ConceptGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4859.ConceptGearMeshModalAnalysisAtAStiffness]':
        """List[ConceptGearMeshModalAnalysisAtAStiffness]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4859.ConceptGearMeshModalAnalysisAtAStiffness]':
        """List[ConceptGearMeshModalAnalysisAtAStiffness]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearMeshCompoundModalAnalysisAtAStiffness._Cast_ConceptGearMeshCompoundModalAnalysisAtAStiffness':
        return self._Cast_ConceptGearMeshCompoundModalAnalysisAtAStiffness(self)
