"""_7271.py

ConnectorAdvancedSystemDeflection
"""
from mastapy.system_model.part_model import _2427
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7315
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ConnectorAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorAdvancedSystemDeflection',)


class ConnectorAdvancedSystemDeflection(_7315.MountableComponentAdvancedSystemDeflection):
    """ConnectorAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_ConnectorAdvancedSystemDeflection:
        """Special nested class for casting ConnectorAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'ConnectorAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def mountable_component_advanced_system_deflection(self):
            return self._parent._cast(_7315.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7260
            
            return self._parent._cast(_7260.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7317
            
            return self._parent._cast(_7317.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

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
        def bearing_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7243
            
            return self._parent._cast(_7243.BearingAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7316
            
            return self._parent._cast(_7316.OilSealAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7334
            
            return self._parent._cast(_7334.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(self) -> 'ConnectorAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorAdvancedSystemDeflection.TYPE'):
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
    def cast_to(self) -> 'ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection':
        return self._Cast_ConnectorAdvancedSystemDeflection(self)
