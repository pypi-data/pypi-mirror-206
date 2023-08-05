"""_4594.py

CycloidalDiscPlanetaryBearingConnectionModalAnalysis
"""
from mastapy.system_model.connections_and_sockets.cycloidal import _2319
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6824
from mastapy.system_model.analyses_and_results.system_deflections import _2716
from mastapy.system_model.analyses_and_results.modal_analyses import _4550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'CycloidalDiscPlanetaryBearingConnectionModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscPlanetaryBearingConnectionModalAnalysis',)


class CycloidalDiscPlanetaryBearingConnectionModalAnalysis(_4550.AbstractShaftToMountableComponentConnectionModalAnalysis):
    """CycloidalDiscPlanetaryBearingConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_MODAL_ANALYSIS

    class _Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysis:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionModalAnalysis to subclasses."""

        def __init__(self, parent: 'CycloidalDiscPlanetaryBearingConnectionModalAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis(self):
            return self._parent._cast(_4550.AbstractShaftToMountableComponentConnectionModalAnalysis)

        @property
        def connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582
            
            return self._parent._cast(_4582.ConnectionModalAnalysis)

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
        def cycloidal_disc_planetary_bearing_connection_modal_analysis(self) -> 'CycloidalDiscPlanetaryBearingConnectionModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscPlanetaryBearingConnectionModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2319.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6824.CycloidalDiscPlanetaryBearingConnectionLoadCase':
        """CycloidalDiscPlanetaryBearingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2716.CycloidalDiscPlanetaryBearingConnectionSystemDeflection':
        """CycloidalDiscPlanetaryBearingConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CycloidalDiscPlanetaryBearingConnectionModalAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysis':
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysis(self)
