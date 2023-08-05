"""_5777.py

SpecialisedAssemblyHarmonicAnalysis
"""
from mastapy.system_model.part_model import _2456
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2785
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5648
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'SpecialisedAssemblyHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyHarmonicAnalysis',)


class SpecialisedAssemblyHarmonicAnalysis(_5648.AbstractAssemblyHarmonicAnalysis):
    """SpecialisedAssemblyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_HARMONIC_ANALYSIS

    class _Cast_SpecialisedAssemblyHarmonicAnalysis:
        """Special nested class for casting SpecialisedAssemblyHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyHarmonicAnalysis'):
            self._parent = parent

        @property
        def abstract_assembly_harmonic_analysis(self):
            return self._parent._cast(_5648.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5755
            
            return self._parent._cast(_5755.PartHarmonicAnalysis)

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
        def agma_gleason_conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5655
            
            return self._parent._cast(_5655.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5659
            
            return self._parent._cast(_5659.BeltDriveHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5662
            
            return self._parent._cast(_5662.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5667
            
            return self._parent._cast(_5667.BevelGearSetHarmonicAnalysis)

        @property
        def bolted_joint_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5668
            
            return self._parent._cast(_5668.BoltedJointHarmonicAnalysis)

        @property
        def clutch_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5672
            
            return self._parent._cast(_5672.ClutchHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5678
            
            return self._parent._cast(_5678.ConceptCouplingHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5681
            
            return self._parent._cast(_5681.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5684
            
            return self._parent._cast(_5684.ConicalGearSetHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5689
            
            return self._parent._cast(_5689.CouplingHarmonicAnalysis)

        @property
        def cvt_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5691
            
            return self._parent._cast(_5691.CVTHarmonicAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5693
            
            return self._parent._cast(_5693.CycloidalAssemblyHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5699
            
            return self._parent._cast(_5699.CylindricalGearSetHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5718
            
            return self._parent._cast(_5718.FaceGearSetHarmonicAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5720
            
            return self._parent._cast(_5720.FlexiblePinAssemblyHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5727
            
            return self._parent._cast(_5727.GearSetHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5740
            
            return self._parent._cast(_5740.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5744
            
            return self._parent._cast(_5744.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5747
            
            return self._parent._cast(_5747.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5750
            
            return self._parent._cast(_5750.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5758
            
            return self._parent._cast(_5758.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5761
            
            return self._parent._cast(_5761.PlanetaryGearSetHarmonicAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5769
            
            return self._parent._cast(_5769.RollingRingAssemblyHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5781
            
            return self._parent._cast(_5781.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5784
            
            return self._parent._cast(_5784.SpringDamperHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5788
            
            return self._parent._cast(_5788.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5791
            
            return self._parent._cast(_5791.StraightBevelGearSetHarmonicAnalysis)

        @property
        def synchroniser_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5795
            
            return self._parent._cast(_5795.SynchroniserHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5799
            
            return self._parent._cast(_5799.TorqueConverterHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807
            
            return self._parent._cast(_5807.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5810
            
            return self._parent._cast(_5810.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(self) -> 'SpecialisedAssemblyHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2456.SpecialisedAssembly':
        """SpecialisedAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2785.SpecialisedAssemblySystemDeflection':
        """SpecialisedAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis':
        return self._Cast_SpecialisedAssemblyHarmonicAnalysis(self)
