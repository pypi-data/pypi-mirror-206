"""_6471.py

SpecialisedAssemblyCompoundDynamicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6373
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'SpecialisedAssemblyCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyCompoundDynamicAnalysis',)


class SpecialisedAssemblyCompoundDynamicAnalysis(_6373.AbstractAssemblyCompoundDynamicAnalysis):
    """SpecialisedAssemblyCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_SpecialisedAssemblyCompoundDynamicAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def abstract_assembly_compound_dynamic_analysis(self):
            return self._parent._cast(_6373.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6452
            
            return self._parent._cast(_6452.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6379
            
            return self._parent._cast(_6379.AGMAGleasonConicalGearSetCompoundDynamicAnalysis)

        @property
        def belt_drive_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6383
            
            return self._parent._cast(_6383.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6386
            
            return self._parent._cast(_6386.BevelDifferentialGearSetCompoundDynamicAnalysis)

        @property
        def bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6391
            
            return self._parent._cast(_6391.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6393
            
            return self._parent._cast(_6393.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6394
            
            return self._parent._cast(_6394.ClutchCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6399
            
            return self._parent._cast(_6399.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6404
            
            return self._parent._cast(_6404.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6407
            
            return self._parent._cast(_6407.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6410
            
            return self._parent._cast(_6410.CouplingCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6414
            
            return self._parent._cast(_6414.CVTCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6416
            
            return self._parent._cast(_6416.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6422
            
            return self._parent._cast(_6422.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6428
            
            return self._parent._cast(_6428.FaceGearSetCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6430
            
            return self._parent._cast(_6430.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6433
            
            return self._parent._cast(_6433.GearSetCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6437
            
            return self._parent._cast(_6437.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6441
            
            return self._parent._cast(_6441.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6444
            
            return self._parent._cast(_6444.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6447
            
            return self._parent._cast(_6447.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6453
            
            return self._parent._cast(_6453.PartToPartShearCouplingCompoundDynamicAnalysis)

        @property
        def planetary_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6457
            
            return self._parent._cast(_6457.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6464
            
            return self._parent._cast(_6464.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6474
            
            return self._parent._cast(_6474.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6475
            
            return self._parent._cast(_6475.SpringDamperCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6480
            
            return self._parent._cast(_6480.StraightBevelDiffGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6483
            
            return self._parent._cast(_6483.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6486
            
            return self._parent._cast(_6486.SynchroniserCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6490
            
            return self._parent._cast(_6490.TorqueConverterCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6498
            
            return self._parent._cast(_6498.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6501
            
            return self._parent._cast(_6501.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(self) -> 'SpecialisedAssemblyCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_6342.SpecialisedAssemblyDynamicAnalysis]':
        """List[SpecialisedAssemblyDynamicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6342.SpecialisedAssemblyDynamicAnalysis]':
        """List[SpecialisedAssemblyDynamicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis':
        return self._Cast_SpecialisedAssemblyCompoundDynamicAnalysis(self)
