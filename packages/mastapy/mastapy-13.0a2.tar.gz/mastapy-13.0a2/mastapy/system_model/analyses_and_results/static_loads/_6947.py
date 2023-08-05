"""_6947.py

WormGearMeshLoadCase
"""
from mastapy.system_model.connections_and_sockets.gears import _2310
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6856
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'WormGearMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearMeshLoadCase',)


class WormGearMeshLoadCase(_6856.GearMeshLoadCase):
    """WormGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_LOAD_CASE

    class _Cast_WormGearMeshLoadCase:
        """Special nested class for casting WormGearMeshLoadCase to subclasses."""

        def __init__(self, parent: 'WormGearMeshLoadCase'):
            self._parent = parent

        @property
        def gear_mesh_load_case(self):
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
        def worm_gear_mesh_load_case(self) -> 'WormGearMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2310.WormGearMesh':
        """WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGearMeshLoadCase._Cast_WormGearMeshLoadCase':
        return self._Cast_WormGearMeshLoadCase(self)
