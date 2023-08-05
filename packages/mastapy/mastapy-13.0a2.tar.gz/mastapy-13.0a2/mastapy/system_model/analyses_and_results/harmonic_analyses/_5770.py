"""_5770.py

RollingRingConnectionHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.connections_and_sockets import _2273
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6910
from mastapy.system_model.analyses_and_results.system_deflections import _2777
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5741
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'RollingRingConnectionHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingConnectionHarmonicAnalysis',)


class RollingRingConnectionHarmonicAnalysis(_5741.InterMountableComponentConnectionHarmonicAnalysis):
    """RollingRingConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_HARMONIC_ANALYSIS

    class _Cast_RollingRingConnectionHarmonicAnalysis:
        """Special nested class for casting RollingRingConnectionHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'RollingRingConnectionHarmonicAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis(self):
            return self._parent._cast(_5741.InterMountableComponentConnectionHarmonicAnalysis)

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
        def rolling_ring_connection_harmonic_analysis(self) -> 'RollingRingConnectionHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingRingConnectionHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2273.RollingRingConnection':
        """RollingRingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6910.RollingRingConnectionLoadCase':
        """RollingRingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2777.RollingRingConnectionSystemDeflection':
        """RollingRingConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[RollingRingConnectionHarmonicAnalysis]':
        """List[RollingRingConnectionHarmonicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RollingRingConnectionHarmonicAnalysis._Cast_RollingRingConnectionHarmonicAnalysis':
        return self._Cast_RollingRingConnectionHarmonicAnalysis(self)
