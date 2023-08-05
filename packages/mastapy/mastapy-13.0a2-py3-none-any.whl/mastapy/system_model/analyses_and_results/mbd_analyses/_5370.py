"""_5370.py

ClutchConnectionMultibodyDynamicsAnalysis
"""
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.couplings import _2323
from mastapy.system_model.analyses_and_results.static_loads import _6797
from mastapy.system_model.analyses_and_results.mbd_analyses import _5387
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'ClutchConnectionMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionMultibodyDynamicsAnalysis',)


class ClutchConnectionMultibodyDynamicsAnalysis(_5387.CouplingConnectionMultibodyDynamicsAnalysis):
    """ClutchConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_ClutchConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting ClutchConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'ClutchConnectionMultibodyDynamicsAnalysis'):
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
        def clutch_connection_multibody_dynamics_analysis(self) -> 'ClutchConnectionMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchConnectionMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def applied_clutch_pressure_at_clutch_plate(self) -> 'float':
        """float: 'AppliedClutchPressureAtClutchPlate' is the original name of this property."""

        temp = self.wrapped.AppliedClutchPressureAtClutchPlate

        if temp is None:
            return 0.0

        return temp

    @applied_clutch_pressure_at_clutch_plate.setter
    def applied_clutch_pressure_at_clutch_plate(self, value: 'float'):
        self.wrapped.AppliedClutchPressureAtClutchPlate = float(value) if value else 0.0

    @property
    def applied_clutch_pressure_at_piston(self) -> 'float':
        """float: 'AppliedClutchPressureAtPiston' is the original name of this property."""

        temp = self.wrapped.AppliedClutchPressureAtPiston

        if temp is None:
            return 0.0

        return temp

    @applied_clutch_pressure_at_piston.setter
    def applied_clutch_pressure_at_piston(self, value: 'float'):
        self.wrapped.AppliedClutchPressureAtPiston = float(value) if value else 0.0

    @property
    def clutch_connection_elastic_torque(self) -> 'float':
        """float: 'ClutchConnectionElasticTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchConnectionElasticTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def clutch_connection_viscous_torque(self) -> 'float':
        """float: 'ClutchConnectionViscousTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchConnectionViscousTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def clutch_plate_dynamic_temperature(self) -> 'float':
        """float: 'ClutchPlateDynamicTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchPlateDynamicTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def clutch_torque_capacity(self) -> 'float':
        """float: 'ClutchTorqueCapacity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchTorqueCapacity

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_clutch_torque_capacity(self) -> 'float':
        """float: 'ExcessClutchTorqueCapacity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcessClutchTorqueCapacity

        if temp is None:
            return 0.0

        return temp

    @property
    def is_locked(self) -> 'bool':
        """bool: 'IsLocked' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsLocked

        if temp is None:
            return False

        return temp

    @property
    def percentage_applied_pressure(self) -> 'float':
        """float: 'PercentageAppliedPressure' is the original name of this property."""

        temp = self.wrapped.PercentageAppliedPressure

        if temp is None:
            return 0.0

        return temp

    @percentage_applied_pressure.setter
    def percentage_applied_pressure(self, value: 'float'):
        self.wrapped.PercentageAppliedPressure = float(value) if value else 0.0

    @property
    def power_loss(self) -> 'float':
        """float: 'PowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_shaft_displacement(self) -> 'float':
        """float: 'RelativeShaftDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeShaftDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_shaft_speed(self) -> 'float':
        """float: 'RelativeShaftSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeShaftSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self) -> '_2323.ClutchConnection':
        """ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6797.ClutchConnectionLoadCase':
        """ClutchConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis':
        return self._Cast_ClutchConnectionMultibodyDynamicsAnalysis(self)
