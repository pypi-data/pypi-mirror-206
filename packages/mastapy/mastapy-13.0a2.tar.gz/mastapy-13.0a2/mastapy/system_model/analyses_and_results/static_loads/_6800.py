"""_6800.py

CoaxialConnectionLoadCase
"""
from mastapy.system_model.connections_and_sockets import _2250
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6915
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CoaxialConnectionLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionLoadCase',)


class CoaxialConnectionLoadCase(_6915.ShaftToMountableComponentConnectionLoadCase):
    """CoaxialConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_LOAD_CASE

    class _Cast_CoaxialConnectionLoadCase:
        """Special nested class for casting CoaxialConnectionLoadCase to subclasses."""

        def __init__(self, parent: 'CoaxialConnectionLoadCase'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_load_case(self):
            return self._parent._cast(_6915.ShaftToMountableComponentConnectionLoadCase)

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6774
            
            return self._parent._cast(_6774.AbstractShaftToMountableComponentConnectionLoadCase)

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
        def cycloidal_disc_central_bearing_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6822
            
            return self._parent._cast(_6822.CycloidalDiscCentralBearingConnectionLoadCase)

        @property
        def coaxial_connection_load_case(self) -> 'CoaxialConnectionLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2250.CoaxialConnection':
        """CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CoaxialConnectionLoadCase._Cast_CoaxialConnectionLoadCase':
        return self._Cast_CoaxialConnectionLoadCase(self)
