"""_4798.py

ShaftToMountableComponentConnectionCompoundModalAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses import _4654
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4704
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'ShaftToMountableComponentConnectionCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnectionCompoundModalAnalysis',)


class ShaftToMountableComponentConnectionCompoundModalAnalysis(_4704.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis):
    """ShaftToMountableComponentConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS

    class _Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'ShaftToMountableComponentConnectionCompoundModalAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(self):
            return self._parent._cast(_4704.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis)

        @property
        def connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4736
            
            return self._parent._cast(_4736.ConnectionCompoundModalAnalysis)

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
        def coaxial_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4725
            
            return self._parent._cast(_4725.CoaxialConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4745
            
            return self._parent._cast(_4745.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis)

        @property
        def planetary_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4784
            
            return self._parent._cast(_4784.PlanetaryConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(self) -> 'ShaftToMountableComponentConnectionCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnectionCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4654.ShaftToMountableComponentConnectionModalAnalysis]':
        """List[ShaftToMountableComponentConnectionModalAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4654.ShaftToMountableComponentConnectionModalAnalysis]':
        """List[ShaftToMountableComponentConnectionModalAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis':
        return self._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis(self)
