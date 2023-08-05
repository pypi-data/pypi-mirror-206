"""_3909.py

ConnectionCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3777
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7501
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'ConnectionCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionCompoundStabilityAnalysis',)


class ConnectionCompoundStabilityAnalysis(_7501.ConnectionCompoundAnalysis):
    """ConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_STABILITY_ANALYSIS

    class _Cast_ConnectionCompoundStabilityAnalysis:
        """Special nested class for casting ConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectionCompoundStabilityAnalysis'):
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
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3877
            
            return self._parent._cast(_3877.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3879
            
            return self._parent._cast(_3879.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis)

        @property
        def belt_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3883
            
            return self._parent._cast(_3883.BeltConnectionCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3886
            
            return self._parent._cast(_3886.BevelDifferentialGearMeshCompoundStabilityAnalysis)

        @property
        def bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3891
            
            return self._parent._cast(_3891.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def clutch_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3896
            
            return self._parent._cast(_3896.ClutchConnectionCompoundStabilityAnalysis)

        @property
        def coaxial_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3898
            
            return self._parent._cast(_3898.CoaxialConnectionCompoundStabilityAnalysis)

        @property
        def concept_coupling_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3901
            
            return self._parent._cast(_3901.ConceptCouplingConnectionCompoundStabilityAnalysis)

        @property
        def concept_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3904
            
            return self._parent._cast(_3904.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3907
            
            return self._parent._cast(_3907.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def coupling_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3912
            
            return self._parent._cast(_3912.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def cvt_belt_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3914
            
            return self._parent._cast(_3914.CVTBeltConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3918
            
            return self._parent._cast(_3918.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3920
            
            return self._parent._cast(_3920.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3922
            
            return self._parent._cast(_3922.CylindricalGearMeshCompoundStabilityAnalysis)

        @property
        def face_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3928
            
            return self._parent._cast(_3928.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3933
            
            return self._parent._cast(_3933.GearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3937
            
            return self._parent._cast(_3937.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3939
            
            return self._parent._cast(_3939.InterMountableComponentConnectionCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3941
            
            return self._parent._cast(_3941.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3944
            
            return self._parent._cast(_3944.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3947
            
            return self._parent._cast(_3947.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3955
            
            return self._parent._cast(_3955.PartToPartShearCouplingConnectionCompoundStabilityAnalysis)

        @property
        def planetary_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3957
            
            return self._parent._cast(_3957.PlanetaryConnectionCompoundStabilityAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3964
            
            return self._parent._cast(_3964.RingPinsToDiscConnectionCompoundStabilityAnalysis)

        @property
        def rolling_ring_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3967
            
            return self._parent._cast(_3967.RollingRingConnectionCompoundStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3971
            
            return self._parent._cast(_3971.ShaftToMountableComponentConnectionCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3974
            
            return self._parent._cast(_3974.SpiralBevelGearMeshCompoundStabilityAnalysis)

        @property
        def spring_damper_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3977
            
            return self._parent._cast(_3977.SpringDamperConnectionCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3980
            
            return self._parent._cast(_3980.StraightBevelDiffGearMeshCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3983
            
            return self._parent._cast(_3983.StraightBevelGearMeshCompoundStabilityAnalysis)

        @property
        def torque_converter_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3992
            
            return self._parent._cast(_3992.TorqueConverterConnectionCompoundStabilityAnalysis)

        @property
        def worm_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3998
            
            return self._parent._cast(_3998.WormGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4001
            
            return self._parent._cast(_4001.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def connection_compound_stability_analysis(self) -> 'ConnectionCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_3777.ConnectionStabilityAnalysis]':
        """List[ConnectionStabilityAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3777.ConnectionStabilityAnalysis]':
        """List[ConnectionStabilityAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis':
        return self._Cast_ConnectionCompoundStabilityAnalysis(self)
