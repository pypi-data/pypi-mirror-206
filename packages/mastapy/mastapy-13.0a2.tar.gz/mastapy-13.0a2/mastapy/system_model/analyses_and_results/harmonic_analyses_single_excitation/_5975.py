"""_5975.py

AbstractAssemblyHarmonicAnalysisOfSingleExcitation
"""
from mastapy.system_model.part_model import _2414
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6055
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'AbstractAssemblyHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyHarmonicAnalysisOfSingleExcitation',)


class AbstractAssemblyHarmonicAnalysisOfSingleExcitation(_6055.PartHarmonicAnalysisOfSingleExcitation):
    """AbstractAssemblyHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractAssemblyHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'AbstractAssemblyHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def part_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6055.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5981
            
            return self._parent._cast(_5981.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5982
            
            return self._parent._cast(_5982.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5985
            
            return self._parent._cast(_5985.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5988
            
            return self._parent._cast(_5988.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5993
            
            return self._parent._cast(_5993.BevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5994
            
            return self._parent._cast(_5994.BoltedJointHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5998
            
            return self._parent._cast(_5998.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6003
            
            return self._parent._cast(_6003.ConceptCouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6006
            
            return self._parent._cast(_6006.ConceptGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6009
            
            return self._parent._cast(_6009.ConicalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6014
            
            return self._parent._cast(_6014.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6016
            
            return self._parent._cast(_6016.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6018
            
            return self._parent._cast(_6018.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6024
            
            return self._parent._cast(_6024.CylindricalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6030
            
            return self._parent._cast(_6030.FaceGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6032
            
            return self._parent._cast(_6032.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6035
            
            return self._parent._cast(_6035.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6040
            
            return self._parent._cast(_6040.HypoidGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6044
            
            return self._parent._cast(_6044.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6047
            
            return self._parent._cast(_6047.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6050
            
            return self._parent._cast(_6050.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6058
            
            return self._parent._cast(_6058.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6060
            
            return self._parent._cast(_6060.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6067
            
            return self._parent._cast(_6067.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6070
            
            return self._parent._cast(_6070.RootAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6074
            
            return self._parent._cast(_6074.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6077
            
            return self._parent._cast(_6077.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6080
            
            return self._parent._cast(_6080.SpringDamperHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6083
            
            return self._parent._cast(_6083.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6086
            
            return self._parent._cast(_6086.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6090
            
            return self._parent._cast(_6090.SynchroniserHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6094
            
            return self._parent._cast(_6094.TorqueConverterHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6101
            
            return self._parent._cast(_6101.WormGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6104
            
            return self._parent._cast(_6104.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(self) -> 'AbstractAssemblyHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2414.AbstractAssembly':
        """AbstractAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2414.AbstractAssembly':
        """AbstractAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation':
        return self._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation(self)
