"""_4954.py

WormGearMeshModalAnalysisAtAStiffness
"""
from mastapy.system_model.connections_and_sockets.gears import _2310
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6947
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4889
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'WormGearMeshModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearMeshModalAnalysisAtAStiffness',)


class WormGearMeshModalAnalysisAtAStiffness(_4889.GearMeshModalAnalysisAtAStiffness):
    """WormGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_WormGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting WormGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'WormGearMeshModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4889.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4896
            
            return self._parent._cast(_4896.InterMountableComponentConnectionModalAnalysisAtAStiffness)

        @property
        def connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4865
            
            return self._parent._cast(_4865.ConnectionModalAnalysisAtAStiffness)

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
        def worm_gear_mesh_modal_analysis_at_a_stiffness(self) -> 'WormGearMeshModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearMeshModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2310.WormGearMesh':
        """WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6947.WormGearMeshLoadCase':
        """WormGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGearMeshModalAnalysisAtAStiffness._Cast_WormGearMeshModalAnalysisAtAStiffness':
        return self._Cast_WormGearMeshModalAnalysisAtAStiffness(self)
