"""_6870.py

HypoidGearMeshLoadCase
"""
from mastapy.system_model.connections_and_sockets.gears import _2296
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6779
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HypoidGearMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMeshLoadCase',)


class HypoidGearMeshLoadCase(_6779.AGMAGleasonConicalGearMeshLoadCase):
    """HypoidGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_LOAD_CASE

    class _Cast_HypoidGearMeshLoadCase:
        """Special nested class for casting HypoidGearMeshLoadCase to subclasses."""

        def __init__(self, parent: 'HypoidGearMeshLoadCase'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_load_case(self):
            return self._parent._cast(_6779.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6810
            
            return self._parent._cast(_6810.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6856
            
            return self._parent._cast(_6856.GearMeshLoadCase)

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
        def hypoid_gear_mesh_load_case(self) -> 'HypoidGearMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2296.HypoidGearMesh':
        """HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HypoidGearMeshLoadCase._Cast_HypoidGearMeshLoadCase':
        return self._Cast_HypoidGearMeshLoadCase(self)
