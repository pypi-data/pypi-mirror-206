"""_5253.py

ConnectionCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5124
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7501
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'ConnectionCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionCompoundModalAnalysisAtASpeed',)


class ConnectionCompoundModalAnalysisAtASpeed(_7501.ConnectionCompoundAnalysis):
    """ConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_ConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'ConnectionCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def connection_compound_analysis(self):
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5221
            
            return self._parent._cast(_5221.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5223
            
            return self._parent._cast(_5223.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def belt_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5227
            
            return self._parent._cast(_5227.BeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5230
            
            return self._parent._cast(_5230.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5235
            
            return self._parent._cast(_5235.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def clutch_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5240
            
            return self._parent._cast(_5240.ClutchConnectionCompoundModalAnalysisAtASpeed)

        @property
        def coaxial_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5242
            
            return self._parent._cast(_5242.CoaxialConnectionCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5245
            
            return self._parent._cast(_5245.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5248
            
            return self._parent._cast(_5248.ConceptGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5251
            
            return self._parent._cast(_5251.ConicalGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5256
            
            return self._parent._cast(_5256.CouplingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5258
            
            return self._parent._cast(_5258.CVTBeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5262
            
            return self._parent._cast(_5262.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5264
            
            return self._parent._cast(_5264.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5266
            
            return self._parent._cast(_5266.CylindricalGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5272
            
            return self._parent._cast(_5272.FaceGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5277
            
            return self._parent._cast(_5277.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5281
            
            return self._parent._cast(_5281.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5283
            
            return self._parent._cast(_5283.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5285
            
            return self._parent._cast(_5285.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5288
            
            return self._parent._cast(_5288.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5291
            
            return self._parent._cast(_5291.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5299
            
            return self._parent._cast(_5299.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def planetary_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5301
            
            return self._parent._cast(_5301.PlanetaryConnectionCompoundModalAnalysisAtASpeed)

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5308
            
            return self._parent._cast(_5308.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5311
            
            return self._parent._cast(_5311.RollingRingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5315
            
            return self._parent._cast(_5315.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5318
            
            return self._parent._cast(_5318.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5321
            
            return self._parent._cast(_5321.SpringDamperConnectionCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5324
            
            return self._parent._cast(_5324.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5327
            
            return self._parent._cast(_5327.StraightBevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5336
            
            return self._parent._cast(_5336.TorqueConverterConnectionCompoundModalAnalysisAtASpeed)

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5342
            
            return self._parent._cast(_5342.WormGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5345
            
            return self._parent._cast(_5345.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_modal_analysis_at_a_speed(self) -> 'ConnectionCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_5124.ConnectionModalAnalysisAtASpeed]':
        """List[ConnectionModalAnalysisAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5124.ConnectionModalAnalysisAtASpeed]':
        """List[ConnectionModalAnalysisAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed':
        return self._Cast_ConnectionCompoundModalAnalysisAtASpeed(self)
