"""_5463.py

SpringDamperConnectionMultibodyDynamicsAnalysis
"""
from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets.couplings import _2331
from mastapy.system_model.analyses_and_results.static_loads import _6920
from mastapy.system_model.analyses_and_results.mbd_analyses import _5387
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'SpringDamperConnectionMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionMultibodyDynamicsAnalysis',)


class SpringDamperConnectionMultibodyDynamicsAnalysis(_5387.CouplingConnectionMultibodyDynamicsAnalysis):
    """SpringDamperConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_SpringDamperConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting SpringDamperConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'SpringDamperConnectionMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def coupling_connection_multibody_dynamics_analysis(self):
            return self._parent._cast(_5387.CouplingConnectionMultibodyDynamicsAnalysis)

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
        def spring_damper_connection_multibody_dynamics_analysis(self) -> 'SpringDamperConnectionMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force(self) -> 'Vector3D':
        """Vector3D: 'Force' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Force

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def moment(self) -> 'Vector3D':
        """Vector3D: 'Moment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Moment

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def relative_displacement(self) -> 'Vector3D':
        """Vector3D: 'RelativeDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def relative_rotation(self) -> 'Vector3D':
        """Vector3D: 'RelativeRotation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeRotation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def connection_design(self) -> '_2331.SpringDamperConnection':
        """SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6920.SpringDamperConnectionLoadCase':
        """SpringDamperConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis':
        return self._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis(self)
