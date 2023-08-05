"""_4866.py

ConnectorModalAnalysisAtAStiffness
"""
from mastapy.system_model.part_model import _2427
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4908
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'ConnectorModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorModalAnalysisAtAStiffness',)


class ConnectorModalAnalysisAtAStiffness(_4908.MountableComponentModalAnalysisAtAStiffness):
    """ConnectorModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_ConnectorModalAnalysisAtAStiffness:
        """Special nested class for casting ConnectorModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'ConnectorModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4908.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4855
            
            return self._parent._cast(_4855.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4910
            
            return self._parent._cast(_4910.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def bearing_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4838
            
            return self._parent._cast(_4838.BearingModalAnalysisAtAStiffness)

        @property
        def oil_seal_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4909
            
            return self._parent._cast(_4909.OilSealModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4926
            
            return self._parent._cast(_4926.ShaftHubConnectionModalAnalysisAtAStiffness)

        @property
        def connector_modal_analysis_at_a_stiffness(self) -> 'ConnectorModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2427.Connector':
        """Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness':
        return self._Cast_ConnectorModalAnalysisAtAStiffness(self)
