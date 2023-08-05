"""_6813.py

ConnectionLoadCase
"""
from mastapy.system_model.connections_and_sockets import _2253
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6769, _6770
from mastapy.system_model.analyses_and_results import _2628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConnectionLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionLoadCase',)


class ConnectionLoadCase(_2628.ConnectionAnalysis):
    """ConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CONNECTION_LOAD_CASE

    class _Cast_ConnectionLoadCase:
        """Special nested class for casting ConnectionLoadCase to subclasses."""

        def __init__(self, parent: 'ConnectionLoadCase'):
            self._parent = parent

        @property
        def connection_analysis(self):
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
        def abstract_shaft_to_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6774
            
            return self._parent._cast(_6774.AbstractShaftToMountableComponentConnectionLoadCase)

        @property
        def agma_gleason_conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6779
            
            return self._parent._cast(_6779.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6785
            
            return self._parent._cast(_6785.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6788
            
            return self._parent._cast(_6788.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6793
            
            return self._parent._cast(_6793.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6797
            
            return self._parent._cast(_6797.ClutchConnectionLoadCase)

        @property
        def coaxial_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6800
            
            return self._parent._cast(_6800.CoaxialConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6802
            
            return self._parent._cast(_6802.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6806
            
            return self._parent._cast(_6806.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6810
            
            return self._parent._cast(_6810.ConicalGearMeshLoadCase)

        @property
        def coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6815
            
            return self._parent._cast(_6815.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6818
            
            return self._parent._cast(_6818.CVTBeltConnectionLoadCase)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6822
            
            return self._parent._cast(_6822.CycloidalDiscCentralBearingConnectionLoadCase)

        @property
        def cycloidal_disc_planetary_bearing_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6824
            
            return self._parent._cast(_6824.CycloidalDiscPlanetaryBearingConnectionLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6827
            
            return self._parent._cast(_6827.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6849
            
            return self._parent._cast(_6849.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6856
            
            return self._parent._cast(_6856.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6870
            
            return self._parent._cast(_6870.HypoidGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6875
            
            return self._parent._cast(_6875.InterMountableComponentConnectionLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6877
            
            return self._parent._cast(_6877.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6880
            
            return self._parent._cast(_6880.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6883
            
            return self._parent._cast(_6883.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        @property
        def part_to_part_shear_coupling_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6893
            
            return self._parent._cast(_6893.PartToPartShearCouplingConnectionLoadCase)

        @property
        def planetary_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6896
            
            return self._parent._cast(_6896.PlanetaryConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6908
            
            return self._parent._cast(_6908.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6910
            
            return self._parent._cast(_6910.RollingRingConnectionLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6915
            
            return self._parent._cast(_6915.ShaftToMountableComponentConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6918
            
            return self._parent._cast(_6918.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6920
            
            return self._parent._cast(_6920.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6924
            
            return self._parent._cast(_6924.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6927
            
            return self._parent._cast(_6927.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6936
            
            return self._parent._cast(_6936.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6947
            
            return self._parent._cast(_6947.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6950
            
            return self._parent._cast(_6950.ZerolBevelGearMeshLoadCase)

        @property
        def connection_load_case(self) -> 'ConnectionLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2253.Connection':
        """Connection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2253.Connection':
        """Connection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def static_load_case(self) -> '_6769.StaticLoadCase':
        """StaticLoadCase: 'StaticLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def time_series_load_case(self) -> '_6770.TimeSeriesLoadCase':
        """TimeSeriesLoadCase: 'TimeSeriesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeSeriesLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionLoadCase._Cast_ConnectionLoadCase':
        return self._Cast_ConnectionLoadCase(self)
