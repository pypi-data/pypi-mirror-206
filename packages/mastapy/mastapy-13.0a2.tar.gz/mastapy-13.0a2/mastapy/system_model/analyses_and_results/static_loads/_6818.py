"""_6818.py

CVTBeltConnectionLoadCase
"""
from mastapy.system_model.connections_and_sockets import _2254
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6785
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CVTBeltConnectionLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTBeltConnectionLoadCase',)


class CVTBeltConnectionLoadCase(_6785.BeltConnectionLoadCase):
    """CVTBeltConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_LOAD_CASE

    class _Cast_CVTBeltConnectionLoadCase:
        """Special nested class for casting CVTBeltConnectionLoadCase to subclasses."""

        def __init__(self, parent: 'CVTBeltConnectionLoadCase'):
            self._parent = parent

        @property
        def belt_connection_load_case(self):
            return self._parent._cast(_6785.BeltConnectionLoadCase)

        @property
        def inter_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6875
            
            return self._parent._cast(_6875.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6813
            
            return self._parent._cast(_6813.ConnectionLoadCase)

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
        def cvt_belt_connection_load_case(self) -> 'CVTBeltConnectionLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTBeltConnectionLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2254.CVTBeltConnection':
        """CVTBeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CVTBeltConnectionLoadCase._Cast_CVTBeltConnectionLoadCase':
        return self._Cast_CVTBeltConnectionLoadCase(self)
