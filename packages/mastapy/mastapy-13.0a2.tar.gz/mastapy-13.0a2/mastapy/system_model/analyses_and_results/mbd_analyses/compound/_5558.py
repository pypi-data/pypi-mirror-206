"""_5558.py

GearMeshCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5408
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5564
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'GearMeshCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundMultibodyDynamicsAnalysis',)


class GearMeshCompoundMultibodyDynamicsAnalysis(_5564.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis):
    """GearMeshCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_GearMeshCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting GearMeshCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'GearMeshCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5564.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5534
            
            return self._parent._cast(_5534.ConnectionCompoundMultibodyDynamicsAnalysis)

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
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5504
            
            return self._parent._cast(_5504.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5511
            
            return self._parent._cast(_5511.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5516
            
            return self._parent._cast(_5516.BevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5529
            
            return self._parent._cast(_5529.ConceptGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5532
            
            return self._parent._cast(_5532.ConicalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5547
            
            return self._parent._cast(_5547.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5553
            
            return self._parent._cast(_5553.FaceGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5562
            
            return self._parent._cast(_5562.HypoidGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5566
            
            return self._parent._cast(_5566.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5569
            
            return self._parent._cast(_5569.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5572
            
            return self._parent._cast(_5572.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5599
            
            return self._parent._cast(_5599.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5605
            
            return self._parent._cast(_5605.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5608
            
            return self._parent._cast(_5608.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5623
            
            return self._parent._cast(_5623.WormGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5626
            
            return self._parent._cast(_5626.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(self) -> 'GearMeshCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_5408.GearMeshMultibodyDynamicsAnalysis]':
        """List[GearMeshMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5408.GearMeshMultibodyDynamicsAnalysis]':
        """List[GearMeshMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis':
        return self._Cast_GearMeshCompoundMultibodyDynamicsAnalysis(self)
