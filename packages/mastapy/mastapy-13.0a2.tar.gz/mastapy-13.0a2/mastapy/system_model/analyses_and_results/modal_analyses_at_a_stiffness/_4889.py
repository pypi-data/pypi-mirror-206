"""_4889.py

GearMeshModalAnalysisAtAStiffness
"""
from mastapy.system_model.connections_and_sockets.gears import _2294
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4896
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'GearMeshModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshModalAnalysisAtAStiffness',)


class GearMeshModalAnalysisAtAStiffness(_4896.InterMountableComponentConnectionModalAnalysisAtAStiffness):
    """GearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_GearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting GearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'GearMeshModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(self):
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
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4834
            
            return self._parent._cast(_4834.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4841
            
            return self._parent._cast(_4841.BevelDifferentialGearMeshModalAnalysisAtAStiffness)

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4846
            
            return self._parent._cast(_4846.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def concept_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4859
            
            return self._parent._cast(_4859.ConceptGearMeshModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4862
            
            return self._parent._cast(_4862.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4877
            
            return self._parent._cast(_4877.CylindricalGearMeshModalAnalysisAtAStiffness)

        @property
        def face_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4884
            
            return self._parent._cast(_4884.FaceGearMeshModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4893
            
            return self._parent._cast(_4893.HypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4897
            
            return self._parent._cast(_4897.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4900
            
            return self._parent._cast(_4900.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4903
            
            return self._parent._cast(_4903.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4930
            
            return self._parent._cast(_4930.SpiralBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4936
            
            return self._parent._cast(_4936.StraightBevelDiffGearMeshModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4939
            
            return self._parent._cast(_4939.StraightBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def worm_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4954
            
            return self._parent._cast(_4954.WormGearMeshModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4957
            
            return self._parent._cast(_4957.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(self) -> 'GearMeshModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2294.GearMesh':
        """GearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness':
        return self._Cast_GearMeshModalAnalysisAtAStiffness(self)
