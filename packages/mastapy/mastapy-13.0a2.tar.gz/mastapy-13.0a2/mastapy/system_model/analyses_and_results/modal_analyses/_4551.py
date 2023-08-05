"""_4551.py

AGMAGleasonConicalGearMeshModalAnalysis
"""
from mastapy.system_model.connections_and_sockets.gears import _2280
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2668
from mastapy.system_model.analyses_and_results.modal_analyses import _4579
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'AGMAGleasonConicalGearMeshModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearMeshModalAnalysis',)


class AGMAGleasonConicalGearMeshModalAnalysis(_4579.ConicalGearMeshModalAnalysis):
    """AGMAGleasonConicalGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_MODAL_ANALYSIS

    class _Cast_AGMAGleasonConicalGearMeshModalAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshModalAnalysis to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearMeshModalAnalysis'):
            self._parent = parent

        @property
        def conical_gear_mesh_modal_analysis(self):
            return self._parent._cast(_4579.ConicalGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609
            
            return self._parent._cast(_4609.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616
            
            return self._parent._cast(_4616.InterMountableComponentConnectionModalAnalysis)

        @property
        def connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582
            
            return self._parent._cast(_4582.ConnectionModalAnalysis)

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
        def bevel_differential_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4558
            
            return self._parent._cast(_4558.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4563
            
            return self._parent._cast(_4563.BevelGearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613
            
            return self._parent._cast(_4613.HypoidGearMeshModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4656
            
            return self._parent._cast(_4656.SpiralBevelGearMeshModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662
            
            return self._parent._cast(_4662.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665
            
            return self._parent._cast(_4665.StraightBevelGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686
            
            return self._parent._cast(_4686.ZerolBevelGearMeshModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(self) -> 'AGMAGleasonConicalGearMeshModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearMeshModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2280.AGMAGleasonConicalGearMesh':
        """AGMAGleasonConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2668.AGMAGleasonConicalGearMeshSystemDeflection':
        """AGMAGleasonConicalGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis':
        return self._Cast_AGMAGleasonConicalGearMeshModalAnalysis(self)
