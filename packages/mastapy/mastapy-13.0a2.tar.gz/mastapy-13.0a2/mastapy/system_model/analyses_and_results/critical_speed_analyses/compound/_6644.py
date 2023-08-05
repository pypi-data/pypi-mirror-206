"""_6644.py

AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6513
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6672
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis',)


class AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis(_6672.ConicalGearMeshCompoundCriticalSpeedAnalysis):
    """AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(self):
            return self._parent._cast(_6672.ConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6698
            
            return self._parent._cast(_6698.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6704
            
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
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6651
            
            return self._parent._cast(_6651.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6656
            
            return self._parent._cast(_6656.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6702
            
            return self._parent._cast(_6702.HypoidGearMeshCompoundCriticalSpeedAnalysis)

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
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6766
            
            return self._parent._cast(_6766.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(self) -> 'AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6513.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]':
        """List[AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6513.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]':
        """List[AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis':
        return self._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis(self)
