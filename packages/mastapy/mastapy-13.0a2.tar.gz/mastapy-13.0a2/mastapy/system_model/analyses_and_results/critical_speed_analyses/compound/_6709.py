"""_6709.py

KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2300
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6580
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6706
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis',)


class KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis(_6706.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis):
    """KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(self):
            return self._parent._cast(_6706.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(self) -> 'KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2300.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2300.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6580.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6580.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis(self)
