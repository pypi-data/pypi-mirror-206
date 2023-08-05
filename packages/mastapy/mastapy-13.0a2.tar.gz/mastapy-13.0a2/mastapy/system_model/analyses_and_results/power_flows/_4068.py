"""_4068.py

GearMeshPowerFlow
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets.gears import _2294
from mastapy.gears.rating import _356
from mastapy.system_model.analyses_and_results.power_flows import _4129, _4075
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'GearMeshPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshPowerFlow',)


class GearMeshPowerFlow(_4075.InterMountableComponentConnectionPowerFlow):
    """GearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_POWER_FLOW

    class _Cast_GearMeshPowerFlow:
        """Special nested class for casting GearMeshPowerFlow to subclasses."""

        def __init__(self, parent: 'GearMeshPowerFlow'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_power_flow(self):
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
        def agma_gleason_conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4013
            
            return self._parent._cast(_4013.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4020
            
            return self._parent._cast(_4020.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4025
            
            return self._parent._cast(_4025.BevelGearMeshPowerFlow)

        @property
        def concept_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4038
            
            return self._parent._cast(_4038.ConceptGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4041
            
            return self._parent._cast(_4041.ConicalGearMeshPowerFlow)

        @property
        def cylindrical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4057
            
            return self._parent._cast(_4057.CylindricalGearMeshPowerFlow)

        @property
        def face_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4063
            
            return self._parent._cast(_4063.FaceGearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4072
            
            return self._parent._cast(_4072.HypoidGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4076
            
            return self._parent._cast(_4076.KlingelnbergCycloPalloidConicalGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4079
            
            return self._parent._cast(_4079.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4082
            
            return self._parent._cast(_4082.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow)

        @property
        def spiral_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4111
            
            return self._parent._cast(_4111.SpiralBevelGearMeshPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4117
            
            return self._parent._cast(_4117.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4120
            
            return self._parent._cast(_4120.StraightBevelGearMeshPowerFlow)

        @property
        def worm_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4136
            
            return self._parent._cast(_4136.WormGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4139
            
            return self._parent._cast(_4139.ZerolBevelGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(self) -> 'GearMeshPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a_tooth_passing_speed(self) -> 'float':
        """float: 'GearAToothPassingSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearAToothPassingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_tooth_passing_speed(self) -> 'float':
        """float: 'GearBToothPassingSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBToothPassingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_frequency(self) -> 'float':
        """float: 'ToothPassingFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothPassingFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self) -> '_2294.GearMesh':
        """GearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_356.GearMeshRating':
        """GearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tooth_passing_harmonics(self) -> 'List[_4129.ToothPassingHarmonic]':
        """List[ToothPassingHarmonic]: 'ToothPassingHarmonics' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothPassingHarmonics

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshPowerFlow._Cast_GearMeshPowerFlow':
        return self._Cast_GearMeshPowerFlow(self)
