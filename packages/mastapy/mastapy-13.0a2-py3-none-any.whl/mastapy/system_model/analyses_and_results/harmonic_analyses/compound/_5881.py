"""_5881.py

ConnectionCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5685
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7501
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'ConnectionCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionCompoundHarmonicAnalysis',)


class ConnectionCompoundHarmonicAnalysis(_7501.ConnectionCompoundAnalysis):
    """ConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_ConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting ConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectionCompoundHarmonicAnalysis'):
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
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5849
            
            return self._parent._cast(_5849.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5851
            
            return self._parent._cast(_5851.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def belt_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5855
            
            return self._parent._cast(_5855.BeltConnectionCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5858
            
            return self._parent._cast(_5858.BevelDifferentialGearMeshCompoundHarmonicAnalysis)

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5863
            
            return self._parent._cast(_5863.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def clutch_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5868
            
            return self._parent._cast(_5868.ClutchConnectionCompoundHarmonicAnalysis)

        @property
        def coaxial_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5870
            
            return self._parent._cast(_5870.CoaxialConnectionCompoundHarmonicAnalysis)

        @property
        def concept_coupling_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5873
            
            return self._parent._cast(_5873.ConceptCouplingConnectionCompoundHarmonicAnalysis)

        @property
        def concept_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5876
            
            return self._parent._cast(_5876.ConceptGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5879
            
            return self._parent._cast(_5879.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def coupling_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5884
            
            return self._parent._cast(_5884.CouplingConnectionCompoundHarmonicAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5886
            
            return self._parent._cast(_5886.CVTBeltConnectionCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5890
            
            return self._parent._cast(_5890.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5892
            
            return self._parent._cast(_5892.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5894
            
            return self._parent._cast(_5894.CylindricalGearMeshCompoundHarmonicAnalysis)

        @property
        def face_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5900
            
            return self._parent._cast(_5900.FaceGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5905
            
            return self._parent._cast(_5905.GearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5909
            
            return self._parent._cast(_5909.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5911
            
            return self._parent._cast(_5911.InterMountableComponentConnectionCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5913
            
            return self._parent._cast(_5913.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5916
            
            return self._parent._cast(_5916.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5919
            
            return self._parent._cast(_5919.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5927
            
            return self._parent._cast(_5927.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis)

        @property
        def planetary_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5929
            
            return self._parent._cast(_5929.PlanetaryConnectionCompoundHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5936
            
            return self._parent._cast(_5936.RingPinsToDiscConnectionCompoundHarmonicAnalysis)

        @property
        def rolling_ring_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5939
            
            return self._parent._cast(_5939.RollingRingConnectionCompoundHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5943
            
            return self._parent._cast(_5943.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5946
            
            return self._parent._cast(_5946.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def spring_damper_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5949
            
            return self._parent._cast(_5949.SpringDamperConnectionCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5952
            
            return self._parent._cast(_5952.StraightBevelDiffGearMeshCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5955
            
            return self._parent._cast(_5955.StraightBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def torque_converter_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5964
            
            return self._parent._cast(_5964.TorqueConverterConnectionCompoundHarmonicAnalysis)

        @property
        def worm_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5970
            
            return self._parent._cast(_5970.WormGearMeshCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5973
            
            return self._parent._cast(_5973.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def connection_compound_harmonic_analysis(self) -> 'ConnectionCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_5685.ConnectionHarmonicAnalysis]':
        """List[ConnectionHarmonicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5685.ConnectionHarmonicAnalysis]':
        """List[ConnectionHarmonicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectionCompoundHarmonicAnalysis._Cast_ConnectionCompoundHarmonicAnalysis':
        return self._Cast_ConnectionCompoundHarmonicAnalysis(self)
