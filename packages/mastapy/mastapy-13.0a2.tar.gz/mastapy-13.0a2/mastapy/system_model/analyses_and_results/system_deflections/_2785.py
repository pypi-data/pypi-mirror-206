"""_2785.py

SpecialisedAssemblySystemDeflection
"""
from mastapy.system_model.part_model import _2456
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4110
from mastapy.system_model.analyses_and_results.system_deflections import _2664
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'SpecialisedAssemblySystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblySystemDeflection',)


class SpecialisedAssemblySystemDeflection(_2664.AbstractAssemblySystemDeflection):
    """SpecialisedAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_SYSTEM_DEFLECTION

    class _Cast_SpecialisedAssemblySystemDeflection:
        """Special nested class for casting SpecialisedAssemblySystemDeflection to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblySystemDeflection'):
            self._parent = parent

        @property
        def abstract_assembly_system_deflection(self):
            return self._parent._cast(_2664.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2764
            
            return self._parent._cast(_2764.PartSystemDeflection)

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
        def agma_gleason_conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2669
            
            return self._parent._cast(_2669.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def belt_drive_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2679
            
            return self._parent._cast(_2679.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2681
            
            return self._parent._cast(_2681.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2686
            
            return self._parent._cast(_2686.BevelGearSetSystemDeflection)

        @property
        def bolted_joint_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2688
            
            return self._parent._cast(_2688.BoltedJointSystemDeflection)

        @property
        def clutch_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2692
            
            return self._parent._cast(_2692.ClutchSystemDeflection)

        @property
        def concept_coupling_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2698
            
            return self._parent._cast(_2698.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2700
            
            return self._parent._cast(_2700.ConceptGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2704
            
            return self._parent._cast(_2704.ConicalGearSetSystemDeflection)

        @property
        def coupling_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2710
            
            return self._parent._cast(_2710.CouplingSystemDeflection)

        @property
        def cvt_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2713
            
            return self._parent._cast(_2713.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2714
            
            return self._parent._cast(_2714.CycloidalAssemblySystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2721
            
            return self._parent._cast(_2721.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2722
            
            return self._parent._cast(_2722.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2723
            
            return self._parent._cast(_2723.CylindricalGearSetSystemDeflectionWithLTCAResults)

        @property
        def face_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2734
            
            return self._parent._cast(_2734.FaceGearSetSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2737
            
            return self._parent._cast(_2737.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2739
            
            return self._parent._cast(_2739.GearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2743
            
            return self._parent._cast(_2743.HypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2748
            
            return self._parent._cast(_2748.KlingelnbergCycloPalloidConicalGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2751
            
            return self._parent._cast(_2751.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2754
            
            return self._parent._cast(_2754.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2767
            
            return self._parent._cast(_2767.PartToPartShearCouplingSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2776
            
            return self._parent._cast(_2776.RollingRingAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2787
            
            return self._parent._cast(_2787.SpiralBevelGearSetSystemDeflection)

        @property
        def spring_damper_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2791
            
            return self._parent._cast(_2791.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2793
            
            return self._parent._cast(_2793.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2796
            
            return self._parent._cast(_2796.StraightBevelGearSetSystemDeflection)

        @property
        def synchroniser_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2803
            
            return self._parent._cast(_2803.SynchroniserSystemDeflection)

        @property
        def torque_converter_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2809
            
            return self._parent._cast(_2809.TorqueConverterSystemDeflection)

        @property
        def worm_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2816
            
            return self._parent._cast(_2816.WormGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2819
            
            return self._parent._cast(_2819.ZerolBevelGearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(self) -> 'SpecialisedAssemblySystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblySystemDeflection.TYPE'):
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
    def power_flow_results(self) -> '_4110.SpecialisedAssemblyPowerFlow':
        """SpecialisedAssemblyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection':
        return self._Cast_SpecialisedAssemblySystemDeflection(self)
