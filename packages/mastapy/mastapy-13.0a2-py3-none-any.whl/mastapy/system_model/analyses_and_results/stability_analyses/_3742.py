"""_3742.py

AbstractAssemblyStabilityAnalysis
"""
from mastapy.system_model.part_model import _2414
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3822
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'AbstractAssemblyStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyStabilityAnalysis',)


class AbstractAssemblyStabilityAnalysis(_3822.PartStabilityAnalysis):
    """AbstractAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_STABILITY_ANALYSIS

    class _Cast_AbstractAssemblyStabilityAnalysis:
        """Special nested class for casting AbstractAssemblyStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractAssemblyStabilityAnalysis'):
            self._parent = parent

        @property
        def part_stability_analysis(self):
            return self._parent._cast(_3822.PartStabilityAnalysis)

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
        def agma_gleason_conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3747
            
            return self._parent._cast(_3747.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3749
            
            return self._parent._cast(_3749.AssemblyStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3752
            
            return self._parent._cast(_3752.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3754
            
            return self._parent._cast(_3754.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3759
            
            return self._parent._cast(_3759.BevelGearSetStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3761
            
            return self._parent._cast(_3761.BoltedJointStabilityAnalysis)

        @property
        def clutch_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3765
            
            return self._parent._cast(_3765.ClutchStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3770
            
            return self._parent._cast(_3770.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3772
            
            return self._parent._cast(_3772.ConceptGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3775
            
            return self._parent._cast(_3775.ConicalGearSetStabilityAnalysis)

        @property
        def coupling_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3781
            
            return self._parent._cast(_3781.CouplingStabilityAnalysis)

        @property
        def cvt_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3785
            
            return self._parent._cast(_3785.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3786
            
            return self._parent._cast(_3786.CycloidalAssemblyStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3791
            
            return self._parent._cast(_3791.CylindricalGearSetStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3797
            
            return self._parent._cast(_3797.FaceGearSetStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3800
            
            return self._parent._cast(_3800.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3802
            
            return self._parent._cast(_3802.GearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3806
            
            return self._parent._cast(_3806.HypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3810
            
            return self._parent._cast(_3810.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3813
            
            return self._parent._cast(_3813.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3816
            
            return self._parent._cast(_3816.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3825
            
            return self._parent._cast(_3825.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3827
            
            return self._parent._cast(_3827.PlanetaryGearSetStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3834
            
            return self._parent._cast(_3834.RollingRingAssemblyStabilityAnalysis)

        @property
        def root_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3837
            
            return self._parent._cast(_3837.RootAssemblyStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3841
            
            return self._parent._cast(_3841.SpecialisedAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3843
            
            return self._parent._cast(_3843.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3847
            
            return self._parent._cast(_3847.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3851
            
            return self._parent._cast(_3851.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3854
            
            return self._parent._cast(_3854.StraightBevelGearSetStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3861
            
            return self._parent._cast(_3861.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3864
            
            return self._parent._cast(_3864.TorqueConverterStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3869
            
            return self._parent._cast(_3869.WormGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3872
            
            return self._parent._cast(_3872.ZerolBevelGearSetStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(self) -> 'AbstractAssemblyStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyStabilityAnalysis.TYPE'):
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
    def cast_to(self) -> 'AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis':
        return self._Cast_AbstractAssemblyStabilityAnalysis(self)
