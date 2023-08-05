"""_5318.py

SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2304
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5188
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'SpiralBevelGearMeshCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearMeshCompoundModalAnalysisAtASpeed',)


class SpiralBevelGearMeshCompoundModalAnalysisAtASpeed(_5235.BevelGearMeshCompoundModalAnalysisAtASpeed):
    """SpiralBevelGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SpiralBevelGearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'SpiralBevelGearMeshCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5235.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5223
            
            return self._parent._cast(_5223.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5251
            
            return self._parent._cast(_5251.ConicalGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5277
            
            return self._parent._cast(_5277.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5283
            
            return self._parent._cast(_5283.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5253
            
            return self._parent._cast(_5253.ConnectionCompoundModalAnalysisAtASpeed)

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
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(self) -> 'SpiralBevelGearMeshCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearMeshCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2304.SpiralBevelGearMesh':
        """SpiralBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2304.SpiralBevelGearMesh':
        """SpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5188.SpiralBevelGearMeshModalAnalysisAtASpeed]':
        """List[SpiralBevelGearMeshModalAnalysisAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5188.SpiralBevelGearMeshModalAnalysisAtASpeed]':
        """List[SpiralBevelGearMeshModalAnalysisAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed':
        return self._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed(self)
