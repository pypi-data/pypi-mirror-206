"""_6342.py

SpecialisedAssemblyDynamicAnalysis
"""
from mastapy.system_model.part_model import _2456
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6243
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'SpecialisedAssemblyDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyDynamicAnalysis',)


class SpecialisedAssemblyDynamicAnalysis(_6243.AbstractAssemblyDynamicAnalysis):
    """SpecialisedAssemblyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_DYNAMIC_ANALYSIS

    class _Cast_SpecialisedAssemblyDynamicAnalysis:
        """Special nested class for casting SpecialisedAssemblyDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyDynamicAnalysis'):
            self._parent = parent

        @property
        def abstract_assembly_dynamic_analysis(self):
            return self._parent._cast(_6243.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323
            
            return self._parent._cast(_6323.PartDynamicAnalysis)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.PartFEAnalysis)

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
        def agma_gleason_conical_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6249
            
            return self._parent._cast(_6249.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6253
            
            return self._parent._cast(_6253.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6256
            
            return self._parent._cast(_6256.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6261
            
            return self._parent._cast(_6261.BevelGearSetDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6263
            
            return self._parent._cast(_6263.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6265
            
            return self._parent._cast(_6265.ClutchDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6270
            
            return self._parent._cast(_6270.ConceptCouplingDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6274
            
            return self._parent._cast(_6274.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277
            
            return self._parent._cast(_6277.ConicalGearSetDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281
            
            return self._parent._cast(_6281.CouplingDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284
            
            return self._parent._cast(_6284.CVTDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286
            
            return self._parent._cast(_6286.CycloidalAssemblyDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292
            
            return self._parent._cast(_6292.CylindricalGearSetDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299
            
            return self._parent._cast(_6299.FaceGearSetDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301
            
            return self._parent._cast(_6301.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304
            
            return self._parent._cast(_6304.GearSetDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308
            
            return self._parent._cast(_6308.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312
            
            return self._parent._cast(_6312.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315
            
            return self._parent._cast(_6315.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318
            
            return self._parent._cast(_6318.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325
            
            return self._parent._cast(_6325.PartToPartShearCouplingDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328
            
            return self._parent._cast(_6328.PlanetaryGearSetDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335
            
            return self._parent._cast(_6335.RollingRingAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345
            
            return self._parent._cast(_6345.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347
            
            return self._parent._cast(_6347.SpringDamperDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351
            
            return self._parent._cast(_6351.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354
            
            return self._parent._cast(_6354.StraightBevelGearSetDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357
            
            return self._parent._cast(_6357.SynchroniserDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362
            
            return self._parent._cast(_6362.TorqueConverterDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369
            
            return self._parent._cast(_6369.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372
            
            return self._parent._cast(_6372.ZerolBevelGearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(self) -> 'SpecialisedAssemblyDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyDynamicAnalysis.TYPE'):
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
    def cast_to(self) -> 'SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis':
        return self._Cast_SpecialisedAssemblyDynamicAnalysis(self)
