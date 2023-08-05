"""_6463.py

RingPinsToDiscConnectionCompoundDynamicAnalysis
"""
from typing import List

from mastapy.system_model.connections_and_sockets.cycloidal import _2322
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6438
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'RingPinsToDiscConnectionCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsToDiscConnectionCompoundDynamicAnalysis',)


class RingPinsToDiscConnectionCompoundDynamicAnalysis(_6438.InterMountableComponentConnectionCompoundDynamicAnalysis):
    """RingPinsToDiscConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_RingPinsToDiscConnectionCompoundDynamicAnalysis:
        """Special nested class for casting RingPinsToDiscConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'RingPinsToDiscConnectionCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(self):
            return self._parent._cast(_6438.InterMountableComponentConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6408
            
            return self._parent._cast(_6408.ConnectionCompoundDynamicAnalysis)

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
        def ring_pins_to_disc_connection_compound_dynamic_analysis(self) -> 'RingPinsToDiscConnectionCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingPinsToDiscConnectionCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2322.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2322.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6334.RingPinsToDiscConnectionDynamicAnalysis]':
        """List[RingPinsToDiscConnectionDynamicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6334.RingPinsToDiscConnectionDynamicAnalysis]':
        """List[RingPinsToDiscConnectionDynamicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RingPinsToDiscConnectionCompoundDynamicAnalysis._Cast_RingPinsToDiscConnectionCompoundDynamicAnalysis':
        return self._Cast_RingPinsToDiscConnectionCompoundDynamicAnalysis(self)
