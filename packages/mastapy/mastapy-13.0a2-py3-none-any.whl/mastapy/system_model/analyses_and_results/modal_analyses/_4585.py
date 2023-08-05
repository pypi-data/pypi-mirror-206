"""_4585.py

CouplingConnectionModalAnalysis
"""
from mastapy.system_model.connections_and_sockets.couplings import _2327
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2708
from mastapy.system_model.analyses_and_results.modal_analyses import _4616
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'CouplingConnectionModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionModalAnalysis',)


class CouplingConnectionModalAnalysis(_4616.InterMountableComponentConnectionModalAnalysis):
    """CouplingConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_MODAL_ANALYSIS

    class _Cast_CouplingConnectionModalAnalysis:
        """Special nested class for casting CouplingConnectionModalAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingConnectionModalAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis(self):
            return self._parent._cast(_4616.InterMountableComponentConnectionModalAnalysis)

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
        def clutch_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4568
            
            return self._parent._cast(_4568.ClutchConnectionModalAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573
            
            return self._parent._cast(_4573.ConceptCouplingConnectionModalAnalysis)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636
            
            return self._parent._cast(_4636.PartToPartShearCouplingConnectionModalAnalysis)

        @property
        def spring_damper_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659
            
            return self._parent._cast(_4659.SpringDamperConnectionModalAnalysis)

        @property
        def torque_converter_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674
            
            return self._parent._cast(_4674.TorqueConverterConnectionModalAnalysis)

        @property
        def coupling_connection_modal_analysis(self) -> 'CouplingConnectionModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2327.CouplingConnection':
        """CouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2708.CouplingConnectionSystemDeflection':
        """CouplingConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis':
        return self._Cast_CouplingConnectionModalAnalysis(self)
