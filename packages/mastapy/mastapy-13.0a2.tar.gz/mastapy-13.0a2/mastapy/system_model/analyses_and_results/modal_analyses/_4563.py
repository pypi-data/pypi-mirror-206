"""_4563.py

BevelGearMeshModalAnalysis
"""
from mastapy.system_model.connections_and_sockets.gears import _2284
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2685
from mastapy.system_model.analyses_and_results.modal_analyses import _4551
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'BevelGearMeshModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearMeshModalAnalysis',)


class BevelGearMeshModalAnalysis(_4551.AGMAGleasonConicalGearMeshModalAnalysis):
    """BevelGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_MODAL_ANALYSIS

    class _Cast_BevelGearMeshModalAnalysis:
        """Special nested class for casting BevelGearMeshModalAnalysis to subclasses."""

        def __init__(self, parent: 'BevelGearMeshModalAnalysis'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(self):
            return self._parent._cast(_4551.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579
            
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
        def bevel_gear_mesh_modal_analysis(self) -> 'BevelGearMeshModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearMeshModalAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2685.BevelGearMeshSystemDeflection':
        """BevelGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis':
        return self._Cast_BevelGearMeshModalAnalysis(self)
