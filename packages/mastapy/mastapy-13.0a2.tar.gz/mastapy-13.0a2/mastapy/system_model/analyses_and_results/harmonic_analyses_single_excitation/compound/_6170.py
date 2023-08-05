"""_6170.py

InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6041
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6140
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation',)


class InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation(_6140.ConnectionCompoundHarmonicAnalysisOfSingleExcitation):
    """InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6140.ConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
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
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6110
            
            return self._parent._cast(_6110.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6114
            
            return self._parent._cast(_6114.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6117
            
            return self._parent._cast(_6117.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6122
            
            return self._parent._cast(_6122.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6127
            
            return self._parent._cast(_6127.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6132
            
            return self._parent._cast(_6132.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6135
            
            return self._parent._cast(_6135.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6138
            
            return self._parent._cast(_6138.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6143
            
            return self._parent._cast(_6143.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_belt_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6145
            
            return self._parent._cast(_6145.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6153
            
            return self._parent._cast(_6153.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6159
            
            return self._parent._cast(_6159.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6164
            
            return self._parent._cast(_6164.GearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6168
            
            return self._parent._cast(_6168.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6172
            
            return self._parent._cast(_6172.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6175
            
            return self._parent._cast(_6175.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6178
            
            return self._parent._cast(_6178.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6186
            
            return self._parent._cast(_6186.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6195
            
            return self._parent._cast(_6195.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6198
            
            return self._parent._cast(_6198.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6205
            
            return self._parent._cast(_6205.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6208
            
            return self._parent._cast(_6208.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6211
            
            return self._parent._cast(_6211.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6214
            
            return self._parent._cast(_6214.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6223
            
            return self._parent._cast(_6223.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6229
            
            return self._parent._cast(_6229.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6232
            
            return self._parent._cast(_6232.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(self) -> 'InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6041.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]':
        """List[InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6041.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]':
        """List[InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation(self)
