"""_4556.py

BeltConnectionModalAnalysis
"""
from mastapy.system_model.connections_and_sockets import _2249
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6785
from mastapy.system_model.analyses_and_results.system_deflections import _2678
from mastapy.system_model.analyses_and_results.modal_analyses import _4616
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'BeltConnectionModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionModalAnalysis',)


class BeltConnectionModalAnalysis(_4616.InterMountableComponentConnectionModalAnalysis):
    """BeltConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_MODAL_ANALYSIS

    class _Cast_BeltConnectionModalAnalysis:
        """Special nested class for casting BeltConnectionModalAnalysis to subclasses."""

        def __init__(self, parent: 'BeltConnectionModalAnalysis'):
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
        def cvt_belt_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588
            
            return self._parent._cast(_4588.CVTBeltConnectionModalAnalysis)

        @property
        def belt_connection_modal_analysis(self) -> 'BeltConnectionModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltConnectionModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2249.BeltConnection':
        """BeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6785.BeltConnectionLoadCase':
        """BeltConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2678.BeltConnectionSystemDeflection':
        """BeltConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BeltConnectionModalAnalysis._Cast_BeltConnectionModalAnalysis':
        return self._Cast_BeltConnectionModalAnalysis(self)
