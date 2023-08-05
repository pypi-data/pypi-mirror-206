"""_6815.py

CouplingConnectionLoadCase
"""
from mastapy.system_model.connections_and_sockets.couplings import _2327
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6875
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CouplingConnectionLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionLoadCase',)


class CouplingConnectionLoadCase(_6875.InterMountableComponentConnectionLoadCase):
    """CouplingConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_LOAD_CASE

    class _Cast_CouplingConnectionLoadCase:
        """Special nested class for casting CouplingConnectionLoadCase to subclasses."""

        def __init__(self, parent: 'CouplingConnectionLoadCase'):
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
        def clutch_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6797
            
            return self._parent._cast(_6797.ClutchConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6802
            
            return self._parent._cast(_6802.ConceptCouplingConnectionLoadCase)

        @property
        def part_to_part_shear_coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6893
            
            return self._parent._cast(_6893.PartToPartShearCouplingConnectionLoadCase)

        @property
        def spring_damper_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6920
            
            return self._parent._cast(_6920.SpringDamperConnectionLoadCase)

        @property
        def torque_converter_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6936
            
            return self._parent._cast(_6936.TorqueConverterConnectionLoadCase)

        @property
        def coupling_connection_load_case(self) -> 'CouplingConnectionLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionLoadCase.TYPE'):
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
    def cast_to(self) -> 'CouplingConnectionLoadCase._Cast_CouplingConnectionLoadCase':
        return self._Cast_CouplingConnectionLoadCase(self)
