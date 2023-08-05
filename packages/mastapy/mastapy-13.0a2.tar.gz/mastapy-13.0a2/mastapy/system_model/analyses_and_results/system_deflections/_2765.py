"""_2765.py

PartToPartShearCouplingConnectionSystemDeflection
"""
from mastapy.system_model.connections_and_sockets.couplings import _2329
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6893
from mastapy.system_model.analyses_and_results.power_flows import _4090
from mastapy.system_model.analyses_and_results.system_deflections import _2708
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'PartToPartShearCouplingConnectionSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingConnectionSystemDeflection',)


class PartToPartShearCouplingConnectionSystemDeflection(_2708.CouplingConnectionSystemDeflection):
    """PartToPartShearCouplingConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_SYSTEM_DEFLECTION

    class _Cast_PartToPartShearCouplingConnectionSystemDeflection:
        """Special nested class for casting PartToPartShearCouplingConnectionSystemDeflection to subclasses."""

        def __init__(self, parent: 'PartToPartShearCouplingConnectionSystemDeflection'):
            self._parent = parent

        @property
        def coupling_connection_system_deflection(self):
            return self._parent._cast(_2708.CouplingConnectionSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2746
            
            return self._parent._cast(_2746.InterMountableComponentConnectionSystemDeflection)

        @property
        def connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2706
            
            return self._parent._cast(_2706.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7502
            
            return self._parent._cast(_7502.ConnectionFEAnalysis)

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
        def part_to_part_shear_coupling_connection_system_deflection(self) -> 'PartToPartShearCouplingConnectionSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2329.PartToPartShearCouplingConnection':
        """PartToPartShearCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6893.PartToPartShearCouplingConnectionLoadCase':
        """PartToPartShearCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4090.PartToPartShearCouplingConnectionPowerFlow':
        """PartToPartShearCouplingConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection':
        return self._Cast_PartToPartShearCouplingConnectionSystemDeflection(self)
