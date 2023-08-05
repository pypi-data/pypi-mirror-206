"""_5929.py

PlanetaryConnectionCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.connections_and_sockets import _2268
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5760
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'PlanetaryConnectionCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryConnectionCompoundHarmonicAnalysis',)


class PlanetaryConnectionCompoundHarmonicAnalysis(_5943.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis):
    """PlanetaryConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_PlanetaryConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting PlanetaryConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'PlanetaryConnectionCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(self):
            return self._parent._cast(_5943.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5849
            
            return self._parent._cast(_5849.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5881
            
            return self._parent._cast(_5881.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def planetary_connection_compound_harmonic_analysis(self) -> 'PlanetaryConnectionCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryConnectionCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2268.PlanetaryConnection':
        """PlanetaryConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2268.PlanetaryConnection':
        """PlanetaryConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5760.PlanetaryConnectionHarmonicAnalysis]':
        """List[PlanetaryConnectionHarmonicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5760.PlanetaryConnectionHarmonicAnalysis]':
        """List[PlanetaryConnectionHarmonicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PlanetaryConnectionCompoundHarmonicAnalysis._Cast_PlanetaryConnectionCompoundHarmonicAnalysis':
        return self._Cast_PlanetaryConnectionCompoundHarmonicAnalysis(self)
