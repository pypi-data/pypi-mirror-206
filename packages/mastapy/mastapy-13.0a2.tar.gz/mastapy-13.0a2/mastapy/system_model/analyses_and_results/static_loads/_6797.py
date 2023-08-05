"""_6797.py

ClutchConnectionLoadCase
"""
from mastapy._internal import constructor
from mastapy.math_utility import _1523
from mastapy.system_model.connections_and_sockets.couplings import _2323
from mastapy.system_model.analyses_and_results.static_loads import _6815
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ClutchConnectionLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionLoadCase',)


class ClutchConnectionLoadCase(_6815.CouplingConnectionLoadCase):
    """ClutchConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_LOAD_CASE

    class _Cast_ClutchConnectionLoadCase:
        """Special nested class for casting ClutchConnectionLoadCase to subclasses."""

        def __init__(self, parent: 'ClutchConnectionLoadCase'):
            self._parent = parent

        @property
        def coupling_connection_load_case(self):
            return self._parent._cast(_6815.CouplingConnectionLoadCase)

        @property
        def inter_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6875
            
            return self._parent._cast(_6875.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6813
            
            return self._parent._cast(_6813.ConnectionLoadCase)

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
        def clutch_connection_load_case(self) -> 'ClutchConnectionLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchConnectionLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutch_initial_temperature(self) -> 'float':
        """float: 'ClutchInitialTemperature' is the original name of this property."""

        temp = self.wrapped.ClutchInitialTemperature

        if temp is None:
            return 0.0

        return temp

    @clutch_initial_temperature.setter
    def clutch_initial_temperature(self, value: 'float'):
        self.wrapped.ClutchInitialTemperature = float(value) if value else 0.0

    @property
    def clutch_pressures(self) -> '_1523.Vector2DListAccessor':
        """Vector2DListAccessor: 'ClutchPressures' is the original name of this property."""

        temp = self.wrapped.ClutchPressures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @clutch_pressures.setter
    def clutch_pressures(self, value: '_1523.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.ClutchPressures = value

    @property
    def is_initially_locked(self) -> 'bool':
        """bool: 'IsInitiallyLocked' is the original name of this property."""

        temp = self.wrapped.IsInitiallyLocked

        if temp is None:
            return False

        return temp

    @is_initially_locked.setter
    def is_initially_locked(self, value: 'bool'):
        self.wrapped.IsInitiallyLocked = bool(value) if value else False

    @property
    def unlocked_clutch_linear_resistance_coefficient(self) -> 'float':
        """float: 'UnlockedClutchLinearResistanceCoefficient' is the original name of this property."""

        temp = self.wrapped.UnlockedClutchLinearResistanceCoefficient

        if temp is None:
            return 0.0

        return temp

    @unlocked_clutch_linear_resistance_coefficient.setter
    def unlocked_clutch_linear_resistance_coefficient(self, value: 'float'):
        self.wrapped.UnlockedClutchLinearResistanceCoefficient = float(value) if value else 0.0

    @property
    def use_fixed_update_time(self) -> 'bool':
        """bool: 'UseFixedUpdateTime' is the original name of this property."""

        temp = self.wrapped.UseFixedUpdateTime

        if temp is None:
            return False

        return temp

    @use_fixed_update_time.setter
    def use_fixed_update_time(self, value: 'bool'):
        self.wrapped.UseFixedUpdateTime = bool(value) if value else False

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
    def cast_to(self) -> 'ClutchConnectionLoadCase._Cast_ClutchConnectionLoadCase':
        return self._Cast_ClutchConnectionLoadCase(self)
