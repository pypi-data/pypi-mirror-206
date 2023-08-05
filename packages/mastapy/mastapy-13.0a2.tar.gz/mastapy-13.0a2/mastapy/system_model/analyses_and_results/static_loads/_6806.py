"""_6806.py

ConceptGearMeshLoadCase
"""
from mastapy.system_model.connections_and_sockets.gears import _2286
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6856
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptGearMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearMeshLoadCase',)


class ConceptGearMeshLoadCase(_6856.GearMeshLoadCase):
    """ConceptGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_LOAD_CASE

    class _Cast_ConceptGearMeshLoadCase:
        """Special nested class for casting ConceptGearMeshLoadCase to subclasses."""

        def __init__(self, parent: 'ConceptGearMeshLoadCase'):
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
        def concept_gear_mesh_load_case(self) -> 'ConceptGearMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2286.ConceptGearMesh':
        """ConceptGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConceptGearMeshLoadCase._Cast_ConceptGearMeshLoadCase':
        return self._Cast_ConceptGearMeshLoadCase(self)
