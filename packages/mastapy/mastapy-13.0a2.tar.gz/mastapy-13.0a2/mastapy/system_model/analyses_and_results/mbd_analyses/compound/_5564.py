"""_5564.py

InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5420
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5534
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis',)


class InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(_5534.ConnectionCompoundMultibodyDynamicsAnalysis):
    """InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def connection_compound_multibody_dynamics_analysis(self):
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
        def belt_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5508
            
            return self._parent._cast(_5508.BeltConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5511
            
            return self._parent._cast(_5511.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5516
            
            return self._parent._cast(_5516.BevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5521
            
            return self._parent._cast(_5521.ClutchConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5526
            
            return self._parent._cast(_5526.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5529
            
            return self._parent._cast(_5529.ConceptGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5532
            
            return self._parent._cast(_5532.ConicalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5537
            
            return self._parent._cast(_5537.CouplingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5539
            
            return self._parent._cast(_5539.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5547
            
            return self._parent._cast(_5547.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5553
            
            return self._parent._cast(_5553.FaceGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5558
            
            return self._parent._cast(_5558.GearMeshCompoundMultibodyDynamicsAnalysis)

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
        def part_to_part_shear_coupling_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5580
            
            return self._parent._cast(_5580.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5589
            
            return self._parent._cast(_5589.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5592
            
            return self._parent._cast(_5592.RollingRingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5599
            
            return self._parent._cast(_5599.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5602
            
            return self._parent._cast(_5602.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5605
            
            return self._parent._cast(_5605.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5608
            
            return self._parent._cast(_5608.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5617
            
            return self._parent._cast(_5617.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5623
            
            return self._parent._cast(_5623.WormGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5626
            
            return self._parent._cast(_5626.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(self) -> 'InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_5420.InterMountableComponentConnectionMultibodyDynamicsAnalysis]':
        """List[InterMountableComponentConnectionMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5420.InterMountableComponentConnectionMultibodyDynamicsAnalysis]':
        """List[InterMountableComponentConnectionMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis':
        return self._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(self)
