"""_4020.py

BevelDifferentialGearMeshPowerFlow
"""
from mastapy.gears.rating.bevel import _549
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2282
from mastapy.system_model.analyses_and_results.static_loads import _6788
from mastapy.system_model.analyses_and_results.power_flows import _4025
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'BevelDifferentialGearMeshPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearMeshPowerFlow',)


class BevelDifferentialGearMeshPowerFlow(_4025.BevelGearMeshPowerFlow):
    """BevelDifferentialGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_POWER_FLOW

    class _Cast_BevelDifferentialGearMeshPowerFlow:
        """Special nested class for casting BevelDifferentialGearMeshPowerFlow to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearMeshPowerFlow'):
            self._parent = parent

        @property
        def bevel_gear_mesh_power_flow(self):
            return self._parent._cast(_4025.BevelGearMeshPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4013
            
            return self._parent._cast(_4013.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4041
            
            return self._parent._cast(_4041.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4068
            
            return self._parent._cast(_4068.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4075
            
            return self._parent._cast(_4075.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4044
            
            return self._parent._cast(_4044.ConnectionPowerFlow)

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
        def bevel_differential_gear_mesh_power_flow(self) -> 'BevelDifferentialGearMeshPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearMeshPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> '_549.BevelGearMeshRating':
        """BevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_549.BevelGearMeshRating':
        """BevelGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2282.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6788.BevelDifferentialGearMeshLoadCase':
        """BevelDifferentialGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelDifferentialGearMeshPowerFlow._Cast_BevelDifferentialGearMeshPowerFlow':
        return self._Cast_BevelDifferentialGearMeshPowerFlow(self)
