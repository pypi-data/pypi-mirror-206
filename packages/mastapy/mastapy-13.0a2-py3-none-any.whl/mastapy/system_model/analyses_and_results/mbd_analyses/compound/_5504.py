"""_5504.py

AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5351
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5532
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis',)


class AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis(_5532.ConicalGearMeshCompoundMultibodyDynamicsAnalysis):
    """AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5532.ConicalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5558
            
            return self._parent._cast(_5558.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5564
            
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
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5511
            
            return self._parent._cast(_5511.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5516
            
            return self._parent._cast(_5516.BevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5562
            
            return self._parent._cast(_5562.HypoidGearMeshCompoundMultibodyDynamicsAnalysis)

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
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5626
            
            return self._parent._cast(_5626.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(self) -> 'AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_5351.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis]':
        """List[AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5351.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis]':
        """List[AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis':
        return self._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis(self)
