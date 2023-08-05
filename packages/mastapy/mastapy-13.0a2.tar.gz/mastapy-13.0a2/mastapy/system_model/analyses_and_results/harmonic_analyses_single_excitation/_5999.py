"""_5999.py

CoaxialConnectionHarmonicAnalysisOfSingleExcitation
"""
from mastapy.system_model.connections_and_sockets import _2250
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6800
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6073
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'CoaxialConnectionHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionHarmonicAnalysisOfSingleExcitation',)


class CoaxialConnectionHarmonicAnalysisOfSingleExcitation(_6073.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation):
    """CoaxialConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_CoaxialConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CoaxialConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'CoaxialConnectionHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6073.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5978
            
            return self._parent._cast(_5978.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6010
            
            return self._parent._cast(_6010.ConnectionHarmonicAnalysisOfSingleExcitation)

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
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6019
            
            return self._parent._cast(_6019.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(self) -> 'CoaxialConnectionHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionHarmonicAnalysisOfSingleExcitation.TYPE'):
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
    def connection_load_case(self) -> '_6800.CoaxialConnectionLoadCase':
        """CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CoaxialConnectionHarmonicAnalysisOfSingleExcitation._Cast_CoaxialConnectionHarmonicAnalysisOfSingleExcitation':
        return self._Cast_CoaxialConnectionHarmonicAnalysisOfSingleExcitation(self)
