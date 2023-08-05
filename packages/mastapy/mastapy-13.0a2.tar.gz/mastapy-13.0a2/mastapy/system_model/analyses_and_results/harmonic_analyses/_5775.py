"""_5775.py

ShaftToMountableComponentConnectionHarmonicAnalysis
"""
from mastapy.system_model.connections_and_sockets import _2276
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2784
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5652
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ShaftToMountableComponentConnectionHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnectionHarmonicAnalysis',)


class ShaftToMountableComponentConnectionHarmonicAnalysis(_5652.AbstractShaftToMountableComponentConnectionHarmonicAnalysis):
    """ShaftToMountableComponentConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS

    class _Cast_ShaftToMountableComponentConnectionHarmonicAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'ShaftToMountableComponentConnectionHarmonicAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(self):
            return self._parent._cast(_5652.AbstractShaftToMountableComponentConnectionHarmonicAnalysis)

        @property
        def connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5685
            
            return self._parent._cast(_5685.ConnectionHarmonicAnalysis)

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
        def coaxial_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5673
            
            return self._parent._cast(_5673.CoaxialConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5694
            
            return self._parent._cast(_5694.CycloidalDiscCentralBearingConnectionHarmonicAnalysis)

        @property
        def planetary_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5760
            
            return self._parent._cast(_5760.PlanetaryConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(self) -> 'ShaftToMountableComponentConnectionHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnectionHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2276.ShaftToMountableComponentConnection':
        """ShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2784.ShaftToMountableComponentConnectionSystemDeflection':
        """ShaftToMountableComponentConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis':
        return self._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis(self)
