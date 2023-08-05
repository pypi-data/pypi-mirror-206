"""_6785.py

BeltConnectionLoadCase
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.connections_and_sockets import _2249
from mastapy.system_model.analyses_and_results.static_loads import _6875
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BeltConnectionLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionLoadCase',)


class BeltConnectionLoadCase(_6875.InterMountableComponentConnectionLoadCase):
    """BeltConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_LOAD_CASE

    class _Cast_BeltConnectionLoadCase:
        """Special nested class for casting BeltConnectionLoadCase to subclasses."""

        def __init__(self, parent: 'BeltConnectionLoadCase'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_load_case(self):
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
        def cvt_belt_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6818
            
            return self._parent._cast(_6818.CVTBeltConnectionLoadCase)

        @property
        def belt_connection_load_case(self) -> 'BeltConnectionLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltConnectionLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pre_extension(self) -> 'float':
        """float: 'PreExtension' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PreExtension

        if temp is None:
            return 0.0

        return temp

    @property
    def rayleigh_damping_beta(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RayleighDampingBeta' is the original name of this property."""

        temp = self.wrapped.RayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @rayleigh_damping_beta.setter
    def rayleigh_damping_beta(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RayleighDampingBeta = value

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
    def cast_to(self) -> 'BeltConnectionLoadCase._Cast_BeltConnectionLoadCase':
        return self._Cast_BeltConnectionLoadCase(self)
