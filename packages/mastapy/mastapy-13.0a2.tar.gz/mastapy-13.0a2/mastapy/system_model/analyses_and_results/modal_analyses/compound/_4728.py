"""_4728.py

ConceptCouplingConnectionCompoundModalAnalysis
"""
from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2325
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4573
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4739
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'ConceptCouplingConnectionCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionCompoundModalAnalysis',)


class ConceptCouplingConnectionCompoundModalAnalysis(_4739.CouplingConnectionCompoundModalAnalysis):
    """ConceptCouplingConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS

    class _Cast_ConceptCouplingConnectionCompoundModalAnalysis:
        """Special nested class for casting ConceptCouplingConnectionCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'ConceptCouplingConnectionCompoundModalAnalysis'):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis(self):
            return self._parent._cast(_4739.CouplingConnectionCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4766
            
            return self._parent._cast(_4766.InterMountableComponentConnectionCompoundModalAnalysis)

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
        def concept_coupling_connection_compound_modal_analysis(self) -> 'ConceptCouplingConnectionCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2325.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2325.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4573.ConceptCouplingConnectionModalAnalysis]':
        """List[ConceptCouplingConnectionModalAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4573.ConceptCouplingConnectionModalAnalysis]':
        """List[ConceptCouplingConnectionModalAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptCouplingConnectionCompoundModalAnalysis._Cast_ConceptCouplingConnectionCompoundModalAnalysis':
        return self._Cast_ConceptCouplingConnectionCompoundModalAnalysis(self)
