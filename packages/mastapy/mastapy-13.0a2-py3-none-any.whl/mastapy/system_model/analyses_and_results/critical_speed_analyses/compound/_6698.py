"""_6698.py

GearMeshCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6569
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6704
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'GearMeshCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundCriticalSpeedAnalysis',)


class GearMeshCompoundCriticalSpeedAnalysis(_6704.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis):
    """GearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_GearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting GearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'GearMeshCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(self):
            return self._parent._cast(_6704.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6674
            
            return self._parent._cast(_6674.ConnectionCompoundCriticalSpeedAnalysis)

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
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6644
            
            return self._parent._cast(_6644.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6651
            
            return self._parent._cast(_6651.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6656
            
            return self._parent._cast(_6656.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6669
            
            return self._parent._cast(_6669.ConceptGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6672
            
            return self._parent._cast(_6672.ConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6687
            
            return self._parent._cast(_6687.CylindricalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6693
            
            return self._parent._cast(_6693.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6702
            
            return self._parent._cast(_6702.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6706
            
            return self._parent._cast(_6706.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6709
            
            return self._parent._cast(_6709.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6712
            
            return self._parent._cast(_6712.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6739
            
            return self._parent._cast(_6739.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6745
            
            return self._parent._cast(_6745.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6748
            
            return self._parent._cast(_6748.StraightBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6763
            
            return self._parent._cast(_6763.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6766
            
            return self._parent._cast(_6766.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def gear_mesh_compound_critical_speed_analysis(self) -> 'GearMeshCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6569.GearMeshCriticalSpeedAnalysis]':
        """List[GearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6569.GearMeshCriticalSpeedAnalysis]':
        """List[GearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis':
        return self._Cast_GearMeshCompoundCriticalSpeedAnalysis(self)
