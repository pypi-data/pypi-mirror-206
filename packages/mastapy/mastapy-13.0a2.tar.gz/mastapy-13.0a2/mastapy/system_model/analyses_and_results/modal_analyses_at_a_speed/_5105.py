"""_5105.py

BevelGearMeshModalAnalysisAtASpeed
"""
from mastapy.system_model.connections_and_sockets.gears import _2284
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5093
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'BevelGearMeshModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearMeshModalAnalysisAtASpeed',)


class BevelGearMeshModalAnalysisAtASpeed(_5093.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed):
    """BevelGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_BevelGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting BevelGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'BevelGearMeshModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5093.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5121
            
            return self._parent._cast(_5121.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5147
            
            return self._parent._cast(_5147.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5154
            
            return self._parent._cast(_5154.InterMountableComponentConnectionModalAnalysisAtASpeed)

        @property
        def connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5124
            
            return self._parent._cast(_5124.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7503
            
            return self._parent._cast(_7503.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7500
            
            return self._parent._cast(_7500.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2628
            
            return self._parent._cast(_2628.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5100
            
            return self._parent._cast(_5100.BevelDifferentialGearMeshModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5188
            
            return self._parent._cast(_5188.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5194
            
            return self._parent._cast(_5194.StraightBevelDiffGearMeshModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5197
            
            return self._parent._cast(_5197.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5215
            
            return self._parent._cast(_5215.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(self) -> 'BevelGearMeshModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearMeshModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2284.BevelGearMesh':
        """BevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed':
        return self._Cast_BevelGearMeshModalAnalysisAtASpeed(self)
