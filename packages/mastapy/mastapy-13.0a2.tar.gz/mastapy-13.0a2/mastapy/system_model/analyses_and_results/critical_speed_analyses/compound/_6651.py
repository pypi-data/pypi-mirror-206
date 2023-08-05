"""_6651.py

BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2282
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6520
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6656
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis',)


class BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis(_6656.BevelGearMeshCompoundCriticalSpeedAnalysis):
    """BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(self):
            return self._parent._cast(_6656.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6644
            
            return self._parent._cast(_6644.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6672
            
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
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(self) -> 'BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2282.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2282.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6520.BevelDifferentialGearMeshCriticalSpeedAnalysis]':
        """List[BevelDifferentialGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6520.BevelDifferentialGearMeshCriticalSpeedAnalysis]':
        """List[BevelDifferentialGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis':
        return self._Cast_BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis(self)
