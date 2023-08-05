"""_5469.py

StraightBevelGearMeshMultibodyDynamicsAnalysis
"""
from mastapy.system_model.connections_and_sockets.gears import _2308
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6927
from mastapy.system_model.analyses_and_results.mbd_analyses import _5365
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'StraightBevelGearMeshMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearMeshMultibodyDynamicsAnalysis',)


class StraightBevelGearMeshMultibodyDynamicsAnalysis(_5365.BevelGearMeshMultibodyDynamicsAnalysis):
    """StraightBevelGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'StraightBevelGearMeshMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(self):
            return self._parent._cast(_5365.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5351
            
            return self._parent._cast(_5351.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382
            
            return self._parent._cast(_5382.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408
            
            return self._parent._cast(_5408.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420
            
            return self._parent._cast(_5420.InterMountableComponentConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5385
            
            return self._parent._cast(_5385.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionTimeSeriesLoadAnalysisCase)

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
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(self) -> 'StraightBevelGearMeshMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearMeshMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2308.StraightBevelGearMesh':
        """StraightBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6927.StraightBevelGearMeshLoadCase':
        """StraightBevelGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis':
        return self._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis(self)
