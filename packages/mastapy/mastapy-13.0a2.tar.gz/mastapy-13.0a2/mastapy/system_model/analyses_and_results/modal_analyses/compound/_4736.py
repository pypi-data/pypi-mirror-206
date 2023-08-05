"""_4736.py

ConnectionCompoundModalAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses import _4582
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7501
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'ConnectionCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionCompoundModalAnalysis',)


class ConnectionCompoundModalAnalysis(_7501.ConnectionCompoundAnalysis):
    """ConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_MODAL_ANALYSIS

    class _Cast_ConnectionCompoundModalAnalysis:
        """Special nested class for casting ConnectionCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectionCompoundModalAnalysis'):
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
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4704
            
            return self._parent._cast(_4704.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4706
            
            return self._parent._cast(_4706.AGMAGleasonConicalGearMeshCompoundModalAnalysis)

        @property
        def belt_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4710
            
            return self._parent._cast(_4710.BeltConnectionCompoundModalAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4713
            
            return self._parent._cast(_4713.BevelDifferentialGearMeshCompoundModalAnalysis)

        @property
        def bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4718
            
            return self._parent._cast(_4718.BevelGearMeshCompoundModalAnalysis)

        @property
        def clutch_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4723
            
            return self._parent._cast(_4723.ClutchConnectionCompoundModalAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4725
            
            return self._parent._cast(_4725.CoaxialConnectionCompoundModalAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4728
            
            return self._parent._cast(_4728.ConceptCouplingConnectionCompoundModalAnalysis)

        @property
        def concept_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4731
            
            return self._parent._cast(_4731.ConceptGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4734
            
            return self._parent._cast(_4734.ConicalGearMeshCompoundModalAnalysis)

        @property
        def coupling_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4739
            
            return self._parent._cast(_4739.CouplingConnectionCompoundModalAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4741
            
            return self._parent._cast(_4741.CVTBeltConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4745
            
            return self._parent._cast(_4745.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4747
            
            return self._parent._cast(_4747.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis)

        @property
        def cylindrical_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4749
            
            return self._parent._cast(_4749.CylindricalGearMeshCompoundModalAnalysis)

        @property
        def face_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4755
            
            return self._parent._cast(_4755.FaceGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4760
            
            return self._parent._cast(_4760.GearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4764
            
            return self._parent._cast(_4764.HypoidGearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4766
            
            return self._parent._cast(_4766.InterMountableComponentConnectionCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4768
            
            return self._parent._cast(_4768.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4771
            
            return self._parent._cast(_4771.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4774
            
            return self._parent._cast(_4774.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4782
            
            return self._parent._cast(_4782.PartToPartShearCouplingConnectionCompoundModalAnalysis)

        @property
        def planetary_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4784
            
            return self._parent._cast(_4784.PlanetaryConnectionCompoundModalAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4791
            
            return self._parent._cast(_4791.RingPinsToDiscConnectionCompoundModalAnalysis)

        @property
        def rolling_ring_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4794
            
            return self._parent._cast(_4794.RollingRingConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4798
            
            return self._parent._cast(_4798.ShaftToMountableComponentConnectionCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4801
            
            return self._parent._cast(_4801.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4804
            
            return self._parent._cast(_4804.SpringDamperConnectionCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4807
            
            return self._parent._cast(_4807.StraightBevelDiffGearMeshCompoundModalAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4810
            
            return self._parent._cast(_4810.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4819
            
            return self._parent._cast(_4819.TorqueConverterConnectionCompoundModalAnalysis)

        @property
        def worm_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4825
            
            return self._parent._cast(_4825.WormGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4828
            
            return self._parent._cast(_4828.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def connection_compound_modal_analysis(self) -> 'ConnectionCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4582.ConnectionModalAnalysis]':
        """List[ConnectionModalAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4582.ConnectionModalAnalysis]':
        """List[ConnectionModalAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectionCompoundModalAnalysis._Cast_ConnectionCompoundModalAnalysis':
        return self._Cast_ConnectionCompoundModalAnalysis(self)
