"""_6814.py

ConnectorLoadCase
"""
from mastapy.system_model.part_model import _2427
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6888
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConnectorLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorLoadCase',)


class ConnectorLoadCase(_6888.MountableComponentLoadCase):
    """ConnectorLoadCase

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_LOAD_CASE

    class _Cast_ConnectorLoadCase:
        """Special nested class for casting ConnectorLoadCase to subclasses."""

        def __init__(self, parent: 'ConnectorLoadCase'):
            self._parent = parent

        @property
        def mountable_component_load_case(self):
            return self._parent._cast(_6888.MountableComponentLoadCase)

        @property
        def component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6801
            
            return self._parent._cast(_6801.ComponentLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.PartLoadCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def bearing_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6784
            
            return self._parent._cast(_6784.BearingLoadCase)

        @property
        def oil_seal_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6890
            
            return self._parent._cast(_6890.OilSealLoadCase)

        @property
        def shaft_hub_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6913
            
            return self._parent._cast(_6913.ShaftHubConnectionLoadCase)

        @property
        def connector_load_case(self) -> 'ConnectorLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2427.Connector':
        """Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectorLoadCase._Cast_ConnectorLoadCase':
        return self._Cast_ConnectorLoadCase(self)
