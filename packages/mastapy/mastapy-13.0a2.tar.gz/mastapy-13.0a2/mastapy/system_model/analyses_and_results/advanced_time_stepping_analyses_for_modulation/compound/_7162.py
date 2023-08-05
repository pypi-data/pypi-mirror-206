"""_7162.py

GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from typing import List

from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7032
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7168
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation',)


class GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(_7168.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation):
    """GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
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
        def agma_gleason_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7108
            
            return self._parent._cast(_7108.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7115
            
            return self._parent._cast(_7115.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7120
            
            return self._parent._cast(_7120.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7133
            
            return self._parent._cast(_7133.ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7136
            
            return self._parent._cast(_7136.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7151
            
            return self._parent._cast(_7151.CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7157
            
            return self._parent._cast(_7157.FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7166
            
            return self._parent._cast(_7166.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7170
            
            return self._parent._cast(_7170.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7173
            
            return self._parent._cast(_7173.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7176
            
            return self._parent._cast(_7176.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7203
            
            return self._parent._cast(_7203.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7209
            
            return self._parent._cast(_7209.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7212
            
            return self._parent._cast(_7212.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7227
            
            return self._parent._cast(_7227.WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7230
            
            return self._parent._cast(_7230.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_7032.GearMeshAdvancedTimeSteppingAnalysisForModulation]':
        """List[GearMeshAdvancedTimeSteppingAnalysisForModulation]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_7032.GearMeshAdvancedTimeSteppingAnalysisForModulation]':
        """List[GearMeshAdvancedTimeSteppingAnalysisForModulation]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(self)
