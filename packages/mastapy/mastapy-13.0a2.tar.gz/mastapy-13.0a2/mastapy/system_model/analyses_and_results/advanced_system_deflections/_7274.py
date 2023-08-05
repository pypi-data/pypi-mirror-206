"""_7274.py

CouplingConnectionAdvancedSystemDeflection
"""
from mastapy.system_model.connections_and_sockets.couplings import _2327
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7302
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'CouplingConnectionAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionAdvancedSystemDeflection',)


class CouplingConnectionAdvancedSystemDeflection(_7302.InterMountableComponentConnectionAdvancedSystemDeflection):
    """CouplingConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_CouplingConnectionAdvancedSystemDeflection:
        """Special nested class for casting CouplingConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'CouplingConnectionAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_advanced_system_deflection(self):
            return self._parent._cast(_7302.InterMountableComponentConnectionAdvancedSystemDeflection)

        @property
        def connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7270
            
            return self._parent._cast(_7270.ConnectionAdvancedSystemDeflection)

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
        def clutch_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7257
            
            return self._parent._cast(_7257.ClutchConnectionAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7262
            
            return self._parent._cast(_7262.ConceptCouplingConnectionAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7319
            
            return self._parent._cast(_7319.PartToPartShearCouplingConnectionAdvancedSystemDeflection)

        @property
        def spring_damper_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7341
            
            return self._parent._cast(_7341.SpringDamperConnectionAdvancedSystemDeflection)

        @property
        def torque_converter_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7356
            
            return self._parent._cast(_7356.TorqueConverterConnectionAdvancedSystemDeflection)

        @property
        def coupling_connection_advanced_system_deflection(self) -> 'CouplingConnectionAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2327.CouplingConnection':
        """CouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection':
        return self._Cast_CouplingConnectionAdvancedSystemDeflection(self)
