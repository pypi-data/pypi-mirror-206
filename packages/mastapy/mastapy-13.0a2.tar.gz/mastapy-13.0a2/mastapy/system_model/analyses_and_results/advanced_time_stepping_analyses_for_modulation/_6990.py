"""_6990.py

BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
"""
from mastapy.system_model.connections_and_sockets.gears import _2284
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2685
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6977
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'BevelGearMeshAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearMeshAdvancedTimeSteppingAnalysisForModulation',)


class BevelGearMeshAdvancedTimeSteppingAnalysisForModulation(_6977.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation):
    """BevelGearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelGearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'BevelGearMeshAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_6977.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7006
            
            return self._parent._cast(_7006.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7032
            
            return self._parent._cast(_7032.GearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7039
            
            return self._parent._cast(_7039.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7008
            
            return self._parent._cast(_7008.ConnectionAdvancedTimeSteppingAnalysisForModulation)

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
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6985
            
            return self._parent._cast(_6985.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7074
            
            return self._parent._cast(_7074.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7080
            
            return self._parent._cast(_7080.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7083
            
            return self._parent._cast(_7083.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7101
            
            return self._parent._cast(_7101.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self) -> 'BevelGearMeshAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2284.BevelGearMesh':
        """BevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2685.BevelGearMeshSystemDeflection':
        """BevelGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation(self)
