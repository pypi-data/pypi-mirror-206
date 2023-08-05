"""_6008.py

ConicalGearMeshHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2288
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6034
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'ConicalGearMeshHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshHarmonicAnalysisOfSingleExcitation',)


class ConicalGearMeshHarmonicAnalysisOfSingleExcitation(_6034.GearMeshHarmonicAnalysisOfSingleExcitation):
    """ConicalGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_ConicalGearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConicalGearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'ConicalGearMeshHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6034.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6041
            
            return self._parent._cast(_6041.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6010
            
            return self._parent._cast(_6010.ConnectionHarmonicAnalysisOfSingleExcitation)

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
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5980
            
            return self._parent._cast(_5980.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5987
            
            return self._parent._cast(_5987.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5992
            
            return self._parent._cast(_5992.BevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6039
            
            return self._parent._cast(_6039.HypoidGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6043
            
            return self._parent._cast(_6043.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6046
            
            return self._parent._cast(_6046.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6049
            
            return self._parent._cast(_6049.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6076
            
            return self._parent._cast(_6076.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6082
            
            return self._parent._cast(_6082.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6085
            
            return self._parent._cast(_6085.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6103
            
            return self._parent._cast(_6103.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(self) -> 'ConicalGearMeshHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2288.ConicalGearMesh':
        """ConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ConicalGearMeshHarmonicAnalysisOfSingleExcitation]':
        """List[ConicalGearMeshHarmonicAnalysisOfSingleExcitation]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearMeshHarmonicAnalysisOfSingleExcitation':
        return self._Cast_ConicalGearMeshHarmonicAnalysisOfSingleExcitation(self)
