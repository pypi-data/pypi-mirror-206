"""_7072.py

SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
"""
from mastapy.system_model.part_model import _2456
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2785
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6969
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation',)


class SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation(_6969.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation):
    """SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_6969.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7053
            
            return self._parent._cast(_7053.PartAdvancedTimeSteppingAnalysisForModulation)

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
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6978
            
            return self._parent._cast(_6978.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6983
            
            return self._parent._cast(_6983.BeltDriveAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6986
            
            return self._parent._cast(_6986.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6991
            
            return self._parent._cast(_6991.BevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bolted_joint_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6993
            
            return self._parent._cast(_6993.BoltedJointAdvancedTimeSteppingAnalysisForModulation)

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6994
            
            return self._parent._cast(_6994.ClutchAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6999
            
            return self._parent._cast(_6999.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7004
            
            return self._parent._cast(_7004.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7007
            
            return self._parent._cast(_7007.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7010
            
            return self._parent._cast(_7010.CouplingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7013
            
            return self._parent._cast(_7013.CVTAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7016
            
            return self._parent._cast(_7016.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7022
            
            return self._parent._cast(_7022.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7028
            
            return self._parent._cast(_7028.FaceGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7030
            
            return self._parent._cast(_7030.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7033
            
            return self._parent._cast(_7033.GearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7038
            
            return self._parent._cast(_7038.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7042
            
            return self._parent._cast(_7042.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7045
            
            return self._parent._cast(_7045.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7048
            
            return self._parent._cast(_7048.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7054
            
            return self._parent._cast(_7054.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7058
            
            return self._parent._cast(_7058.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7066
            
            return self._parent._cast(_7066.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7075
            
            return self._parent._cast(_7075.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7076
            
            return self._parent._cast(_7076.SpringDamperAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7081
            
            return self._parent._cast(_7081.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7084
            
            return self._parent._cast(_7084.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7087
            
            return self._parent._cast(_7087.SynchroniserAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7091
            
            return self._parent._cast(_7091.TorqueConverterAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7099
            
            return self._parent._cast(_7099.WormGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7102
            
            return self._parent._cast(_7102.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(self) -> 'SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation.TYPE'):
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
    def cast_to(self) -> 'SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation(self)
