"""_6771.py

AbstractAssemblyLoadCase
"""
from mastapy.system_model.part_model import _2414
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6892
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AbstractAssemblyLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyLoadCase',)


class AbstractAssemblyLoadCase(_6892.PartLoadCase):
    """AbstractAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_LOAD_CASE

    class _Cast_AbstractAssemblyLoadCase:
        """Special nested class for casting AbstractAssemblyLoadCase to subclasses."""

        def __init__(self, parent: 'AbstractAssemblyLoadCase'):
            self._parent = parent

        @property
        def part_load_case(self):
            return self._parent._cast(_6892.PartLoadCase)

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
        def agma_gleason_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6780
            
            return self._parent._cast(_6780.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6783
            
            return self._parent._cast(_6783.AssemblyLoadCase)

        @property
        def belt_drive_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6786
            
            return self._parent._cast(_6786.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6789
            
            return self._parent._cast(_6789.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6794
            
            return self._parent._cast(_6794.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6795
            
            return self._parent._cast(_6795.BoltedJointLoadCase)

        @property
        def clutch_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6799
            
            return self._parent._cast(_6799.ClutchLoadCase)

        @property
        def concept_coupling_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6804
            
            return self._parent._cast(_6804.ConceptCouplingLoadCase)

        @property
        def concept_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6807
            
            return self._parent._cast(_6807.ConceptGearSetLoadCase)

        @property
        def conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6812
            
            return self._parent._cast(_6812.ConicalGearSetLoadCase)

        @property
        def coupling_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6817
            
            return self._parent._cast(_6817.CouplingLoadCase)

        @property
        def cvt_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6819
            
            return self._parent._cast(_6819.CVTLoadCase)

        @property
        def cycloidal_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6821
            
            return self._parent._cast(_6821.CycloidalAssemblyLoadCase)

        @property
        def cylindrical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6829
            
            return self._parent._cast(_6829.CylindricalGearSetLoadCase)

        @property
        def face_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6850
            
            return self._parent._cast(_6850.FaceGearSetLoadCase)

        @property
        def flexible_pin_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6852
            
            return self._parent._cast(_6852.FlexiblePinAssemblyLoadCase)

        @property
        def gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6859
            
            return self._parent._cast(_6859.GearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6871
            
            return self._parent._cast(_6871.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6878
            
            return self._parent._cast(_6878.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6881
            
            return self._parent._cast(_6881.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6884
            
            return self._parent._cast(_6884.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6895
            
            return self._parent._cast(_6895.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6897
            
            return self._parent._cast(_6897.PlanetaryGearSetLoadCase)

        @property
        def rolling_ring_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6909
            
            return self._parent._cast(_6909.RollingRingAssemblyLoadCase)

        @property
        def root_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6912
            
            return self._parent._cast(_6912.RootAssemblyLoadCase)

        @property
        def specialised_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6916
            
            return self._parent._cast(_6916.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6919
            
            return self._parent._cast(_6919.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6922
            
            return self._parent._cast(_6922.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6925
            
            return self._parent._cast(_6925.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6928
            
            return self._parent._cast(_6928.StraightBevelGearSetLoadCase)

        @property
        def synchroniser_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6932
            
            return self._parent._cast(_6932.SynchroniserLoadCase)

        @property
        def torque_converter_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6937
            
            return self._parent._cast(_6937.TorqueConverterLoadCase)

        @property
        def worm_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6948
            
            return self._parent._cast(_6948.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6951
            
            return self._parent._cast(_6951.ZerolBevelGearSetLoadCase)

        @property
        def abstract_assembly_load_case(self) -> 'AbstractAssemblyLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyLoadCase.TYPE'):
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
    def cast_to(self) -> 'AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase':
        return self._Cast_AbstractAssemblyLoadCase(self)
