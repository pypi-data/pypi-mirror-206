"""_4582.py

ConnectionModalAnalysis
"""
from typing import List

from mastapy.system_model.connections_and_sockets import _2253
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _2614
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4699
from mastapy.system_model.analyses_and_results.system_deflections import _2706
from mastapy.system_model.analyses_and_results.analysis_cases import _7503
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ConnectionModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionModalAnalysis',)


class ConnectionModalAnalysis(_7503.ConnectionStaticLoadAnalysisCase):
    """ConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_MODAL_ANALYSIS

    class _Cast_ConnectionModalAnalysis:
        """Special nested class for casting ConnectionModalAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectionModalAnalysis'):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(self):
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
        def abstract_shaft_to_mountable_component_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4550
            
            return self._parent._cast(_4550.AbstractShaftToMountableComponentConnectionModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4551
            
            return self._parent._cast(_4551.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def belt_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4556
            
            return self._parent._cast(_4556.BeltConnectionModalAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4558
            
            return self._parent._cast(_4558.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4563
            
            return self._parent._cast(_4563.BevelGearMeshModalAnalysis)

        @property
        def clutch_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4568
            
            return self._parent._cast(_4568.ClutchConnectionModalAnalysis)

        @property
        def coaxial_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4571
            
            return self._parent._cast(_4571.CoaxialConnectionModalAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573
            
            return self._parent._cast(_4573.ConceptCouplingConnectionModalAnalysis)

        @property
        def concept_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4576
            
            return self._parent._cast(_4576.ConceptGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579
            
            return self._parent._cast(_4579.ConicalGearMeshModalAnalysis)

        @property
        def coupling_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585
            
            return self._parent._cast(_4585.CouplingConnectionModalAnalysis)

        @property
        def cvt_belt_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588
            
            return self._parent._cast(_4588.CVTBeltConnectionModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4592
            
            return self._parent._cast(_4592.CycloidalDiscCentralBearingConnectionModalAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594
            
            return self._parent._cast(_4594.CycloidalDiscPlanetaryBearingConnectionModalAnalysis)

        @property
        def cylindrical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595
            
            return self._parent._cast(_4595.CylindricalGearMeshModalAnalysis)

        @property
        def face_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603
            
            return self._parent._cast(_4603.FaceGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609
            
            return self._parent._cast(_4609.GearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613
            
            return self._parent._cast(_4613.HypoidGearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616
            
            return self._parent._cast(_4616.InterMountableComponentConnectionModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617
            
            return self._parent._cast(_4617.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620
            
            return self._parent._cast(_4620.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623
            
            return self._parent._cast(_4623.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636
            
            return self._parent._cast(_4636.PartToPartShearCouplingConnectionModalAnalysis)

        @property
        def planetary_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639
            
            return self._parent._cast(_4639.PlanetaryConnectionModalAnalysis)

        @property
        def ring_pins_to_disc_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646
            
            return self._parent._cast(_4646.RingPinsToDiscConnectionModalAnalysis)

        @property
        def rolling_ring_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648
            
            return self._parent._cast(_4648.RollingRingConnectionModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654
            
            return self._parent._cast(_4654.ShaftToMountableComponentConnectionModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4656
            
            return self._parent._cast(_4656.SpiralBevelGearMeshModalAnalysis)

        @property
        def spring_damper_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659
            
            return self._parent._cast(_4659.SpringDamperConnectionModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662
            
            return self._parent._cast(_4662.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665
            
            return self._parent._cast(_4665.StraightBevelGearMeshModalAnalysis)

        @property
        def torque_converter_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674
            
            return self._parent._cast(_4674.TorqueConverterConnectionModalAnalysis)

        @property
        def worm_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683
            
            return self._parent._cast(_4683.WormGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686
            
            return self._parent._cast(_4686.ZerolBevelGearMeshModalAnalysis)

        @property
        def connection_modal_analysis(self) -> 'ConnectionModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionModalAnalysis.TYPE'):
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
    def modal_analysis(self) -> '_2614.ModalAnalysis':
        """ModalAnalysis: 'ModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excited_modes_summary(self) -> 'List[_4699.SingleExcitationResultsModalAnalysis]':
        """List[SingleExcitationResultsModalAnalysis]: 'ExcitedModesSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitedModesSummary

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def system_deflection_results(self) -> '_2706.ConnectionSystemDeflection':
        """ConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionModalAnalysis._Cast_ConnectionModalAnalysis':
        return self._Cast_ConnectionModalAnalysis(self)
