"""_7157.py

FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2292
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7027
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7162
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation',)


class FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(_7162.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation):
    """FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7162.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7168
            
            return self._parent._cast(_7168.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7138
            
            return self._parent._cast(_7138.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

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
        def face_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2292.FaceGearMesh':
        """FaceGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2292.FaceGearMesh':
        """FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_7027.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation]':
        """List[FaceGearMeshAdvancedTimeSteppingAnalysisForModulation]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_7027.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation]':
        """List[FaceGearMeshAdvancedTimeSteppingAnalysisForModulation]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(self)
